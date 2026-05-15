"""
Technical agent: reads price_update only (no extra HTTP).

Uses RSI, trend vs MA, and momentum. Regime (up / down / sideways) changes how
we mix signals. For panel backtests see orchestrator/cs_technical.py (price_walk
uses it when ALPHAGENT_BACKTEST_CS_PANEL=1).

Env knobs (short list): ALPHAGENT_TECH_ALPHA_ENGINE (1=smooth factors, 0=rule set),
ALPHAGENT_TECH_ZSCORE, ALPHAGENT_TECH_REGIME_SWITCH, ALPHAGENT_TECH_IC_BLEND (off by default).
"""

from __future__ import annotations

import asyncio
import math
import os
from collections import deque
from datetime import datetime, timezone
from typing import Optional

from core.models import EventType, MarketEvent

from .agent_debug import log_agent
from .orchestrator import PartialSignal, SubAgent


def _wilder_rsi_for_period(closes: list[float], period: int) -> float | None:
    if len(closes) < period + 1:
        return None
    deltas = [closes[i] - closes[i - 1] for i in range(1, len(closes))]
    gains = [max(d, 0.0) for d in deltas]
    losses = [max(-d, 0.0) for d in deltas]
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    for i in range(period, len(gains)):
        avg_gain = (avg_gain * (period - 1) + gains[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i]) / period
    if avg_loss < 1e-12:
        return 100.0
    rs = avg_gain / avg_loss
    return 100.0 - (100.0 / (1.0 + rs))


def _wilder_rsi(closes: list[float], max_period: int = 14) -> tuple[float | None, int]:
    """RSI (Wilder); use biggest period that still fits data."""
    n = len(closes)
    if n < 3:
        return None, 0
    upper = min(max_period, n - 1)
    upper = max(2, upper)
    for period in range(upper, 1, -1):
        rsi = _wilder_rsi_for_period(closes, period)
        if rsi is not None:
            return rsi, period
    return None, 0


def _rsi_to_score(rsi: float) -> float:
    """Map RSI to score when regime filter is off (old style)."""
    if rsi <= 30.0:
        return min(0.35 + (30.0 - rsi) / 30.0 * 0.55, 1.0)
    if rsi >= 70.0:
        return max(-0.35 - (rsi - 70.0) / 30.0 * 0.55, -1.0)
    return (50.0 - rsi) / 50.0 * 0.35


def _trend_ma(closes: list[float], max_period: int, min_bars: int) -> tuple[float | None, int]:
    """Simple moving average; None if not enough bars."""
    n = len(closes)
    if n < min_bars:
        return None, 0
    use = min(max_period, n)
    window = closes[-use:]
    return sum(window) / float(use), use


def _classify_regime(close: float, ma: float, band_frac: float) -> str:
    """Return uptrend, downtrend, or sideways from price vs MA."""
    if ma <= 1e-12:
        return "sideways"
    rel = (close - ma) / ma
    if abs(rel) < band_frac:
        return "sideways"
    return "uptrend" if rel > 0 else "downtrend"


def _vol_rising(closes: list[float]) -> bool:
    """True if last move is big vs recent median (simple vol spike)."""
    if len(closes) < 12:
        return False
    moves = [abs(closes[i] - closes[i - 1]) for i in range(-10, 0)]
    if not moves:
        return False
    recent = abs(closes[-1] - closes[-2])
    med = sorted(moves)[len(moves) // 2]
    return recent > max(med * 1.22, 1e-9)


def _uptrend_exhaust_rsi() -> float:
    return float(os.environ.get("ALPHAGENT_TECH_UPTREND_EXHAUST_RSI", "76"))


def _uptrend_soft_sell_rsi() -> float:
    """RSI floor for “soft” sell in an uptrend."""
    return float(os.environ.get("ALPHAGENT_TECH_UPTREND_SOFT_SELL_RSI", "68"))


def _uptrend_soft_sell_mom() -> float:
    """Momentum must be below this for soft sell (default -0.02)."""
    return float(os.environ.get("ALPHAGENT_TECH_UPTREND_SOFT_SELL_MOM", "-0.02"))


def _uptrend_sell_require_vol() -> bool:
    return os.environ.get("ALPHAGENT_TECH_UPTREND_SELL_REQUIRE_VOL", "0").strip().lower() in (
        "1",
        "true",
        "yes",
        "on",
    )


def _uptrend_hold_tilt_enabled() -> bool:
    """Allow a small bear tilt on stretched RSI so score is not always 0."""
    return os.environ.get("ALPHAGENT_TECH_UPTREND_HOLD_TILT", "1").strip().lower() not in (
        "0",
        "false",
        "no",
        "off",
    )


def _uptrend_hold_de_risk_tilt(rsi: float, mom: float) -> float:
    if not _uptrend_hold_tilt_enabled():
        return 0.0
    if rsi < 62.0:
        return 0.0
    t = -0.038 * min(1.0, (rsi - 62.0) / 22.0)
    if mom < 0.0:
        t *= 1.4
    return max(-0.14, min(0.0, t))


def _uptrend_stretch_rsi_lone() -> float:
    """High RSI alone can trigger stretch sell in uptrend."""
    return float(os.environ.get("ALPHAGENT_TECH_UPTREND_STRETCH_RSI_LONE", "70"))


def _regime_rsi_decision(
    regime: str, rsi: float, mom: float, closes: list[float]
) -> tuple[str, str]:
    """Pick BUY/SELL/HOLD from RSI + mom rules for this regime."""
    if regime == "uptrend":
        if rsi < 40.0:
            return "BUY", "uptrend+dip(RSI<40)"
        thr = _uptrend_exhaust_rsi()
        soft_thr = _uptrend_soft_sell_rsi()
        soft_mom = _uptrend_soft_sell_mom()
        lone = _uptrend_stretch_rsi_lone()
        if rsi > thr and mom < 0.0:
            if _uptrend_sell_require_vol():
                if _vol_rising(closes):
                    return "SELL", f"uptrend+exhaustion(RSI>{thr:g}+mom-+vol)"
                return "HOLD", "uptrend+exhaustion_partial(no_vol_confirm)"
            return "SELL", f"uptrend+exhaustion(RSI>{thr:g}+mom-)"
        if rsi >= soft_thr and (mom < soft_mom or rsi >= lone):
            return "SELL", f"uptrend+stretch(RSI≥{soft_thr:g} & (mom<{soft_mom:g} or RSI≥{lone:g}))"
        return "HOLD", "uptrend+no_edge"
    if regime == "downtrend":
        if rsi > 60.0:
            return "SELL", "downtrend+rally(RSI>60)"
        return "HOLD", "downtrend+ignore_oversold_bounce"
    if rsi > 70.0:
        return "SELL", "range+RSI>70"
    if rsi < 30.0:
        return "BUY", "range+RSI<30"
    return "HOLD", "range+RSI_mid"


def _score_from_regime_decision(decision: str, regime: str, rsi: float) -> float:
    """Turn BUY/SELL/HOLD + regime into a -1..+1 score."""
    if decision == "HOLD":
        return 0.0
    if decision == "BUY":
        if regime == "uptrend":
            return min(0.95, 0.36 + max(0.0, (40.0 - rsi) / 40.0) * 0.52)
        return min(0.95, 0.34 + max(0.0, (30.0 - rsi) / 30.0) * 0.58)
    if decision == "SELL":
        if regime == "uptrend":
            thr = _uptrend_exhaust_rsi()
            soft_thr = _uptrend_soft_sell_rsi()
            # stretch tier after exhaustion check
            if rsi >= thr:
                return max(
                    -0.95,
                    -0.40 - max(0.0, (rsi - thr) / max(101.0 - thr, 1e-6)) * 0.48,
                )
            return max(
                -0.55,
                -0.22 - max(0.0, (rsi - soft_thr) / max(thr - soft_thr, 1e-6)) * 0.28,
            )
        if regime == "downtrend":
            return max(-0.95, -0.36 - max(0.0, (rsi - 60.0) / 40.0) * 0.52)
        return max(-0.95, -0.34 - max(0.0, (rsi - 70.0) / 30.0) * 0.58)
    return 0.0


def _alpha_engine_enabled() -> bool:
    """True = smooth factor blend (default). False = older rule ladder."""
    v = os.environ.get("ALPHAGENT_TECH_ALPHA_ENGINE", "1").strip().lower()
    return v not in ("0", "false", "no", "off")


def _alpha_features(close: float, ma: float, rsi: float, closes: list[float]) -> tuple[float, float, float]:
    """Three ~[-1,1] inputs: trend vs MA, RSI (high = bearish), short momentum."""
    dist = (close - ma) / max(ma, 1e-9)
    scale_t = float(os.environ.get("ALPHAGENT_TECH_ALPHA_TREND_SCALE", "0.095"))
    trend_n = max(-1.0, min(1.0, dist / max(scale_t, 1e-6)))

    scale_r = float(os.environ.get("ALPHAGENT_TECH_ALPHA_RSI_SCALE", "26.0"))
    rsi_n = max(-1.0, min(1.0, (50.0 - rsi) / max(scale_r, 1e-6)))

    mom_n = 0.0
    if len(closes) >= 6:
        pr = close / max(closes[-6], 1e-9) - 1.0
        gain = float(os.environ.get("ALPHAGENT_TECH_ALPHA_MOM_GAIN", "14.0"))
        mom_n = max(-1.0, min(1.0, pr * gain))
    return trend_n, rsi_n, mom_n


def _tech_zscore_enabled() -> bool:
    return os.environ.get("ALPHAGENT_TECH_ZSCORE", "1").strip().lower() not in (
        "0",
        "false",
        "no",
        "off",
    )


def _tech_z_window() -> int:
    return max(20, int(os.environ.get("ALPHAGENT_TECH_Z_WINDOW", "105")))


def _tech_orth_enabled() -> bool:
    return os.environ.get("ALPHAGENT_TECH_ORTHOGONALIZE", "1").strip().lower() not in (
        "0",
        "false",
        "no",
        "off",
    )


def _tech_ic_blend_enabled() -> bool:
    # Off by default — IC tilt can wobble on long multi-ticker runs.
    return os.environ.get("ALPHAGENT_TECH_IC_BLEND", "0").strip().lower() in (
        "1",
        "true",
        "yes",
        "on",
    )


def _tech_ic_horizon() -> int:
    return max(1, int(os.environ.get("ALPHAGENT_TECH_IC_HORIZON", "3")))


def _tech_ic_min_samples() -> int:
    return max(15, int(os.environ.get("ALPHAGENT_TECH_IC_MIN_SAMPLES", "55")))


def _tech_ic_max_history() -> int:
    return max(60, int(os.environ.get("ALPHAGENT_TECH_IC_MAX_HISTORY", "252")))


def _tech_ic_blend_lambda() -> float:
    return max(0.0, min(1.0, float(os.environ.get("ALPHAGENT_TECH_IC_BLEND_LAMBDA", "0.20"))))


def _zscore_last_component(rows: list[tuple[float, float, float]], dim: int) -> float:
    """Z-score of the last row feature vs the window (dim 0=trend, 1=rsi, 2=mom)."""
    if len(rows) < 5:
        return 0.0
    xs = [r[dim] for r in rows]
    x = xs[-1]
    mu = sum(xs) / len(xs)
    var = sum((v - mu) ** 2 for v in xs) / max(1, len(xs) - 1)
    sd = math.sqrt(var)
    if sd < 1e-9:
        return 0.0
    return max(-4.0, min(4.0, (x - mu) / sd))


def _orthogonalize_m_z_on_t(zt_hist: list[float], zm_hist: list[float]) -> float:
    """Momentum z with trend z regressed out (uses past points only)."""
    if len(zt_hist) < 6 or len(zm_hist) != len(zt_hist):
        return zm_hist[-1]
    zt_p, zm_p = zt_hist[:-1], zm_hist[:-1]
    n = len(zt_p)
    mt = sum(zt_p) / n
    mm = sum(zm_p) / n
    vt = sum((a - mt) ** 2 for a in zt_p)
    if vt < 1e-12:
        return zm_hist[-1]
    cov = sum((zt_p[i] - mt) * (zm_p[i] - mm) for i in range(n))
    beta = cov / vt
    return zm_hist[-1] - beta * zt_hist[-1]


def _pearson_corr(xs: list[float], ys: list[float]) -> float:
    n = len(xs)
    if n < 8 or n != len(ys):
        return 0.0
    mx = sum(xs) / n
    my = sum(ys) / n
    vx = sum((x - mx) ** 2 for x in xs)
    vy = sum((y - my) ** 2 for y in ys)
    if vx < 1e-18 or vy < 1e-18:
        return 0.0
    cov = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    return max(-1.0, min(1.0, cov / math.sqrt(vx * vy)))


def _ic_factor_weights(rows: list[tuple[float, float, float, float]]) -> tuple[float, float, float]:
    """Weights for trend/RSI/mom from rolling IC vs forward return; rows add fwd_ret."""
    if len(rows) < 8:
        return (1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0)
    zt = [r[0] for r in rows]
    zr = [r[1] for r in rows]
    zm = [r[2] for r in rows]
    y = [r[3] for r in rows]
    ic_t = _pearson_corr(zt, y)
    ic_r = _pearson_corr(zr, y)
    ic_m = _pearson_corr(zm, y)
    thr = float(os.environ.get("ALPHAGENT_TECH_IC_SHRINK_ABS", "0.0"))
    if thr > 0.0:
        ic_t = 0.0 if abs(ic_t) < thr else ic_t
        ic_r = 0.0 if abs(ic_r) < thr else ic_r
        ic_m = 0.0 if abs(ic_m) < thr else ic_m
    tilt = max(0.0, min(1.0, float(os.environ.get("ALPHAGENT_TECH_IC_TILT", "0.32"))))
    prior = 1.0 / 3.0
    raw = [
        prior + tilt * ic_t,
        prior + tilt * ic_r,
        prior + tilt * ic_m,
    ]
    s = abs(raw[0]) + abs(raw[1]) + abs(raw[2])
    if s < 1e-9:
        return (1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0)
    return (raw[0] / s, raw[1] / s, raw[2] / s)


def _regime_weighted_alpha(
    regime: str,
    rsi: float,
    mom: float,
    closes: list[float],
    close: float,
    ma: float,
    *,
    blend_t: float | None = None,
    blend_r: float | None = None,
    blend_m: float | None = None,
) -> tuple[float, str]:
    """Blend trend/RSI/mom into one -1..+1 score; optional z inputs; note string for logs."""
    t, r, m = _alpha_features(close, ma, rsi, closes)
    bt = t if blend_t is None else blend_t
    br = r if blend_r is None else blend_r
    bm = m if blend_m is None else blend_m
    zpart = ""
    if blend_t is not None:
        zpart = f" | zt={bt:+.2f} zr={br:+.2f} zm={bm:+.2f}"
    thr = _uptrend_exhaust_rsi()
    req_vol = _uptrend_sell_require_vol()
    vu = _vol_rising(closes)

    wt, wr, wm, pack = _regime_factor_weights(regime)

    if regime == "uptrend":
        raw = wt * bt + wr * br + wm * bm
        if rsi > thr and m < -0.06:
            ex = 0.18 + max(0.0, rsi - thr) / max(101.0 - thr, 1e-6) * 0.35
            if req_vol and not vu:
                ex *= 0.45
            raw -= ex
        note = f"α t={t:+.2f} r={r:+.2f} m={m:+.2f}{zpart} | w=({wt:.2f},{wr:.2f},{wm:.2f}) {pack}"
        if req_vol:
            note += f" vol={vu}"
        return max(-1.0, min(1.0, raw)), note
    if regime == "downtrend":
        raw = wt * bt + wr * br + wm * bm
        return (
            max(-1.0, min(1.0, raw)),
            f"α t={t:+.2f} r={r:+.2f} m={m:+.2f}{zpart} | w=({wt:.2f},{wr:.2f},{wm:.2f}) {pack}",
        )
    raw = wt * bt + wr * br + wm * bm
    return (
        max(-1.0, min(1.0, raw)),
        f"α t={t:+.2f} r={r:+.2f} m={m:+.2f}{zpart} | w=({wt:.2f},{wr:.2f},{wm:.2f}) {pack}",
    )


def _regime_filter_enabled() -> bool:
    v = os.environ.get("ALPHAGENT_TECH_REGIME_FILTER", "1").strip().lower()
    return v not in ("0", "false", "no", "off")


def _regime_switch_enabled() -> bool:
    """True = shift weights by regime (trending vs range)."""
    v = os.environ.get("ALPHAGENT_TECH_REGIME_SWITCH", "1").strip().lower()
    return v not in ("0", "false", "no", "off")


def _regime_factor_weights(regime: str) -> tuple[float, float, float, str]:
    """(trend, rsi, mom) weights that sum to 1, plus a short label."""
    if not _regime_switch_enabled():
        if regime == "uptrend":
            return 0.50, 0.18, 0.32, "legacy_up"
        if regime == "downtrend":
            return 0.46, 0.32, 0.22, "legacy_dn"
        return 0.38, 0.34, 0.28, "legacy_rng"

    if regime == "uptrend":
        return 0.42, 0.14, 0.44, "trend_pack"
    if regime == "downtrend":
        return 0.40, 0.22, 0.38, "trend_pack"
    return 0.22, 0.55, 0.23, "range_pack"


class TechnicalAgent(SubAgent):
    """Turns price_update into a PartialSignal (RSI / trend / mom; see module doc)."""

    name = "technical"

    def __init__(self, maxlen: int | None = None, rsi_period: int = 14):
        self._closes: dict[str, deque[float]] = {}
        # Long enough for ~200-day MA when data exists.
        self._maxlen = int(
            maxlen
            if maxlen is not None
            else os.environ.get("ALPHAGENT_TECH_CLOSE_BUFFER", "260")
        )
        self._rsi_period = rsi_period
        self._ma_period = int(os.environ.get("ALPHAGENT_TECH_MA_PERIOD", "200"))
        self._ma_min_bars = int(os.environ.get("ALPHAGENT_TECH_MA_MIN_BARS", "20"))
        self._regime_band = float(os.environ.get("ALPHAGENT_TECH_REGIME_BAND", "0.004"))
        self._lock = asyncio.Lock()
        # Per-ticker rolling features for z-scores / optional IC.
        self._raw_feat_hist: dict[str, deque[tuple[float, float, float]]] = {}
        self._z_trail: dict[str, deque[tuple[float, float, float]]] = {}
        self._z_feat_hist: dict[str, deque[tuple[float, float, float, float]]] = {}
        self._ic_train: dict[str, deque[tuple[float, float, float, float]]] = {}

    async def process(self, event: MarketEvent) -> Optional[PartialSignal]:
        if event.event_type != EventType.PRICE_UPDATE:
            return None
        p = event.payload or {}
        close = p.get("close")
        if close is None:
            return None
        try:
            c = float(close)
        except (TypeError, ValueError):
            return None

        ticker = event.ticker.upper()
        eid = [event.event_id] if event.event_id else []

        async with self._lock:
            if ticker not in self._closes:
                self._closes[ticker] = deque(maxlen=self._maxlen)
            self._closes[ticker].append(c)
            closes = list(self._closes[ticker])

        rsi, used_period = _wilder_rsi(closes, self._rsi_period)
        if rsi is None:
            n = len(closes)
            log_agent(
                "technical",
                "%s warmup n=%s (need >=3 closes for short RSI)",
                ticker,
                n,
            )
            return PartialSignal(
                agent_name="technical",
                ticker=ticker,
                score=0.0,
                confidence=0.22,
                timestamp=datetime.now(timezone.utc),
                reasoning=f"Warming price buffer ({n}/3+ closes for RSI)",
                decay_hours=2.0,
                source_event_ids=eid,
            )

        mom = 0.0
        if len(closes) >= 6:
            mom = (closes[-1] - closes[-6]) / max(abs(closes[-6]), 1e-9)
            mom = max(-1.0, min(1.0, mom * 8.0))

        if not _regime_filter_enabled():
            score = 0.72 * _rsi_to_score(rsi) + 0.28 * mom
            score = max(-1.0, min(1.0, score))
            conf = min(0.45 + min(len(closes), 30) / 60.0, 0.85)
            if used_period < self._rsi_period:
                conf *= 0.85 + 0.15 * (used_period / self._rsi_period)
            log_agent(
                "technical",
                "%s RSI≈%.1f p=%s score=%.3f (no regime filter)",
                ticker,
                rsi,
                used_period,
                score,
            )
            return PartialSignal(
                agent_name="technical",
                ticker=ticker,
                score=round(score, 4),
                confidence=round(conf, 3),
                timestamp=datetime.now(timezone.utc),
                reasoning=f"RSI≈{rsi:.1f} (p={used_period}), 5-bar mom (legacy blend)",
                decay_hours=4.0,
                source_event_ids=eid,
            )

        ma, ma_used = _trend_ma(closes, self._ma_period, self._ma_min_bars)
        if ma is None:
            return PartialSignal(
                agent_name="technical",
                ticker=ticker,
                score=0.0,
                confidence=0.24,
                timestamp=datetime.now(timezone.utc),
                reasoning=(
                    f"Warming MA trend ({len(closes)}/{self._ma_min_bars}+ closes; "
                    f"RSI≈{rsi:.1f} p={used_period})"
                ),
                decay_hours=2.0,
                source_event_ids=eid,
            )

        regime = _classify_regime(c, ma, self._regime_band)

        if _alpha_engine_enabled():
            t, r, m = _alpha_features(c, ma, rsi, closes)
            zw = _tech_z_window()
            ic_h = _tech_ic_horizon()
            ic_cap = _tech_ic_max_history()

            raw_dq = self._raw_feat_hist.setdefault(ticker, deque(maxlen=zw))
            raw_dq.append((t, r, m))
            rows = list(raw_dq)

            if _tech_zscore_enabled():
                zt = _zscore_last_component(rows, 0)
                zr = _zscore_last_component(rows, 1)
                zm0 = _zscore_last_component(rows, 2)
            else:
                zt, zr, zm0 = t, r, m

            trail = self._z_trail.setdefault(ticker, deque(maxlen=zw))
            zt_prev = [p[0] for p in trail]
            zm_prev = [p[2] for p in trail]
            if _tech_orth_enabled() and _tech_zscore_enabled() and len(trail) >= 5:
                zm2 = _orthogonalize_m_z_on_t(zt_prev + [zt], zm_prev + [zm0])
            else:
                zm2 = zm0
            trail.append((zt, zr, zm2))

            zmax = max(zw + 5, ic_h + 30)
            zhist = self._z_feat_hist.setdefault(ticker, deque(maxlen=zmax))
            zhist.append((zt, zr, zm2, float(c)))
            ic_train = self._ic_train.setdefault(ticker, deque(maxlen=ic_cap))
            if len(zhist) > ic_h:
                old = zhist[-(ic_h + 1)]
                fwd_o = float(c) / max(old[3], 1e-12) - 1.0
                ic_train.append((old[0], old[1], old[2], fwd_o))

            blend_t: float | None = None
            blend_r: float | None = None
            blend_m: float | None = None
            if _tech_zscore_enabled():
                blend_t, blend_r, blend_m = zt, zr, zm2

            reg_score, note = _regime_weighted_alpha(
                regime,
                rsi,
                mom,
                closes,
                c,
                ma,
                blend_t=blend_t,
                blend_r=blend_r,
                blend_m=blend_m,
            )
            score = reg_score
            ic_gain = float(os.environ.get("ALPHAGENT_TECH_IC_GAIN", "0.18"))
            if _tech_ic_blend_enabled() and len(ic_train) >= _tech_ic_min_samples():
                lam = _tech_ic_blend_lambda()
                w_ic = _ic_factor_weights(list(ic_train))
                ic_dot = w_ic[0] * zt + w_ic[1] * zr + w_ic[2] * zm2
                ic_scalar = max(-1.0, min(1.0, ic_dot * ic_gain))
                score = max(-1.0, min(1.0, (1.0 - lam) * reg_score + lam * ic_scalar))
                note += (
                    f" | ICw=({w_ic[0]:+.2f},{w_ic[1]:+.2f},{w_ic[2]:+.2f})"
                    f" ic={ic_scalar:+.3f} n={len(ic_train)} λ={lam:.2f}"
                )

            conf = min(0.82, max(0.38, 0.33 + min(abs(score) * 0.90, 0.46)))
            if used_period < self._rsi_period:
                conf *= 0.88 + 0.12 * (used_period / self._rsi_period)
            if ma_used < self._ma_period:
                conf *= 0.82 + 0.18 * (ma_used / self._ma_period)
            reasoning = (
                f"{regime} MA{ma_used}={ma:.2f} vs close={c:.2f}; RSI≈{rsi:.1f} (p={used_period}) | "
                f"{note} → score={score:+.3f}"
            )
            log_agent("technical", "%s ALPHA_ENGINE score=%.3f", ticker, score)
        else:
            decision, rule = _regime_rsi_decision(regime, rsi, mom, closes)
            score = _score_from_regime_decision(decision, regime, rsi)
            if decision == "HOLD" and regime == "uptrend":
                score = max(-1.0, min(1.0, score + _uptrend_hold_de_risk_tilt(rsi, mom)))
                if score != 0.0:
                    rule = f"{rule}+rsi_tilt"
            if decision != "HOLD":
                score = max(-1.0, min(1.0, score + 0.14 * mom))

            if decision == "HOLD":
                conf = 0.30 + min(len(closes), 40) / 200.0
                if score != 0.0:
                    conf = min(0.52, conf + 0.14)
            else:
                conf = min(0.42 + min(len(closes), 60) / 90.0, 0.82)
                if used_period < self._rsi_period:
                    conf *= 0.88 + 0.12 * (used_period / self._rsi_period)
                if ma_used < self._ma_period:
                    conf *= 0.82 + 0.18 * (ma_used / self._ma_period)

            reasoning = (
                f"{regime} MA{ma_used}={ma:.2f} vs close={c:.2f}; RSI≈{rsi:.1f} (p={used_period}) "
                f"→ {decision} [{rule}]"
            )

            log_agent(
                "technical",
                "%s regime=%s decision=%s RSI=%.1f score=%.3f",
                ticker,
                regime,
                decision,
                rsi,
                score,
            )

        return PartialSignal(
            agent_name="technical",
            ticker=ticker,
            score=round(score, 4),
            confidence=round(conf, 3),
            timestamp=datetime.now(timezone.utc),
            reasoning=reasoning,
            decay_hours=4.0,
            source_event_ids=eid,
        )
