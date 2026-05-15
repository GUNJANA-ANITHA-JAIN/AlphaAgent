"""Macro stub with no network — neutral backdrop (not used in price_walk CS path)."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

from core.models import EventType, MarketEvent
from orchestrator.orchestrator import PartialSignal, SubAgent


class StaticMacroAgent(SubAgent):
    """Fixed neutral macro so replay never calls yfinance/FRED."""

    name = "macro"

    async def process(self, event: MarketEvent) -> Optional[PartialSignal]:
        if event.event_type != EventType.PRICE_UPDATE:
            return None
        eid = [event.event_id] if event.event_id else []
        return PartialSignal(
            agent_name="macro",
            ticker=event.ticker,
            score=0.0,
            confidence=0.25,
            timestamp=datetime.now(timezone.utc),
            reasoning="Backtest: static macro (no live VIX)",
            decay_hours=24.0,
            source_event_ids=eid,
        )
