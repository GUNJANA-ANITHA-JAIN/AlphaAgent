"""
base_collector.py — Shared collector base: fetch, normalize, dedupe.

Subclass and implement fetch() + normalize(); collect() wires the loop.
"""

import hashlib
import logging
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Generator

from core.models import MarketEvent

logger = logging.getLogger(__name__)


class DedupStore:
    """
    In-memory dedup keys with TTL. Prod would use Redis with the same key idea.

    Key hashes source + ticker + time + payload snippet (not only event_id),
    so the same story from two feeds can still dedupe once.
    """

    def __init__(self, ttl_seconds: int = 86400):  # default 24h
        self._store: dict[str, float] = {}
        self.ttl = ttl_seconds

    def _evict(self):
        now = datetime.utcnow().timestamp()
        self._store = {k: v for k, v in self._store.items() if now - v < self.ttl}

    def is_duplicate(self, key: str) -> bool:
        self._evict()
        return key in self._store

    def mark_seen(self, key: str):
        self._store[key] = datetime.utcnow().timestamp()

    @staticmethod
    def make_key(source: str, ticker: str, timestamp: datetime, payload_snippet: str) -> str:
        raw = f"{source}:{ticker}:{timestamp.isoformat()}:{payload_snippet[:120]}"
        return hashlib.sha256(raw.encode()).hexdigest()[:16]


class BaseCollector(ABC):
    """fetch raw rows per ticker; normalize each to MarketEvent or None."""

    def __init__(self, dedup_store: DedupStore, tickers: list[str]):
        self.dedup = dedup_store
        self.tickers = [t.upper() for t in tickers]
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def fetch(self, ticker: str) -> list[dict]:
        """Return raw dict rows for one ticker. Raise SourceUnavailableError if the API fails."""
        ...

    @abstractmethod
    def normalize(self, raw: dict, ticker: str) -> MarketEvent | None:
        """Turn one raw dict into a MarketEvent, or None to skip. Prefer log over raise."""
        ...

    def collect(self) -> Generator[MarketEvent, None, None]:
        """fetch → normalize → dedupe → yield events."""
        for ticker in self.tickers:
            try:
                raw_items = self.fetch(ticker)
            except Exception as e:
                self.logger.error(f"[{ticker}] fetch failed: {e}")
                continue

            for raw in raw_items:
                try:
                    event = self.normalize(raw, ticker)
                    if event is None:
                        continue

                    # skip duplicates
                    dedup_key = DedupStore.make_key(
                        source=event.source.value,
                        ticker=ticker,
                        timestamp=event.timestamp,
                        payload_snippet=str(event.payload)
                    )
                    if self.dedup.is_duplicate(dedup_key):
                        self.logger.debug(f"[{ticker}] duplicate dropped: {dedup_key}")
                        continue

                    self.dedup.mark_seen(dedup_key)
                    yield event

                except Exception as e:
                    self.logger.warning(f"[{ticker}] normalize failed: {e} | raw={raw}")
                    continue


class SourceUnavailableError(Exception):
    """Upstream API down or throttled."""
    pass
