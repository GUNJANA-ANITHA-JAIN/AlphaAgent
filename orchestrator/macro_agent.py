"""
Macro agent: VIX from yfinance (cached) plus optional FRED yield spread.

Network work stays off the asyncio lock with a short timeout so other agents keep moving.
"""

from __future__ import annotations

import asyncio
import logging
import os
import time
from datetime import datetime, timezone
from typing import Optional

import requests

from core.models import EventType, MarketEvent

from .agent_debug import log_agent
from .orchestrator import PartialSignal, SubAgent

logger = logging.getLogger("MacroAgent")

_FETCH_TIMEOUT_SEC = float(os.environ.get("ALPHAGENT_MACRO_FETCH_TIMEOUT", "6"))


def _fetch_vix_close() -> float | None:
    try:
        import yfinance as yf

        h = yf.Ticker("^VIX").history(period="5d", interval="1d", auto_adjust=True)
        if h is None or h.empty:
            return None
        return float(h["Close"].iloc[-1])
    except Exception as e:
        logger.debug("VIX fetch failed: %s", e)
        return None


def _vix_to_score(vix: float) -> tuple[float, str]:
    if vix >= 32:
        return -0.35, f"Very high fear (VIX≈{vix:.1f})"
    if vix >= 26:
        return -0.18, f"Elevated fear (VIX≈{vix:.1f})"
    if vix >= 20:
        return -0.05, f"Normal stress (VIX≈{vix:.1f})"
    if vix <= 14:
        return 0.08, f"Complacency risk / low vol (VIX≈{vix:.1f})"
    return 0.02, f"Calm backdrop (VIX≈{vix:.1f})"


def _fred_fetch_latest_spread_pct() -> float | None:
    """Latest 10Y minus 2Y spread (%). Needs FRED_API_KEY."""
    api_key = os.environ.get("FRED_API_KEY", "").strip()
    if not api_key:
        return None
    series_id = (os.environ.get("ALPHAGENT_FRED_SERIES_ID", "T10Y2Y") or "T10Y2Y").strip()
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "api_key": api_key,
        "file_type": "json",
        "sort_order": "desc",
        "limit": 1,
    }
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    obs = r.json().get("observations") or []
    if not obs:
        return None
    raw = obs[0].get("value")
    if raw is None or raw == ".":
        return None
    return float(raw)


def _fred_spread_adjustment(spread_pct: float) -> tuple[float, str]:
    """Small score nudge from yield-curve shape."""
    if spread_pct < -0.05:
        return -0.07, f"10Y–2Y {spread_pct:.2f}% (inverted)"
    if spread_pct < 0:
        return -0.03, f"10Y–2Y flat/inverted {spread_pct:.2f}%"
    if spread_pct > 1.2:
        return 0.04, f"Steep curve 10Y–2Y {spread_pct:.2f}%"
    if spread_pct > 0.5:
        return 0.02, f"Healthy slope 10Y–2Y {spread_pct:.2f}%"
    return 0.0, f"Curve {spread_pct:.2f}% (neutral)"


class MacroAgent(SubAgent):
    name = "macro"

    def __init__(self, cache_ttl_sec: float | None = None):
        self._ttl = float(
            cache_ttl_sec if cache_ttl_sec is not None else os.environ.get("ALPHAGENT_MACRO_CACHE_SEC", "900")
        )
        self._vix: float | None = None
        self._fetched_at: float = 0.0
        self._lock = asyncio.Lock()
        self._last_fail_at: float = 0.0
        self._fail_ttl = float(os.environ.get("ALPHAGENT_MACRO_FAIL_CACHE_SEC", "300"))
        self._fred_spread: float | None = None
        self._fred_fetched_at: float = 0.0
        self._fred_lock = asyncio.Lock()

    async def _get_vix(self) -> float | None:
        now = time.monotonic()
        async with self._lock:
            if self._vix is not None and (now - self._fetched_at) < self._ttl:
                return self._vix
            if (
                self._vix is None
                and self._last_fail_at > 0.0
                and (now - self._last_fail_at) < self._fail_ttl
            ):
                return None

        try:
            v = await asyncio.wait_for(
                asyncio.to_thread(_fetch_vix_close),
                timeout=_FETCH_TIMEOUT_SEC,
            )
        except asyncio.TimeoutError:
            logger.warning("VIX fetch timed out after %.0fs — macro abstains", _FETCH_TIMEOUT_SEC)
            v = None
        except Exception as e:
            logger.debug("VIX fetch error: %s", e)
            v = None

        async with self._lock:
            if v is None:
                self._last_fail_at = time.monotonic()
                return None
            self._vix = v
            self._fetched_at = time.monotonic()
            logger.info("Macro VIX refreshed: %.2f (cache %ds)", v, int(self._ttl))
            return self._vix

    async def _get_fred_spread(self) -> float | None:
        if not os.environ.get("FRED_API_KEY", "").strip():
            return None
        now = time.monotonic()
        async with self._fred_lock:
            if self._fred_spread is not None and (now - self._fred_fetched_at) < self._ttl:
                return self._fred_spread
        try:
            spread = await asyncio.wait_for(
                asyncio.to_thread(_fred_fetch_latest_spread_pct),
                timeout=float(os.environ.get("ALPHAGENT_FRED_FETCH_TIMEOUT", "8")),
            )
        except asyncio.TimeoutError:
            logger.warning("FRED spread fetch timed out")
            spread = None
        except Exception as e:
            logger.debug("FRED spread fetch error: %s", e)
            spread = None
        async with self._fred_lock:
            if spread is not None:
                self._fred_spread = spread
                self._fred_fetched_at = time.monotonic()
                logger.info("Macro FRED spread refreshed: %.3f%%", spread)
            if self._fred_spread is not None and (time.monotonic() - self._fred_fetched_at) < self._ttl:
                return self._fred_spread
            return None

    async def process(self, event: MarketEvent) -> Optional[PartialSignal]:
        if event.event_type not in (
            EventType.NEWS_ARTICLE,
            EventType.PRICE_UPDATE,
            EventType.SEC_FILING,
            EventType.SOCIAL_POST,
            EventType.EARNINGS_CALL,
        ):
            return None

        vix = await self._get_vix()
        eid = [event.event_id] if event.event_id else []
        if vix is None:
            log_agent(
                "macro",
                "%s VIX unavailable — emitting neutral backdrop partial",
                event.ticker,
            )
            return PartialSignal(
                agent_name="macro",
                ticker=event.ticker,
                score=0.0,
                confidence=0.24,
                timestamp=datetime.now(timezone.utc),
                reasoning="Macro: VIX fetch failed or offline (neutral backdrop; retry later)",
                decay_hours=6.0,
                source_event_ids=eid,
            )

        score, reason = _vix_to_score(vix)
        spread = await self._get_fred_spread()
        if spread is not None:
            adj, fred_note = _fred_spread_adjustment(spread)
            score = max(-1.0, min(1.0, score + adj))
            reason = f"{reason} | FRED {fred_note}"
            log_agent("macro", "%s FRED T10Y2Y=%.3f adj=%.3f", event.ticker, spread, adj)

        log_agent("macro", "%s VIX=%.2f score=%.3f", event.ticker, vix, score)
        return PartialSignal(
            agent_name="macro",
            ticker=event.ticker,
            score=score,
            confidence=0.52 if spread is not None else 0.50,
            timestamp=datetime.now(timezone.utc),
            reasoning=reason,
            decay_hours=24.0,
            source_event_ids=eid,
        )
