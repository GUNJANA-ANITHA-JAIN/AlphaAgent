"""
Full pipeline: collectors -> bus -> orchestrator -> fused signals.

From repo root: python run_pipeline.py

FinBERT (default): needs torch + transformers; HF_TOKEN in .env speeds Hub.
Keyword sentiment only: ALPHAGENT_USE_FINBERT=0 python run_pipeline.py
Macro cache seconds: ALPHAGENT_MACRO_CACHE_SEC=900 python run_pipeline.py
Log each event at INFO: ALPHAGENT_LOG_EVENTS=1 python run_pipeline.py

Markdown summary each run: runs/latest_pipeline_run.md (override with ALPHAGENT_RUN_REPORT_PATH).
Disable report: ALPHAGENT_RUN_REPORT=0. Tickers: ALPHAGENT_TICKERS in .env.
"""

from __future__ import annotations

import asyncio
import logging
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent
try:
    from dotenv import load_dotenv

    load_dotenv(_REPO_ROOT / ".env")
except ImportError:
    pass
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from core.models import EventType, MarketEvent
from ingestion.ingestion_agent import EventBus, IngestionAgent
from orchestrator.fundamental_agent import FundamentalAgent
from orchestrator.macro_agent import MacroAgent
from orchestrator.orchestrator import Orchestrator, TradeSignal, format_trade_signal_message
from orchestrator.sentiment_agent import FinBERTSentimentAgent, HeuristicSentimentAgent
from orchestrator.technical_agent import TechnicalAgent

from pipeline_run_report import write_latest_run_report

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("run_pipeline")

# Demo ticker list; override with ALPHAGENT_TICKERS in .env
_DEFAULT_TICKERS = (
    "AAPL,MSFT,GOOGL,AMZN,META,NVDA,TSLA,JPM,V,JNJ,WMT,PG,MA,UNH,HD,DIS,BAC,XOM,CVX,COST"
)


def _print_signal(signal: TradeSignal) -> None:
    logger.info("%s", format_trade_signal_message(signal))


def _env_finbert_enabled() -> bool:
    v = os.environ.get("ALPHAGENT_USE_FINBERT", "1").strip().lower()
    return v not in ("0", "false", "no", "off")


def _env_log_events() -> bool:
    return os.environ.get("ALPHAGENT_LOG_EVENTS", "0").strip().lower() in ("1", "true", "yes", "on")


def _wire_event_logging(bus: EventBus) -> None:
    """If ALPHAGENT_LOG_EVENTS=1, log each MarketEvent."""

    def _log_event(evt: MarketEvent) -> None:
        et = evt.event_type.value if hasattr(evt.event_type, "value") else str(evt.event_type)
        src = evt.source.value if hasattr(evt.source, "value") else str(evt.source)
        logger.info("EVENT %s | %s | %s | id=%s", et, src, evt.ticker, evt.event_id[:8] if evt.event_id else "?")

    for et in (
        EventType.PRICE_UPDATE,
        EventType.NEWS_ARTICLE,
        EventType.SEC_FILING,
        EventType.SOCIAL_POST,
        EventType.EARNINGS_CALL,
    ):
        bus.subscribe(et, _log_event)


async def main() -> None:
    started = datetime.now(timezone.utc)
    tickers = os.environ.get("ALPHAGENT_TICKERS", _DEFAULT_TICKERS).split(",")
    tickers = [t.strip().upper() for t in tickers if t.strip()]

    bus = EventBus()
    if _env_log_events():
        _wire_event_logging(bus)
        logger.info("ALPHAGENT_LOG_EVENTS=1 — logging each MarketEvent under run_pipeline.")

    orch = Orchestrator()

    if _env_finbert_enabled():
        if os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN"):
            logger.info(
                "Sentiment: FinBERT (ProsusAI/finbert). HF_TOKEN is set (authenticated Hub access)."
            )
        else:
            logger.info(
                "Sentiment: FinBERT (ProsusAI/finbert). Add HF_TOKEN in `.env` for faster Hub downloads. "
                "Use ALPHAGENT_USE_FINBERT=0 for keyword-only sentiment (no model download)."
            )
        orch.register_agent("sentiment", FinBERTSentimentAgent(eager_load=True))
    else:
        logger.info("Sentiment: HeuristicSentimentAgent (keyword patterns, no torch).")
        orch.register_agent("sentiment", HeuristicSentimentAgent())

    orch.register_agent("technical", TechnicalAgent())
    orch.register_agent("fundamental", FundamentalAgent())
    orch.register_agent("macro", MacroAgent())
    orch.on_signal(_print_signal)

    ingestion = IngestionAgent(tickers, bus, orchestrator=orch)

    logger.info("Starting orchestrator + ingestion (Ctrl+C to stop). Tickers=%s", tickers)

    orch_task = asyncio.create_task(orch.run())
    try:
        await ingestion.run()
    except asyncio.CancelledError:
        raise
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt — shutting down.")
    finally:
        ingestion.stop()
        orch.stop()
        try:
            await asyncio.wait_for(orch_task, timeout=60.0)
        except asyncio.TimeoutError:
            logger.warning("Orchestrator did not finish after stop(); cancelling.")
            orch_task.cancel()
            try:
                await orch_task
            except asyncio.CancelledError:
                pass
        try:
            out_path = write_latest_run_report(
                repo_root=_REPO_ROOT,
                tickers=tickers,
                started=started,
                orch=orch,
            )
            if out_path is not None:
                logger.info("Run summary (Markdown): %s", out_path.resolve())
        except Exception as e:
            logger.warning("Could not write pipeline run report: %s", e)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
