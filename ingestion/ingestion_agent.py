"""
ingestion_agent.py — Runs collectors on timers and fans out MarketEvents.

For prod, swap the in-process bus for Kafka or similar.
"""

import sys
from pathlib import Path

# Repo root on path when you run this file from ingestion/
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

import asyncio
import logging
import time
from collections import deque
from datetime import datetime
from typing import Any, Callable, Optional

from core.models import EventType, MarketEvent
from ingestion.base_collector import DedupStore
from ingestion.collectors import PriceCollector, NewsCollector, EdgarCollector, StockTwitsCollector

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("IngestionAgent")


class EventBus:
    """In-process pub/sub: subscribe(EventType, handler); emit(event) calls handlers."""

    def __init__(self):
        self._handlers: dict[EventType, list[Callable]] = {}
        self._history: deque = deque(maxlen=10_000)  # last events for debug

    def subscribe(self, event_type: EventType, handler: Callable[[MarketEvent], None]):
        self._handlers.setdefault(event_type, []).append(handler)
        logger.info(f"Subscribed {handler.__name__} → {event_type.value}")

    def emit(self, event: MarketEvent):
        self._history.append(event)
        handlers = self._handlers.get(event.event_type, [])
        for handler in handlers:
            try:
                handler(event)
            except Exception as e:
                logger.error(f"Handler {handler.__name__} failed on {event.event_id}: {e}")

    def recent_events(self, n: int = 50) -> list[MarketEvent]:
        return list(self._history)[-n:]


class IngestionAgent:
    """
    Owns collectors + bus. Default poll seconds: price 60, news 30, edgar 300, stocktwits 120.

    Slow collectors should move to threads/processes with timeouts so one API cannot block all.
    """

    def __init__(
        self,
        tickers: list[str],
        event_bus: EventBus,
        config: dict = None,
        orchestrator: Optional[Any] = None,
    ):
        self.tickers = tickers
        self.bus = event_bus
        self.config = config or {}
        self.dedup = DedupStore(ttl_seconds=86400)
        self._running = False
        self._stats = {
            "total_emitted": 0,
            "duplicates_dropped": 0,
            "errors": 0,
            "by_source": {},
        }

        # collectors: name -> (instance, seconds between runs)
        self.collectors = {
            "price":      (PriceCollector(self.dedup, tickers), 60),
            "news":       (NewsCollector(self.dedup, tickers),  30),
            "edgar":      (EdgarCollector(self.dedup, tickers), 300),
            "stocktwits": (StockTwitsCollector(self.dedup, tickers), 120),
        }

        if orchestrator is not None:
            from core.event_codec import market_event_to_dict

            def _forward_to_orch(evt: MarketEvent) -> None:
                orchestrator.push_event(market_event_to_dict(evt))

            for et in (
                EventType.PRICE_UPDATE,
                EventType.NEWS_ARTICLE,
                EventType.SEC_FILING,
                EventType.SOCIAL_POST,
                EventType.EARNINGS_CALL,
            ):
                self.bus.subscribe(et, _forward_to_orch)
            logger.info("IngestionAgent wired to orchestrator queue (all EventTypes).")

    def _run_collector(self, name: str):
        """One pass: collect events and emit each."""
        collector, _ = self.collectors[name]
        count = 0
        for event in collector.collect():
            self.bus.emit(event)
            count += 1
            self._stats["total_emitted"] += 1
            self._stats["by_source"][event.source.value] = \
                self._stats["by_source"].get(event.source.value, 0) + 1

        if count > 0:
            logger.info(f"[{name}] emitted {count} events")

    async def _collector_loop(self, name: str, interval_seconds: int):
        """Sleep interval_seconds between collector runs."""
        logger.info(f"Starting {name} collector (interval={interval_seconds}s)")
        while self._running:
            try:
                # run blocking fetch in a thread
                await asyncio.to_thread(self._run_collector, name)
            except Exception as e:
                logger.error(f"[{name}] collector loop error: {e}")
                self._stats["errors"] += 1
            await asyncio.sleep(interval_seconds)

    async def run(self):
        """Start all collector loops concurrently."""
        self._running = True
        logger.info(f"Ingestion agent starting. Tickers: {self.tickers}")

        tasks = [
            self._collector_loop(name, interval)
            for name, (_, interval) in self.collectors.items()
        ]
        # stats every 60s
        tasks.append(self._stats_loop())

        await asyncio.gather(*tasks)

    async def _stats_loop(self):
        while self._running:
            await asyncio.sleep(60)
            logger.info(
                f"Stats — emitted: {self._stats['total_emitted']} | "
                f"errors: {self._stats['errors']} | "
                f"by_source: {self._stats['by_source']}"
            )

    def stop(self):
        self._running = False
        logger.info("Ingestion agent stopped.")


# --- tiny demo handlers ---

def example_price_handler(event: MarketEvent):
    """Demo only."""
    p = event.payload
    logger.info(
        f"PRICE | {event.ticker} | close={p['close']:.2f} | "
        f"vol={p['volume']:,} | {event.timestamp.date()}"
    )

def example_news_handler(event: MarketEvent):
    logger.info(f"NEWS  | {event.ticker} | {event.payload['headline'][:80]}")

def example_filing_handler(event: MarketEvent):
    logger.info(
        f"FILING| {event.ticker} | {event.payload['form_type']} "
        f"filed {event.payload['filed_date']}"
    )

def example_social_handler(event: MarketEvent):
    p = event.payload
    logger.info(
        f"STOCKTWITS| {event.ticker} | score={p['score']} | "
        f"{p['text'][:60]}..."
    )


async def main():
    # liquid large-cap names for demo
    TICKERS = [
        "AAPL", "MSFT", "GOOGL", "AMZN", "META",
        "NVDA", "TSLA", "JPM", "JNJ", "V",
        "UNH", "XOM", "PG", "MA", "HD",
        "CVX", "MRK", "ABBV", "PEP", "COST",
    ]

    bus = EventBus()

    # demo wiring only
    bus.subscribe(EventType.PRICE_UPDATE,  example_price_handler)
    bus.subscribe(EventType.NEWS_ARTICLE,  example_news_handler)
    bus.subscribe(EventType.SEC_FILING,    example_filing_handler)
    bus.subscribe(EventType.SOCIAL_POST,   example_social_handler)

    config = {}

    agent = IngestionAgent(TICKERS, bus, config)

    try:
        await agent.run()
    except KeyboardInterrupt:
        agent.stop()
        logger.info("Shutdown complete.")


if __name__ == "__main__":
    asyncio.run(main())
