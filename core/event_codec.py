"""
event_codec.py — MarketEvent <-> dict for queues and JSON.

event_type strings match EventType.value.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from core.models import DataSource, EventType, MarketEvent


def _parse_dt(value: Any) -> datetime:
    if isinstance(value, datetime):
        if value.tzinfo is None:
            return value.replace(tzinfo=timezone.utc)
        return value.astimezone(timezone.utc)
    if isinstance(value, str):
        s = value.replace("Z", "+00:00")
        dt = datetime.fromisoformat(s)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    return datetime.now(timezone.utc)


def market_event_to_dict(event: MarketEvent) -> dict[str, Any]:
    """Small dict for queues (drops raw blob)."""
    et = event.event_type.value if isinstance(event.event_type, EventType) else str(event.event_type)
    src = event.source.value if isinstance(event.source, DataSource) else str(event.source)
    return {
        "event_id": event.event_id,
        "event_type": et,
        "source": src,
        "ticker": event.ticker.upper(),
        "timestamp": event.timestamp.astimezone(timezone.utc).isoformat(),
        "ingested_at": _parse_dt(event.ingested_at).isoformat(),
        "payload": event.payload,
        "confidence": float(event.confidence),
        "tags": list(event.tags),
    }


def dict_to_market_event(data: dict[str, Any]) -> MarketEvent:
    """Build MarketEvent from queue/test dict."""
    et_raw = data.get("event_type", "")
    try:
        event_type = EventType(et_raw) if isinstance(et_raw, str) else et_raw
    except ValueError:
        event_type = EventType.NEWS_ARTICLE

    src_raw = data.get("source", "")
    try:
        source = DataSource(src_raw) if isinstance(src_raw, str) else src_raw
    except ValueError:
        source = DataSource.REUTERS_RSS

    return MarketEvent(
        event_id=str(data.get("event_id", "")),
        event_type=event_type,
        source=source,
        ticker=str(data.get("ticker", "UNKNOWN")).upper(),
        timestamp=_parse_dt(data.get("timestamp")),
        ingested_at=_parse_dt(data.get("ingested_at")),
        payload=dict(data.get("payload") or {}),
        raw=None,
        confidence=float(data.get("confidence", 1.0)),
        tags=list(data.get("tags") or []),
    )
