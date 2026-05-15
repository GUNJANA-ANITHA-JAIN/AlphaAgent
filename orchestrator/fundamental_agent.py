"""
Fundamental agent: simple rules on SEC forms and news text.

Uses only MarketEvent fields (no extra HTTP). Returns soft scores when text is unclear.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Optional

from core.models import EventType, MarketEvent

from .agent_debug import log_agent
from .orchestrator import PartialSignal, SubAgent


_POS_HEADLINE = re.compile(
    r"\b(beats?|topped?|exceed|raised? guidance|strong (?:results|quarter)|"
    r"record (?:revenue|profit)|upgrade|reinstated? buy|surge|soar|"
    r"profit(?:able)?|eps (?:beat|growth)|raises? outlook|bullish|"
    r"partnership|acquisition|buyback|dividend (?:hike|increase))\b",
    re.I,
)
_NEG_HEADLINE = re.compile(
    r"\b(miss|missed|fell short|cut(s|ting)? guidance|weak (?:results|outlook)|"
    r"downgrade|investigation|sec probe|lawsuit|bankruptcy|layoff|"
    r"plunge|tumble|loss|net loss|recall|breach|fraud|delist|"
    r"bearish|cuts? jobs|restructuring|going concern)\b",
    re.I,
)


class FundamentalAgent(SubAgent):
    name = "fundamental"

    async def process(self, event: MarketEvent) -> Optional[PartialSignal]:
        eid = [event.event_id] if event.event_id else []

        if event.event_type == EventType.SEC_FILING:
            return self._from_filing(event, eid)
        if event.event_type in (EventType.NEWS_ARTICLE, EventType.EARNINGS_CALL):
            return self._from_text_news(event, eid)
        return None

    def _from_filing(self, event: MarketEvent, eid: list) -> Optional[PartialSignal]:
        p = event.payload or {}
        form = str(p.get("form_type", "")).upper().strip()
        if not form:
            return None

        log_agent("fundamental", "%s SEC form=%s", event.ticker, form or "?")

        if form == "8-K":
            return PartialSignal(
                agent_name="fundamental",
                ticker=event.ticker,
                score=0.12,
                confidence=0.48,
                timestamp=datetime.now(timezone.utc),
                reasoning="8-K: material corporate event (cautious positive prior)",
                decay_hours=48.0,
                source_event_ids=eid,
            )
        if form in ("10-K", "10-Q"):
            return PartialSignal(
                agent_name="fundamental",
                ticker=event.ticker,
                score=0.04,
                confidence=0.35,
                timestamp=datetime.now(timezone.utc),
                reasoning=f"{form}: periodic disclosure (low directional edge)",
                decay_hours=120.0,
                source_event_ids=eid,
            )
        if form == "4":
            return self._from_form4(event, eid, p)
        return PartialSignal(
            agent_name="fundamental",
            ticker=event.ticker,
            score=0.0,
            confidence=0.26,
            timestamp=datetime.now(timezone.utc),
            reasoning=f"SEC form {form}: no built-in prior (neutral)",
            decay_hours=48.0,
            source_event_ids=eid,
        )

    def _from_form4(self, event: MarketEvent, eid: list, p: dict) -> PartialSignal:
        """Direction from acquired_disposed / is_purchase / transaction_code when present."""
        ip = p.get("is_purchase")
        ad_raw = (p.get("acquired_disposed") or "").strip() or None
        ad_upper = ad_raw.upper() if ad_raw else None
        tc = (p.get("transaction_code") or "").strip().upper() or None
        codes = p.get("transaction_codes") or []
        log_agent(
            "fundamental",
            "%s Form4 is_purchase=%s acquired_disposed=%s tx=%s",
            event.ticker,
            ip,
            ad_raw,
            tc or codes,
        )

        if ip is True:
            return PartialSignal(
                agent_name="fundamental",
                ticker=event.ticker,
                score=0.24,
                confidence=0.52,
                timestamp=datetime.now(timezone.utc),
                reasoning=(
                    f"Form 4: insider acquisition tilt (acquired_disposed={ad_raw or 'A'}, "
                    f"transaction_code={tc or '—'})"
                ),
                decay_hours=72.0,
                source_event_ids=eid,
            )
        if ip is False:
            return PartialSignal(
                agent_name="fundamental",
                ticker=event.ticker,
                score=-0.18,
                confidence=0.46,
                timestamp=datetime.now(timezone.utc),
                reasoning=(
                    f"Form 4: insider disposition tilt (acquired_disposed={ad_raw or 'D'}, "
                    f"transaction_code={tc or '—'})"
                ),
                decay_hours=72.0,
                source_event_ids=eid,
            )
        if ad_upper == "MIXED":
            return PartialSignal(
                agent_name="fundamental",
                ticker=event.ticker,
                score=0.0,
                confidence=0.34,
                timestamp=datetime.now(timezone.utc),
                reasoning="Form 4: mixed buy and sell lines in filing (neutral)",
                decay_hours=72.0,
                source_event_ids=eid,
            )
        detail = f"tx={tc or '—'} codes={codes[:5]!s}" if codes else (f"tx={tc}" if tc else "no parsed side")
        return PartialSignal(
            agent_name="fundamental",
            ticker=event.ticker,
            score=0.0,
            confidence=0.30,
            timestamp=datetime.now(timezone.utc),
            reasoning=f"Form 4 insider activity ({detail}; no clear A/D — neutral)",
            decay_hours=72.0,
            source_event_ids=eid,
        )

    def _from_text_news(self, event: MarketEvent, eid: list) -> Optional[PartialSignal]:
        p = event.payload or {}
        text = f"{p.get('headline', '')} {p.get('body', '')}".strip()
        if len(text) < 8:
            log_agent("fundamental", "%s news text too short", event.ticker)
            return None

        pos = bool(_POS_HEADLINE.search(text))
        neg = bool(_NEG_HEADLINE.search(text))
        log_agent(
            "fundamental",
            "%s news len=%s pos=%s neg=%s",
            event.ticker,
            len(text),
            pos,
            neg,
        )
        if pos == neg:
            return PartialSignal(
                agent_name="fundamental",
                ticker=event.ticker,
                score=0.0,
                confidence=0.28,
                timestamp=datetime.now(timezone.utc),
                reasoning="Fundamental: no clear keyword tilt vs conflict (neutral)",
                decay_hours=12.0,
                source_event_ids=eid,
            )

        if pos:
            return PartialSignal(
                agent_name="fundamental",
                ticker=event.ticker,
                score=0.42,
                confidence=0.52,
                timestamp=datetime.now(timezone.utc),
                reasoning="Headline patterns suggest positive fundamental tone",
                decay_hours=24.0,
                source_event_ids=eid,
            )
        return PartialSignal(
            agent_name="fundamental",
            ticker=event.ticker,
            score=-0.42,
            confidence=0.52,
            timestamp=datetime.now(timezone.utc),
            reasoning="Headline patterns suggest negative fundamental tone",
            decay_hours=24.0,
            source_event_ids=eid,
        )
