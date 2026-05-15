"""
Short orchestrator demo: python -m orchestrator from repo root.

Using -m avoids double-loading orchestrator as __main__ and as a package.
"""

from __future__ import annotations

import asyncio
import logging
import os
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
try:
    from dotenv import load_dotenv

    load_dotenv(_ROOT / ".env")
except ImportError:
    pass
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from orchestrator.fundamental_agent import FundamentalAgent
from orchestrator.macro_agent import MacroAgent
from orchestrator.orchestrator import Orchestrator, logger, print_signal
from orchestrator.sentiment_agent import FinBERTSentimentAgent, HeuristicSentimentAgent
from orchestrator.technical_agent import TechnicalAgent


async def _demo() -> None:
    orch = Orchestrator()

    if os.environ.get("ALPHAGENT_USE_FINBERT", "0").strip().lower() not in (
        "0",
        "false",
        "no",
        "off",
    ):
        orch.register_agent("sentiment", FinBERTSentimentAgent(eager_load=True))
    else:
        orch.register_agent("sentiment", HeuristicSentimentAgent())

    orch.register_agent("technical", TechnicalAgent())
    orch.register_agent("fundamental", FundamentalAgent())
    orch.register_agent("macro", MacroAgent())
    orch.on_signal(print_signal)

    run_task = asyncio.create_task(orch.run())
    await asyncio.sleep(0.1)

    now = datetime.now(timezone.utc).isoformat()
    test_events = [
        {
            "event_id": str(uuid.uuid4()),
            "event_type": "news_article",
            "source": "reuters_rss",
            "ticker": "AAPL",
            "timestamp": now,
            "ingested_at": now,
            "payload": {"headline": "Apple beats Q3 earnings by 12%"},
            "confidence": 1.0,
            "tags": [],
        },
        {
            "event_id": str(uuid.uuid4()),
            "event_type": "price_update",
            "source": "yfinance",
            "ticker": "NVDA",
            "timestamp": now,
            "ingested_at": now,
            "payload": {"close": 875.50, "volume": 42_000_000},
            "confidence": 1.0,
            "tags": [],
        },
        {
            "event_id": str(uuid.uuid4()),
            "event_type": "sec_filing",
            "source": "edgar",
            "ticker": "TSLA",
            "timestamp": now,
            "ingested_at": now,
            "payload": {"form_type": "8-K", "filed_date": "2025-05-06"},
            "confidence": 1.0,
            "tags": [],
        },
    ]

    for event in test_events:
        orch.push_event(event)
        logger.info("Pushed event: %s / %s", event["ticker"], event["event_type"])

    await asyncio.sleep(10)
    orch.stop()
    try:
        await asyncio.wait_for(run_task, timeout=45.0)
    except asyncio.TimeoutError:
        logger.warning("Orchestrator did not finish after stop(); cancelling.")
        run_task.cancel()
        try:
            await run_task
        except asyncio.CancelledError:
            pass

    print(f"\nTotal signals emitted: {len(orch.signal_history())}")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
    )
    asyncio.run(_demo())
