"""
Replay daily bars through the price path: yfinance -> signals -> report.

Default uses cross-section engine (cs_technical). Set ALPHAGENT_BACKTEST_CS_PANEL=0
for older per-bar orchestrator + TechnicalAgent + fuse path.
"""

from __future__ import annotations

import logging
import math
import os
import uuid
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timezone
from typing import Any

from core.models import DataSource, EventType, MarketEvent
from orchestrator.cs_technical import CrossSectionBacktestEngine
from orchestrator.orchestrator import Orchestrator, TradeSignal, format_trade_signal_message
from orchestrator.technical_agent import TechnicalAgent

logger = logging.getLogger(__name__)


@dataclass
class SignalRecord:
    bar_time: datetime
    ticker: str
    close: float
    signal: TradeSignal


def _yf_history(ticker: str, period: str):
    try:
        import yfinance as yf
    except ImportError as e:
        raise SystemExit(
            "Backtest requires `yfinance`. Install: pip install -r requirements.txt"
        ) from e
    return yf.Ticker(ticker).history(period=period, auto_adjust=True)


def _build_series_and_timeline(
    tickers: list[str], period: str
) -> tuple[
    list[tuple[datetime, str, float, float, float, float, int]],
    dict[str, list[datetime]],
    dict[str, list[float]],
]:
    """One yfinance pull per ticker; merged time-ordered bar list + per-ticker closes."""
    timeline: list[tuple[datetime, str, float, float, float, float, int]] = []
    series_ts: dict[str, list[datetime]] = {t: [] for t in tickers}
    series_close: dict[str, list[float]] = {t: [] for t in tickers}

    for t in tickers:
        hist = _yf_history(t, period)
        if hist.empty:
            logger.warning("No history for %s", t)
            continue
        for idx, row in hist.iterrows():
            ts = idx.to_pydatetime().replace(tzinfo=timezone.utc)
            o, h, low, c = float(row["Open"]), float(row["High"]), float(row["Low"]), float(row["Close"])
            vol = int(row["Volume"])
            timeline.append((ts, t, o, h, low, c, vol))
            series_ts[t].append(ts)
            series_close[t].append(c)

    timeline.sort(key=lambda r: (r[0], r[1]))
    return timeline, series_ts, series_close


def _build_price_event(
    ticker: str, ts: datetime, o: float, h: float, low: float, c: float, vol: int
) -> MarketEvent:
    return MarketEvent(
        event_id=str(uuid.uuid4()),
        event_type=EventType.PRICE_UPDATE,
        source=DataSource.YFINANCE,
        ticker=ticker,
        timestamp=ts,
        ingested_at=datetime.now(timezone.utc),
        payload={
            "open": o,
            "high": h,
            "low": low,
            "close": c,
            "volume": vol,
            "interval": "1d",
        },
        confidence=1.0,
        tags=["backtest"],
    )


def _forward_ret(closes: list[float], idx: int, horizon: int) -> float | None:
    if idx + horizon >= len(closes):
        return None
    a, b = closes[idx], closes[idx + horizon]
    if a == 0:
        return None
    return b / a - 1.0


def _pearson_ic(xs: list[float], ys: list[float]) -> float | None:
    n = len(xs)
    if n < 5 or n != len(ys):
        return None
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    denx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    deny = math.sqrt(sum((y - my) ** 2 for y in ys))
    if denx < 1e-18 or deny < 1e-18:
        return None
    return num / (denx * deny)


def _max_drawdown(equity_steps: list[float]) -> float:
    """Worst drop from a running peak on the PnL path (<= 0)."""
    if not equity_steps:
        return 0.0
    peak = equity_steps[0]
    mdd = 0.0
    for x in equity_steps:
        peak = max(peak, x)
        mdd = min(mdd, x - peak)
    return mdd


def _score_decile_lines(pairs: list[tuple[float, float]], n_bins: int = 10) -> list[str]:
    """pairs are (raw_score, forward_return) for decile table."""
    if len(pairs) < n_bins * 3:
        return ["_Too few completed windows for score deciles._"]
    pairs_sorted = sorted(pairs, key=lambda z: z[0])
    n = len(pairs_sorted)
    lines: list[str] = [
        "",
        "| Bucket | n | raw_score range | mean_fwd |",
        "|--------|---|-----------------|----------|",
    ]
    for k in range(n_bins):
        lo = k * n // n_bins
        hi = (k + 1) * n // n_bins if k < n_bins - 1 else n
        chunk = pairs_sorted[lo:hi]
        rs = [p[0] for p in chunk]
        frs = [p[1] for p in chunk]
        mu = sum(frs) / len(frs)
        lines.append(
            f"| Q{k + 1} | {len(chunk)} | [{min(rs):+.3f}, {max(rs):+.3f}] | {mu:+.4f} |"
        )
    return lines


def _cross_section_ls_daily_pnls(
    records: list[SignalRecord],
    *,
    series_close: dict[str, list[float]],
    horizon: int,
    idx_for,
    quantile: float = 0.25,
    min_names: int = 8,
    cost_bps: float = 0.0,
    borrow_bps: float = 0.0,
) -> tuple[list[float], list[date]]:
    """
    Each day: rank tickers by fused raw_score among names with a full H-day forward return.
    Long top q fraction equal-weight, short bottom q equal-weight (50/50 gross).
    Day PnL = 0.5 * mean(long fwd) - 0.5 * mean(short fwd) minus simple costs.
    """
    q = max(0.05, min(0.45, float(quantile)))
    min_n = max(4, int(min_names))
    by_date: dict[date, list[tuple[str, float, float]]] = defaultdict(list)

    for rec in records:
        i = idx_for(rec.ticker, rec.bar_time)
        if i is None:
            continue
        fr = _forward_ret(series_close[rec.ticker], i, horizon)
        if fr is None:
            continue
        by_date[rec.bar_time.date()].append(
            (rec.ticker, float(rec.signal.raw_score), float(fr))
        )

    pnls: list[float] = []
    dates_used: list[date] = []

    for d in sorted(by_date.keys()):
        rows = by_date[d]
        if len(rows) < min_n:
            continue
        rows.sort(key=lambda r: r[1], reverse=True)
        n = len(rows)
        k = max(1, int(n * q))
        if 2 * k > n:
            k = max(1, n // 4)
        longs = rows[:k]
        shorts = rows[-k:]
        ml = sum(x[2] for x in longs) / len(longs)
        ms = sum(x[2] for x in shorts) / len(shorts)
        gross = 0.5 * ml - 0.5 * ms
        # round-trip cost on 1.0 notional (open + close both legs)
        cost_rt = 2.0 * (cost_bps / 10000.0)
        # short leg borrow: annual bps * 0.5 short weight * (hold days / 252)
        borrow_drag = 0.5 * (borrow_bps / 10000.0) * (float(horizon) / 252.0)
        net = gross - cost_rt - borrow_drag
        pnls.append(net)
        dates_used.append(d)

    return pnls, dates_used


def _event_pnl(
    direction: str,
    fwd_ret: float,
    position_weight: float,
    *,
    exposure: str,
    cost_bps: float,
) -> float:
    """
    Simple mark: position_weight * sign * forward return minus one-way cost on weight.
    long_only: SELL returns 0 (caller skips shorts).
    """
    if direction == "HOLD":
        return 0.0
    if exposure.strip().lower() == "long_only" and direction == "SELL":
        return 0.0
    sign = 1.0 if direction == "BUY" else -1.0
    gross = position_weight * sign * fwd_ret
    cost = (cost_bps / 10000.0) * max(position_weight, 0.0)
    return gross - cost


async def run_price_bar_backtest(
    *,
    tickers: list[str],
    period: str = "1y",
    forward_horizon: int = 3,
) -> tuple[list[SignalRecord], dict[str, list[float]], dict[str, list[datetime]], dict[str, int]]:
    """
    Replay bars. Default: CrossSectionBacktestEngine. Legacy: Orchestrator + TechnicalAgent
    when ALPHAGENT_BACKTEST_CS_PANEL=0.
    """
    timeline, series_ts, series_close = _build_series_and_timeline(tickers, period)

    use_cs = os.environ.get("ALPHAGENT_BACKTEST_CS_PANEL", "1").strip().lower() not in (
        "0",
        "false",
        "no",
        "off",
    )

    if use_cs:
        eng = CrossSectionBacktestEngine(forward_horizon=forward_horizon)
        rows, meta = eng.run_sync(timeline, series_ts, series_close, tickers)
        records = [SignalRecord(bar_time=a, ticker=b, close=c, signal=s) for a, b, c, s in rows]
        st = {
            "events_processed": meta.get("events_processed", len(timeline)),
            "signals_emitted": meta.get("signals_emitted", len(records)),
            "ttl_forced": meta.get("ttl_forced", 0),
            "replay_timeline_bars": len(timeline),
            "factor_ic_report": meta.get("factor_ic_report", []),
        }
        return records, series_close, series_ts, st

    orch = Orchestrator()
    orch.register_agent("technical", TechnicalAgent())

    records: list[SignalRecord] = []
    prev_n = 0

    for ts, ticker, o, h, low, c, vol in timeline:
        evt = _build_price_event(ticker, ts, o, h, low, c, vol)
        await orch.process_event(evt)
        n = len(orch.signal_history())
        if n > prev_n:
            sig = orch.signal_history()[-1]
            records.append(SignalRecord(bar_time=ts, ticker=ticker, close=c, signal=sig))
            prev_n = n

    st = orch.get_stats()
    st["replay_timeline_bars"] = len(timeline)
    st["factor_ic_report"] = []
    return records, series_close, series_ts, st


def build_backtest_report_md(
    *,
    tickers: list[str],
    period: str,
    horizon: int,
    records: list[SignalRecord],
    series_close: dict[str, list[float]],
    series_ts: dict[str, list[datetime]],
    stats: dict[str, int],
    cost_bps: float = 0.0,
    exposure: str = "long_short",
    borrow_bps: float = 0.0,
    ls_quantile: float = 0.25,
    ls_min_names: int = 8,
) -> str:
    """Markdown report: buckets, forward returns, IC, toy PnL, cross-section block."""

    def idx_for(t: str, bar_time: datetime) -> int | None:
        ts_list = series_ts.get(t) or []
        for i, x in enumerate(ts_list):
            if x.date() == bar_time.date():
                return i
        return None

    fwd_samples: list[tuple[str, str, float | None]] = []
    ic_pairs: list[tuple[float, float]] = []
    event_pnls: list[float] = []

    for rec in records:
        i = idx_for(rec.ticker, rec.bar_time)
        if i is None:
            fwd_samples.append((rec.ticker, rec.signal.direction.value, None))
            continue
        fr = _forward_ret(series_close[rec.ticker], i, horizon)
        fwd_samples.append((rec.ticker, rec.signal.direction.value, fr))
        if fr is not None:
            ic_pairs.append((rec.signal.raw_score, fr))
        d = rec.signal.direction.value
        if fr is not None and d != "HOLD":
            if exposure.strip().lower() == "long_only" and d == "SELL":
                pass
            else:
                event_pnls.append(
                    _event_pnl(
                        d,
                        fr,
                        rec.signal.position_weight,
                        exposure=exposure,
                        cost_bps=cost_bps,
                    )
                )

    ic = _pearson_ic([a for a, _ in ic_pairs], [b for _, b in ic_pairs]) if ic_pairs else None
    exp_label = exposure.strip().lower()

    lines = [
        "# AlphaAgent — price-only backtest (walk-forward)",
        "",
        "| Setting | Value |",
        "|---------|-------|",
        f"| Tickers | {', '.join(tickers)} |",
        f"| History window | `{period}` (yfinance daily) |",
        f"| Forward horizon | **{horizon}** trading days |",
        f"| Signals emitted | **{len(records)}** |",
        f"| Replay timeline bars | **{stats.get('replay_timeline_bars', '—')}** |",
        f"| Transaction cost | **{cost_bps:g}** bps one-way on `position_weight` |",
        f"| Exposure model | **`{exp_label}`** (SELL: short unless long_only) |",
        f"| Short borrow (CS L/S) | **{borrow_bps:g}** bps annualized drag on 50% short leg × horizon/252 |",
        f"| CS L/S book | top/bottom **{ls_quantile:.0%}** of names per day (min **{ls_min_names}** names) |",
        "",
        "## Orchestrator stats",
        "",
    ]
    for k, v in sorted(stats.items()):
        if k == "factor_ic_report":
            continue
        lines.append(f"- **{k}:** {v}")
    ic_rep = stats.get("factor_ic_report") or []
    if ic_rep:
        lines.extend(["", "## Rolling factor IC (pooled, trailing observations)", ""])
        lines.extend(ic_rep)
    lines.append("")
    lines.append("## Direction mix (fused signals)")
    c = Counter(r.signal.direction.value for r in records)
    for d in ("BUY", "SELL", "HOLD"):
        lines.append(f"- **{d}:** {c.get(d, 0)}")
    lines.extend(["", "## Naive forward return (by fused direction)", ""])

    for d in ("BUY", "SELL", "HOLD"):
        xs = [fr for _, di, fr in fwd_samples if di == d and fr is not None]
        if not xs:
            lines.append(f"- **{d}:** (no completed {horizon}d forward windows)")
            continue
        lines.append(
            f"- **{d}:** n={len(xs)}  mean_fwd={sum(xs)/len(xs):+.4f}  "
            f"min={min(xs):+.4f}  max={max(xs):+.4f}"
        )

    lines.extend(
        [
            "",
            "## Continuous alpha vs forward return",
            "",
            "Pearson **IC** between fused `raw_score` and realized "
            f"{horizon}d forward return (all emitted signals with a full window):",
            "",
        ]
    )
    if ic is None:
        lines.append("- **IC:** _insufficient variance or sample size_")
    else:
        lines.append(f"- **IC (Pearson):** {ic:+.4f}")
    lines.extend(
        [
            "",
            "_`raw_score` is the continuous fused ensemble in [-1, +1]; BUY/SELL/HOLD is only a threshold view._",
            "",
        ]
    )
    lines.extend(_score_decile_lines(ic_pairs))
    lines.append("")

    lines.extend(
        [
            "## Position-weighted event PnL (toy)",
            "",
            "Each **BUY**/**SELL** with a full forward window: "
            "`pnl = position_weight × sign × fwd_ret − cost`, "
            "where `position_weight` comes from fusion (strength past HOLD band × confidence). "
            "`long_only` excludes SELL legs from this stream (no short).",
            "",
        ]
    )
    if not event_pnls:
        lines.append("_No directional signals with completed forward windows._")
    else:
        mu = sum(event_pnls) / len(event_pnls)
        var = sum((x - mu) ** 2 for x in event_pnls) / max(1, len(event_pnls) - 1)
        sd = math.sqrt(var) if len(event_pnls) > 1 else 0.0
        sharpe_evt = (mu / sd) if sd > 1e-12 else None
        # rough annualization; overlaps ignored
        ann_scale = math.sqrt(252.0 / max(1, horizon))
        sharpe_ann = sharpe_evt * ann_scale if sharpe_evt is not None else None
        cum: list[float] = []
        s = 0.0
        for p in event_pnls:
            s += p
            cum.append(s)
        mdd = _max_drawdown(cum)
        lines.append(f"- **Events (sized):** n={len(event_pnls)}")
        lines.append(f"- **Mean / std (per event):** {mu:+.6f} / {sd:.6f}")
        if sharpe_evt is not None:
            lines.append(f"- **Event Sharpe (μ/σ):** {sharpe_evt:+.3f}")
        else:
            lines.append("- **Event Sharpe:** _undefined (σ≈0)_")
        if sharpe_ann is not None:
            lines.append(
                f"- **Loose annualized Sharpe** (×√(252/H), overlapping holds ignored): **{sharpe_ann:+.3f}**"
            )
        lines.append(f"- **Cumulative PnL (sum of events):** {cum[-1]:+.4f}")
        lines.append(f"- **Max drawdown (event-time equity):** {mdd:.4f}")
        lines.append("")
        lines.append("_Not calendar portfolio accounting, beta-neutral book, or borrow cost — research harness only._")
        if exp_label == "long_short":
            lines.append("")
            lines.append(
                "_`long_short` toy PnL includes shorts; when 5d drift after SELLs is positive, "
                "that leg drags the sum. Use `--exposure long_only` (or env `ALPHAGENT_BACKTEST_EXPOSURE`) "
                "to score BUY legs only and separate short-side effects from alpha quality._"
            )

    cs_pnls, _cs_dates = _cross_section_ls_daily_pnls(
        records,
        series_close=series_close,
        horizon=horizon,
        idx_for=idx_for,
        quantile=ls_quantile,
        min_names=ls_min_names,
        cost_bps=cost_bps,
        borrow_bps=borrow_bps,
    )
    lines.extend(
        [
            "",
            "## Cross-sectional dollar-neutral L/S book",
            "",
            "Each **calendar date**, among tickers with a full **H-day** forward window, rank by fused **`raw_score`**. "
            "Go **equal-weight long** the top **q** fraction and **equal-weight short** the bottom **q** (gross **50% / 50%**). "
            "Day mark: **`0.5 × mean(fwd long) − 0.5 × mean(fwd short)`** minus a simple **round-trip cost** "
            f"(`2 × cost_bps` on 1.0 notional) and optional **short borrow** (`0.5 × borrow_bps × H/252`).",
            "",
            "_This isolates **relative** (cross-sectional) alpha the way many **equity long/short** books are evaluated; "
            "it does **not** change orchestrator `BUY`/`SELL`/`HOLD` — only how **portfolio** toy PnL is computed in this report._",
            "",
        ]
    )
    if not cs_pnls:
        lines.append(
            f"_No days with ≥ **{ls_min_names}** names and full forward windows — widen universe, "
            "lower `--ls-min-names`, or shorten `--horizon`._"
        )
    else:
        mu_cs = sum(cs_pnls) / len(cs_pnls)
        var_cs = sum((x - mu_cs) ** 2 for x in cs_pnls) / max(1, len(cs_pnls) - 1)
        sd_cs = math.sqrt(var_cs) if len(cs_pnls) > 1 else 0.0
        sharpe_d = (mu_cs / sd_cs) if sd_cs > 1e-12 else None
        ann_cs = sharpe_d * math.sqrt(252.0) if sharpe_d is not None else None
        cum_cs: list[float] = []
        s_cs = 0.0
        for p in cs_pnls:
            s_cs += p
            cum_cs.append(s_cs)
        mdd_cs = _max_drawdown(cum_cs)
        lines.append(f"- **Rebalance days (marks):** n={len(cs_pnls)}")
        lines.append(f"- **Mean / std (daily portfolio return):** {mu_cs:+.6f} / {sd_cs:.6f}")
        if sharpe_d is not None:
            lines.append(f"- **Daily Sharpe (μ/σ):** {sharpe_d:+.3f}")
        else:
            lines.append("- **Daily Sharpe:** _undefined (σ≈0)_")
        if ann_cs is not None:
            lines.append(f"- **Loose annualized Sharpe** (×√252): **{ann_cs:+.3f}**")
        lines.append(f"- **Cumulative PnL (sum of daily marks):** {cum_cs[-1]:+.4f}")
        lines.append(f"- **Max drawdown (daily equity):** {mdd_cs:.4f}")
        lines.append("")
        lines.append(
            "_Overlapping **H-day** windows: each day’s mark uses the same forward horizon, so the cumulative sum is a "
            "**research aggregate**, not a single non-overlapping portfolio path._"
        )

    hits_buy = sum(1 for _, di, fr in fwd_samples if di == "BUY" and fr is not None and fr > 0)
    tot_buy = sum(1 for _, di, fr in fwd_samples if di == "BUY" and fr is not None)
    hits_sell = sum(1 for _, di, fr in fwd_samples if di == "SELL" and fr is not None and fr < 0)
    tot_sell = sum(1 for _, di, fr in fwd_samples if di == "SELL" and fr is not None)
    lines.extend(
        [
            "",
            "## Directional hit rates (toy labels)",
            "",
            f"- **BUY** then positive {horizon}d return: **{hits_buy} / {tot_buy}**"
            if tot_buy
            else "- **BUY:** n=0",
            f"- **SELL** then negative {horizon}d return: **{hits_sell} / {tot_sell}**"
            if tot_sell
            else "- **SELL:** n=0",
            "",
            "_Slippage, borrow, and statistical significance not modeled — sanity / research harness._",
            "",
            "## Sample signals (last 15)",
            "",
        ]
    )
    for rec in records[-15:]:
        fr = None
        i = idx_for(rec.ticker, rec.bar_time)
        if i is not None:
            fr = _forward_ret(series_close[rec.ticker], i, horizon)
        fr_s = f"{fr:+.2%}" if fr is not None else "n/a"
        lines.append(
            f"### {rec.bar_time.date()} `{rec.ticker}` → {rec.signal.direction.value} "
            f"(fwd {horizon}d={fr_s})"
        )
        lines.append("```")
        lines.append(format_trade_signal_message(rec.signal))
        lines.append("```")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(
        "_Replay: cross-sectional panel alpha (`orchestrator/cs_technical.py`) unless "
        "`ALPHAGENT_BACKTEST_CS_PANEL=0` (legacy per-bar orchestrator path)._"
    )
    return "\n".join(lines)
