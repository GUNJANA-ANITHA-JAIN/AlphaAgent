"""
Daily cross-section technical alpha for backtests.

Per date: raw factors -> cross-section z-scores -> one regime bucket -> blend -> percentile BUY/SELL.
Rolling IC can turn weak factors off (|IC| < 0.02) or flip sign when IC < 0.
"""

from __future__ import annotations

import math
import os
import uuid
from collections import defaultdict, deque
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from typing import Any

from orchestrator.orchestrator import Direction, PartialSignal, TradeSignal

FACTOR_NAMES = ("mom20", "mom60", "dist_ma", "rev5", "vol_adj_mom", "mean_rsi_z")


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


def _wilder_rsi(closes: list[float], max_period: int = 14) -> float | None:
    n = len(closes)
    if n < 3:
        return None
    upper = min(max_period, n - 1)
    upper = max(2, upper)
    for period in range(upper, 1, -1):
        rsi = _wilder_rsi_for_period(closes, period)
        if rsi is not None:
            return rsi
    return None


def _cross_section_z(values: dict[str, float]) -> dict[str, float]:
    xs = [(t, v) for t, v in values.items() if math.isfinite(v)]
    if len(xs) < 3:
        return {t: 0.0 for t in values}
    vs = [v for _, v in xs]
    mu = sum(vs) / len(vs)
    var = sum((v - mu) ** 2 for v in vs) / max(1, len(vs) - 1)
    sd = math.sqrt(var)
    if sd < 1e-12:
        return {t: 0.0 for t in values}
    out: dict[str, float] = {}
    for t, v in values.items():
        if not math.isfinite(v):
            out[t] = 0.0
        else:
            out[t] = max(-4.0, min(4.0, (v - mu) / sd))
    return out


def _pearson(xs: list[float], ys: list[float]) -> float | None:
    n = len(xs)
    if n < 8 or n != len(ys):
        return None
    mx = sum(xs) / n
    my = sum(ys) / n
    vx = sum((x - mx) ** 2 for x in xs)
    vy = sum((y - my) ** 2 for y in ys)
    if vx < 1e-18 or vy < 1e-18:
        return None
    cov = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    return max(-1.0, min(1.0, cov / math.sqrt(vx * vy)))


@dataclass
class FactorICTracker:
    maxlen: int = 2520
    _hist: dict[str, deque[tuple[float, float]]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        for k in FACTOR_NAMES:
            self._hist[k] = deque(maxlen=self.maxlen)

    def push(self, factor: str, z_cs: float, fwd_ret: float) -> None:
        if factor not in self._hist:
            return
        if not math.isfinite(z_cs) or not math.isfinite(fwd_ret):
            return
        self._hist[factor].append((z_cs, fwd_ret))

    def ic(self, factor: str) -> float | None:
        d = self._hist.get(factor)
        if not d or len(d) < 20:
            return None
        xs = [a for a, _ in d]
        ys = [b for _, b in d]
        return _pearson(xs, ys)

    def ic_report_lines(self) -> list[str]:
        lines: list[str] = []
        for f in FACTOR_NAMES:
            ic = self.ic(f)
            if ic is None:
                lines.append(f"- **{f}:** IC=n/a  enabled=n/a  invert=n/a")
                continue
            en = abs(ic) >= 0.02
            inv = ic < 0
            lines.append(
                f"- **{f}:** IC={ic:+.4f}  enabled={en}  invert={inv}  (off if |IC|<0.02)"
            )
        return lines


def _ma(closes: list[float], n: int) -> float | None:
    if len(closes) < n:
        return None
    w = closes[-n:]
    return sum(w) / float(n)


def _ret(closes: list[float], lag: int) -> float | None:
    if len(closes) <= lag:
        return None
    a, b = closes[-lag - 1], closes[-1]
    if abs(a) < 1e-12:
        return None
    return b / a - 1.0


def _realized_vol_20(closes: list[float]) -> float | None:
    if len(closes) < 22:
        return None
    rs: list[float] = []
    for i in range(-20, 0):
        a, b = closes[i - 1], closes[i]
        if abs(a) < 1e-12:
            continue
        rs.append(math.log(b / a))
    if len(rs) < 10:
        return None
    mu = sum(rs) / len(rs)
    var = sum((x - mu) ** 2 for x in rs) / max(1, len(rs) - 1)
    return math.sqrt(max(var, 0.0))


def _raw_factors_for_ticker(closes: list[float], ma_period: int) -> dict[str, float] | None:
    n = len(closes)
    if n < 65:
        return None
    eff_ma = min(int(ma_period), n - 15)
    eff_ma = max(20, eff_ma)
    ma = _ma(closes, eff_ma)
    if ma is None or ma < 1e-9:
        return None
    c = closes[-1]
    m20 = _ret(closes, 20)
    m60 = _ret(closes, 60)
    m5 = _ret(closes, 5)
    if m20 is None or m60 is None or m5 is None:
        return None
    dist = (c - ma) / ma
    rev5 = -m5
    vol = _realized_vol_20(closes)
    if vol is None or vol < 1e-8:
        return None
    m_short = _ret(closes, 3)
    if m_short is None:
        m_short = m5
    vol_adj = m_short / (vol + 1e-6)
    rsi = _wilder_rsi(closes, 14)
    if rsi is None:
        return None
    return {
        "mom20": m20,
        "mom60": m60,
        "dist_ma": dist,
        "rev5": rev5,
        "vol_adj_mom": vol_adj,
        "_rsi": rsi,
        "_vol": vol,
    }


def _regime_exclusive(raw: dict[str, float], vol_z_cs: float) -> str:
    thr_vol = float(os.environ.get("ALPHAGENT_CS_VOL_Z", "1.5"))
    thr_trend = float(os.environ.get("ALPHAGENT_CS_TREND_DIST", "0.08"))
    if vol_z_cs > thr_vol:
        return "HIGH_VOL"
    dist = raw["dist_ma"]
    if abs(dist) > thr_trend:
        return "TREND"
    return "MEAN_REV"


def _base_factor_weights_short_horizon() -> dict[str, float]:
    return {
        "mom20": float(os.environ.get("ALPHAGENT_CS_W_MOM20", "0.38")),
        "mom60": float(os.environ.get("ALPHAGENT_CS_W_MOM60", "0.12")),
        "dist_ma": float(os.environ.get("ALPHAGENT_CS_W_DIST", "0.15")),
        "rev5": float(os.environ.get("ALPHAGENT_CS_W_REV5", "0.22")),
        "vol_adj_mom": float(os.environ.get("ALPHAGENT_CS_W_VOLADJ", "0.13")),
    }


def _ic_weight_and_sign(ic: float | None, base: float) -> tuple[float, float, str]:
    if ic is None:
        return base, 1.0, "ic=n/a"
    if abs(ic) < 0.02:
        return 0.0, 1.0, f"ic={ic:+.3f} off"
    sgn = -1.0 if ic < 0 else 1.0
    return base, sgn, f"ic={ic:+.3f}×{sgn:+.0f}"


def _combine_alpha(
    z_by: dict[str, float],
    regime: str,
    tracker: FactorICTracker,
) -> tuple[float, str]:
    base = _base_factor_weights_short_horizon()
    parts: list[str] = []

    if regime == "MEAN_REV":
        zr = z_by.get("mean_rsi_z", 0.0)
        w, sgn, tag = _ic_weight_and_sign(tracker.ic("mean_rsi_z"), 1.0)
        alpha = w * sgn * zr
        parts.append(f"MR mean_rsi_z {tag}")
        return max(-3.0, min(3.0, alpha)), "; ".join(parts)

    if regime == "HIGH_VOL":
        zv = z_by.get("vol_adj_mom", 0.0)
        w, sgn, tag = _ic_weight_and_sign(tracker.ic("vol_adj_mom"), 1.0)
        alpha = w * sgn * zv
        parts.append(f"HIGH_VOL vol_adj {tag}")
        return max(-3.0, min(3.0, alpha)), "; ".join(parts)

    acc = 0.0
    wsum = 0.0
    for f in ("mom20", "mom60", "dist_ma", "rev5"):
        ic = tracker.ic(f)
        bw = base.get(f, 0.0)
        w, sgn, tag = _ic_weight_and_sign(ic, bw)
        acc += w * sgn * z_by.get(f, 0.0)
        wsum += abs(w)
        parts.append(f"{f}:{tag}")
    if wsum < 1e-12:
        return 0.0, "TREND all IC-off"
    return max(-3.0, min(3.0, acc / wsum)), "TREND " + "; ".join(parts)


def _assign_quantiles(
    alphas: dict[str, float],
    *,
    buy_frac: float,
    sell_frac: float,
) -> dict[str, Direction]:
    items = [(t, a) for t, a in alphas.items() if math.isfinite(a)]
    n = len(items)
    out = {t: Direction.HOLD for t in alphas}
    if n < 5:
        return out
    items.sort(key=lambda x: x[1])
    nb = max(1, int(n * buy_frac))
    ns = max(1, int(n * sell_frac))
    for i in range(ns):
        out[items[i][0]] = Direction.SELL
    for i in range(n - nb, n):
        out[items[i][0]] = Direction.BUY
    return out


def _position_weight_pctile(
    alpha: float, direction: Direction, items_sorted: list[tuple[str, float]]
) -> float:
    if direction == Direction.HOLD:
        return 0.0
    alphas_only = [a for _, a in items_sorted]
    lo, hi = alphas_only[0], alphas_only[-1]
    span = hi - lo
    if span < 1e-12:
        return 0.28
    u = (alpha - lo) / span
    if direction == Direction.SELL:
        u = 1.0 - u
    cap = float(os.environ.get("ALPHAGENT_FUSION_POSITION_CAP", "0.58"))
    return min(cap, max(0.12, 0.12 + 0.46 * u))


def _forward_ret_simple(closes: list[float], idx: int, horizon: int) -> float | None:
    if idx + horizon >= len(closes):
        return None
    a, b = closes[idx], closes[idx + horizon]
    if abs(a) < 1e-12:
        return None
    return b / a - 1.0


@dataclass
class CrossSectionBacktestEngine:
    forward_horizon: int = 3
    ma_period: int = 200
    buy_frac: float = 0.20
    sell_frac: float = 0.20

    def __post_init__(self) -> None:
        self.ma_period = int(os.environ.get("ALPHAGENT_TECH_MA_PERIOD", str(self.ma_period)))
        self.buy_frac = float(os.environ.get("ALPHAGENT_CS_BUY_FRAC", str(self.buy_frac)))
        self.sell_frac = float(os.environ.get("ALPHAGENT_CS_SELL_FRAC", str(self.sell_frac)))
        self.tracker = FactorICTracker()

    def run_sync(
        self,
        timeline: list[tuple[datetime, str, float, float, float, float, int]],
        series_ts: dict[str, list[datetime]],
        series_close: dict[str, list[float]],
        tickers: list[str],
    ) -> tuple[list[tuple[datetime, str, float, TradeSignal]], dict[str, Any]]:
        by_date: dict[date, list[tuple[datetime, str, float, float, float, float, int]]] = defaultdict(list)
        for row in timeline:
            by_date[row[0].date()].append(row)

        idx_on_date: dict[tuple[str, date], int] = {}
        for t in tickers:
            for i, ts in enumerate(series_ts.get(t, [])):
                idx_on_date[(t, ts.date())] = i

        snapshots: dict[tuple[str, int], dict[str, float]] = {}
        out_rows: list[tuple[datetime, str, float, TradeSignal]] = []

        for d in sorted(by_date.keys()):
            day_rows = by_date[d]
            raw_panel: dict[str, dict[str, float]] = {}
            idx_map: dict[str, int] = {}
            for ts, ticker, o, h, low, c, vol in day_rows:
                i = idx_on_date.get((ticker, d))
                if i is None:
                    continue
                closes = series_close[ticker][: i + 1]
                raw = _raw_factors_for_ticker(closes, self.ma_period)
                if raw is None:
                    continue
                raw_panel[ticker] = raw
                idx_map[ticker] = i

            if len(raw_panel) < 5:
                continue

            mom20 = {t: raw_panel[t]["mom20"] for t in raw_panel}
            mom60 = {t: raw_panel[t]["mom60"] for t in raw_panel}
            dist_ma = {t: raw_panel[t]["dist_ma"] for t in raw_panel}
            rev5 = {t: raw_panel[t]["rev5"] for t in raw_panel}
            vol_adj = {t: raw_panel[t]["vol_adj_mom"] for t in raw_panel}
            vol_lvl = {t: raw_panel[t]["_vol"] for t in raw_panel}

            z_m20 = _cross_section_z(mom20)
            z_m60 = _cross_section_z(mom60)
            z_d = _cross_section_z(dist_ma)
            z_r5 = _cross_section_z(rev5)
            z_vam = _cross_section_z(vol_adj)
            z_vol = _cross_section_z(vol_lvl)

            rsi_raw = {t: (50.0 - raw_panel[t]["_rsi"]) / 25.0 for t in raw_panel}
            z_mean_rsi = _cross_section_z(rsi_raw)

            regimes: dict[str, str] = {}
            for t in raw_panel:
                regimes[t] = _regime_exclusive(raw_panel[t], z_vol.get(t, 0.0))

            alphas: dict[str, float] = {}
            notes: dict[str, str] = {}
            z_bundle: dict[str, dict[str, float]] = {}

            for t in raw_panel:
                z_by = {
                    "mom20": z_m20.get(t, 0.0),
                    "mom60": z_m60.get(t, 0.0),
                    "dist_ma": z_d.get(t, 0.0),
                    "rev5": z_r5.get(t, 0.0),
                    "vol_adj_mom": z_vam.get(t, 0.0),
                    "mean_rsi_z": z_mean_rsi.get(t, 0.0),
                }
                z_bundle[t] = z_by
                alpha, note = _combine_alpha(z_by, regimes[t], self.tracker)
                alphas[t] = alpha
                notes[t] = f"{regimes[t]} | {note}"

            dirs = _assign_quantiles(alphas, buy_frac=self.buy_frac, sell_frac=self.sell_frac)
            sorted_items = sorted(alphas.items(), key=lambda x: x[1])
            ic_snapshot = " ".join(self.tracker.ic_report_lines())[:400]

            for ts, ticker, o, h, low, c, vol in day_rows:
                if ticker not in alphas:
                    continue
                i = idx_map[ticker]
                direction = dirs.get(ticker, Direction.HOLD)
                alpha = alphas[ticker]
                regime = regimes[ticker]
                conf_base = float(os.environ.get("ALPHAGENT_CS_BASE_CONF", "0.62"))
                if regime == "HIGH_VOL":
                    conf_base *= 0.4
                pw = _position_weight_pctile(alpha, direction, sorted_items)
                reasoning = (
                    f"CS_panel d={d} α={alpha:+.3f} regime={regime} | {notes[ticker]} | "
                    f"{ic_snapshot}"
                )
                ps = PartialSignal(
                    agent_name="technical_cs",
                    ticker=ticker,
                    score=round(alpha, 4),
                    confidence=round(conf_base, 3),
                    timestamp=datetime.now(timezone.utc),
                    reasoning=reasoning[:480],
                    decay_hours=6.0,
                    source_event_ids=[],
                )
                sig = TradeSignal(
                    signal_id=str(uuid.uuid4()),
                    ticker=ticker,
                    direction=direction,
                    confidence=round(conf_base, 3),
                    raw_score=round(alpha, 4),
                    contributing=[ps],
                    reasoning=reasoning[:800],
                    timestamp=datetime.now(timezone.utc),
                    decay_hours=6.0,
                    num_agents=1,
                    position_weight=round(pw, 4),
                )
                out_rows.append((ts, ticker, float(c), sig))

                snap: dict[str, float] = {}
                zb = z_bundle[ticker]
                r = regimes[ticker]
                if r == "TREND":
                    for f in ("mom20", "mom60", "dist_ma", "rev5"):
                        snap[f] = zb.get(f, 0.0)
                elif r == "MEAN_REV":
                    snap["mean_rsi_z"] = zb.get("mean_rsi_z", 0.0)
                else:
                    snap["vol_adj_mom"] = zb.get("vol_adj_mom", 0.0)
                snapshots[(ticker, i)] = snap

            for ts, ticker, o, h, low, c, vol in day_rows:
                i = idx_map.get(ticker)
                if i is None or i < self.forward_horizon:
                    continue
                i0 = i - self.forward_horizon
                cl = series_close[ticker]
                fwd = _forward_ret_simple(cl, i0, self.forward_horizon)
                if fwd is None:
                    continue
                snap = snapshots.get((ticker, i0))
                if not snap:
                    continue
                for fname, zv in snap.items():
                    self.tracker.push(fname, zv, fwd)

        meta: dict[str, Any] = {
            "replay_timeline_bars": len(timeline),
            "signals_emitted": len(out_rows),
            "ttl_forced": 0,
            "events_processed": len(timeline),
            "factor_ic_report": self.tracker.ic_report_lines(),
        }
        return out_rows, meta


async def run_cross_section_backtest(
    timeline: list[tuple[datetime, str, float, float, float, float, int]],
    series_ts: dict[str, list[datetime]],
    series_close: dict[str, list[float]],
    tickers: list[str],
    *,
    forward_horizon: int,
) -> tuple[list[tuple[datetime, str, float, TradeSignal]], dict[str, Any]]:
    eng = CrossSectionBacktestEngine(forward_horizon=forward_horizon)
    return eng.run_sync(timeline, series_ts, series_close, tickers)
