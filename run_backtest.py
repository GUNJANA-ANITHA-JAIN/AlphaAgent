"""
Price-only backtest: daily bars -> signals -> runs/backtest_last.md.

Default: panel cross-section path. ALPHAGENT_BACKTEST_CS_PANEL=0 for legacy orchestrator replay.

Examples:
  python run_backtest.py
  python run_backtest.py --tickers AAPL,MSFT --period 2y --horizon 10
Fusion/env: same as run_pipeline.py (e.g. ALPHAGENT_HOLD_DEADBAND).
Costs: ALPHAGENT_BACKTEST_COST_BPS, ALPHAGENT_BACKTEST_EXPOSURE.
CS book in report: ALPHAGENT_BACKTEST_BORROW_BPS, ALPHAGENT_BACKTEST_LS_QUANTILE, ALPHAGENT_BACKTEST_CS_MIN_NAMES.
"""

from __future__ import annotations

import argparse
import asyncio
import logging
import os
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent
try:
    from dotenv import load_dotenv

    load_dotenv(_REPO_ROOT / ".env")
except ImportError:
    pass
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from backtest.price_walk import build_backtest_report_md, run_price_bar_backtest

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("run_backtest")

_DEFAULT_BT = "AAPL,MSFT,GOOGL,AMZN,META,NVDA,TSLA,JPM,JNJ,V,UNH,XOM,PG,MA,HD,CVX,MRK,ABBV,PEP,COST"


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="AlphaAgent price-only backtest (walk-forward daily)")
    p.add_argument(
        "--tickers",
        default=os.environ.get("ALPHAGENT_BACKTEST_TICKERS", _DEFAULT_BT),
        help="Comma-separated symbols (default: env ALPHAGENT_BACKTEST_TICKERS or AAPL,MSFT,GOOGL)",
    )
    p.add_argument(
        "--period",
        default=os.environ.get("ALPHAGENT_BACKTEST_PERIOD", "1y"),
        help="yfinance period string, e.g. 6mo, 1y, 2y, max",
    )
    p.add_argument(
        "--horizon",
        type=int,
        default=int(os.environ.get("ALPHAGENT_BACKTEST_HORIZON", "3")),
        help="Forward return horizon in trading days (default 3; env ALPHAGENT_BACKTEST_HORIZON)",
    )
    p.add_argument(
        "--output",
        default=os.environ.get("ALPHAGENT_BACKTEST_OUTPUT", str(_REPO_ROOT / "runs" / "backtest_last.md")),
        help="Markdown report path",
    )
    p.add_argument(
        "--cost-bps",
        type=float,
        default=float(os.environ.get("ALPHAGENT_BACKTEST_COST_BPS", "0")),
        help="One-way transaction cost in basis points on position_weight notional (default env ALPHAGENT_BACKTEST_COST_BPS or 0)",
    )
    p.add_argument(
        "--exposure",
        default=os.environ.get("ALPHAGENT_BACKTEST_EXPOSURE", "long_short"),
        choices=["long_short", "long_only"],
        help="Toy PnL: long_short charges SELL as short; long_only uses BUY legs only (default env ALPHAGENT_BACKTEST_EXPOSURE)",
    )
    p.add_argument(
        "--borrow-bps",
        type=float,
        default=float(os.environ.get("ALPHAGENT_BACKTEST_BORROW_BPS", "0")),
        help="Annual short-borrow drag (bps) applied in CS L/S section on 50%% short × H/252 (env ALPHAGENT_BACKTEST_BORROW_BPS)",
    )
    p.add_argument(
        "--ls-quantile",
        type=float,
        default=float(os.environ.get("ALPHAGENT_BACKTEST_LS_QUANTILE", "0.25")),
        help="Top/bottom fraction for cross-sectional L/S book (env ALPHAGENT_BACKTEST_LS_QUANTILE, default 0.25)",
    )
    p.add_argument(
        "--ls-min-names",
        type=int,
        default=int(os.environ.get("ALPHAGENT_BACKTEST_CS_MIN_NAMES", "8")),
        help="Minimum names per calendar date to form CS L/S book (env ALPHAGENT_BACKTEST_CS_MIN_NAMES)",
    )
    return p.parse_args()


async def _async_main(args: argparse.Namespace) -> None:
    tickers = [t.strip().upper() for t in args.tickers.split(",") if t.strip()]
    if not tickers:
        logger.error("No tickers after parsing --tickers")
        return

    logger.info("Backtest tickers=%s period=%s horizon=%dd", tickers, args.period, args.horizon)
    records, series_close, series_ts, stats = await run_price_bar_backtest(
        tickers=tickers,
        period=args.period,
        forward_horizon=args.horizon,
    )
    q = max(0.05, min(0.45, float(args.ls_quantile)))
    md = build_backtest_report_md(
        tickers=tickers,
        period=args.period,
        horizon=args.horizon,
        records=records,
        series_close=series_close,
        series_ts=series_ts,
        stats=stats,
        cost_bps=float(args.cost_bps),
        exposure=str(args.exposure),
        borrow_bps=max(0.0, float(args.borrow_bps)),
        ls_quantile=q,
        ls_min_names=max(4, int(args.ls_min_names)),
    )
    out = Path(args.output).expanduser()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8")
    logger.info("Wrote backtest report: %s", out.resolve())
    logger.info("Signals captured: %s", len(records))


def main() -> None:
    args = _parse_args()
    asyncio.run(_async_main(args))


if __name__ == "__main__":
    main()
