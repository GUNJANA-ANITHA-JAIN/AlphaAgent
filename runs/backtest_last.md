# AlphaAgent — price-only backtest (walk-forward)

| Setting | Value |
|---------|-------|
| Tickers | AAPL, MSFT, GOOGL, AMZN, META, NVDA, TSLA, JPM, JNJ, V, UNH, XOM, PG, MA, HD, CVX, MRK, ABBV, PEP, COST |
| History window | `3y` (yfinance daily) |
| Forward horizon | **5** trading days |
| Signals emitted | **13780** |
| Replay timeline bars | **15060** |
| Transaction cost | **0** bps one-way on `position_weight` |
| Exposure model | **`long_short`** (SELL: short unless long_only) |
| Short borrow (CS L/S) | **0** bps annualized drag on 50% short leg × horizon/252 |
| CS L/S book | top/bottom **25%** of names per day (min **8** names) |

## Orchestrator stats

- **events_processed:** 15060
- **replay_timeline_bars:** 15060
- **signals_emitted:** 13780
- **ttl_forced:** 0

## Rolling factor IC (pooled, trailing observations)

- **mom20:** IC=-0.0525  enabled=True  invert=True  (off if |IC|<0.02)
- **mom60:** IC=-0.0176  enabled=False  invert=True  (off if |IC|<0.02)
- **dist_ma:** IC=-0.0383  enabled=True  invert=True  (off if |IC|<0.02)
- **rev5:** IC=+0.0254  enabled=True  invert=False  (off if |IC|<0.02)
- **vol_adj_mom:** IC=+0.0726  enabled=True  invert=False  (off if |IC|<0.02)
- **mean_rsi_z:** IC=-0.0048  enabled=False  invert=True  (off if |IC|<0.02)

## Direction mix (fused signals)
- **BUY:** 2756
- **SELL:** 2756
- **HOLD:** 8268

## Naive forward return (by fused direction)

- **BUY:** n=2736  mean_fwd=+0.0060  min=-0.1730  max=+0.2782
- **SELL:** n=2736  mean_fwd=+0.0052  min=-0.2905  max=+0.3661
- **HOLD:** n=8208  mean_fwd=+0.0031  min=-0.2884  max=+0.4413

## Continuous alpha vs forward return

Pearson **IC** between fused `raw_score` and realized 5d forward return (all emitted signals with a full window):

- **IC (Pearson):** -0.0064

_`raw_score` is the continuous fused ensemble in [-1, +1]; BUY/SELL/HOLD is only a threshold view._


| Bucket | n | raw_score range | mean_fwd |
|--------|---|-----------------|----------|
| Q1 | 1368 | [-3.000, -1.140] | +0.0055 |
| Q2 | 1368 | [-1.139, -0.729] | +0.0071 |
| Q3 | 1368 | [-0.729, -0.421] | +0.0035 |
| Q4 | 1368 | [-0.420, -0.185] | +0.0051 |
| Q5 | 1368 | [-0.185, +0.000] | +0.0042 |
| Q6 | 1368 | [-0.000, +0.047] | +0.0015 |
| Q7 | 1368 | [+0.047, +0.276] | +0.0011 |
| Q8 | 1368 | [+0.276, +0.550] | +0.0019 |
| Q9 | 1368 | [+0.550, +0.928] | +0.0045 |
| Q10 | 1368 | [+0.929, +3.000] | +0.0070 |

## Position-weighted event PnL (toy)

Each **BUY**/**SELL** with a full forward window: `pnl = position_weight × sign × fwd_ret − cost`, where `position_weight` comes from fusion (strength past HOLD band × confidence). `long_only` excludes SELL legs from this stream (no short).

- **Events (sized):** n=5472
- **Mean / std (per event):** +0.000217 / 0.022401
- **Event Sharpe (μ/σ):** +0.010
- **Loose annualized Sharpe** (×√(252/H), overlapping holds ignored): **+0.069**
- **Cumulative PnL (sum of events):** +1.1848
- **Max drawdown (event-time equity):** -2.3714

_Not calendar portfolio accounting, beta-neutral book, or borrow cost — research harness only._

_`long_short` toy PnL includes shorts; when 5d drift after SELLs is positive, that leg drags the sum. Use `--exposure long_only` (or env `ALPHAGENT_BACKTEST_EXPOSURE`) to score BUY legs only and separate short-side effects from alpha quality._

## Cross-sectional dollar-neutral L/S book

Each **calendar date**, among tickers with a full **H-day** forward window, rank by fused **`raw_score`**. Go **equal-weight long** the top **q** fraction and **equal-weight short** the bottom **q** (gross **50% / 50%**). Day mark: **`0.5 × mean(fwd long) − 0.5 × mean(fwd short)`** minus a simple **round-trip cost** (`2 × cost_bps` on 1.0 notional) and optional **short borrow** (`0.5 × borrow_bps × H/252`).

_This isolates **relative** (cross-sectional) alpha the way many **equity long/short** books are evaluated; it does **not** change orchestrator `BUY`/`SELL`/`HOLD` — only how **portfolio** toy PnL is computed in this report._

- **Rebalance days (marks):** n=684
- **Mean / std (daily portfolio return):** +0.000032 / 0.013885
- **Daily Sharpe (μ/σ):** +0.002
- **Loose annualized Sharpe** (×√252): **+0.037**
- **Cumulative PnL (sum of daily marks):** +0.0220
- **Max drawdown (daily equity):** -0.5591

_Overlapping **H-day** windows: each day’s mark uses the same forward horizon, so the cumulative sum is a **research aggregate**, not a single non-overlapping portfolio path._

## Directional hit rates (toy labels)

- **BUY** then positive 5d return: **1528 / 2736**
- **SELL** then negative 5d return: **1184 / 2736**

_Slippage, borrow, and statistical significance not modeled — sanity / research harness._

## Sample signals (last 15)

### 2026-05-14 `GOOGL` → HOLD (fwd 5d=n/a)
```
TradeSignal GOOGL → HOLD
  raw_score=+0.25560   confidence=0.248   position_weight=0.0000   agents=1
  contributing partials:
    · technical_cs  score=+0.2556  conf=0.25  — CS_panel d=2026-05-14 α=+0.256 regime=HIGH_VOL | HIGH_VOL | HIGH_VOL vol_adj ic=+0.071×+1 | - **mom2…
  combined reasoning: CS_panel d=2026-05-14 α=+0.256 regime=HIGH_VOL | HIGH_VOL | HIGH_VOL vol_adj ic=+0.071×+1 | - **mom20:** IC=-0.0533  enabled=True  invert=True  (off if |IC|<0.02) - **mom60:** IC=-0.0217  enabled=True  invert=True  (off if |IC|<0.02) - *…
```

### 2026-05-14 `HD` → BUY (fwd 5d=n/a)
```
TradeSignal HD → BUY
  raw_score=+1.48360   confidence=0.620   position_weight=0.5800   agents=1
  contributing partials:
    · technical_cs  score=+1.4836  conf=0.62  — CS_panel d=2026-05-14 α=+1.484 regime=TREND | TREND | TREND mom20:ic=-0.053×-1; mom60:ic=-0.022×-1; …
  combined reasoning: CS_panel d=2026-05-14 α=+1.484 regime=TREND | TREND | TREND mom20:ic=-0.053×-1; mom60:ic=-0.022×-1; dist_ma:ic=-0.043×-1; rev5:ic=+0.025×+1 | - **mom20:** IC=-0.0533  enabled=True  invert=True  (off if |IC|<0.02) - **mom60:** IC=-0.0217 …
```

### 2026-05-14 `JNJ` → HOLD (fwd 5d=n/a)
```
TradeSignal JNJ → HOLD
  raw_score=+0.12630   confidence=0.620   position_weight=0.0000   agents=1
  contributing partials:
    · technical_cs  score=+0.1263  conf=0.62  — CS_panel d=2026-05-14 α=+0.126 regime=TREND | TREND | TREND mom20:ic=-0.053×-1; mom60:ic=-0.022×-1; …
  combined reasoning: CS_panel d=2026-05-14 α=+0.126 regime=TREND | TREND | TREND mom20:ic=-0.053×-1; mom60:ic=-0.022×-1; dist_ma:ic=-0.043×-1; rev5:ic=+0.025×+1 | - **mom20:** IC=-0.0533  enabled=True  invert=True  (off if |IC|<0.02) - **mom60:** IC=-0.0217 …
```

### 2026-05-14 `JPM` → HOLD (fwd 5d=n/a)
```
TradeSignal JPM → HOLD
  raw_score=+0.00000   confidence=0.620   position_weight=0.0000   agents=1
  contributing partials:
    · technical_cs  score=+0.0000  conf=0.62  — CS_panel d=2026-05-14 α=+0.000 regime=MEAN_REV | MEAN_REV | MR mean_rsi_z ic=-0.001 off | - **mom20:…
  combined reasoning: CS_panel d=2026-05-14 α=+0.000 regime=MEAN_REV | MEAN_REV | MR mean_rsi_z ic=-0.001 off | - **mom20:** IC=-0.0533  enabled=True  invert=True  (off if |IC|<0.02) - **mom60:** IC=-0.0217  enabled=True  invert=True  (off if |IC|<0.02) - **d…
```

### 2026-05-14 `MA` → BUY (fwd 5d=n/a)
```
TradeSignal MA → BUY
  raw_score=+0.90630   confidence=0.620   position_weight=0.5014   agents=1
  contributing partials:
    · technical_cs  score=+0.9063  conf=0.62  — CS_panel d=2026-05-14 α=+0.906 regime=TREND | TREND | TREND mom20:ic=-0.053×-1; mom60:ic=-0.022×-1; …
  combined reasoning: CS_panel d=2026-05-14 α=+0.906 regime=TREND | TREND | TREND mom20:ic=-0.053×-1; mom60:ic=-0.022×-1; dist_ma:ic=-0.043×-1; rev5:ic=+0.025×+1 | - **mom20:** IC=-0.0533  enabled=True  invert=True  (off if |IC|<0.02) - **mom60:** IC=-0.0217 …
```

### 2026-05-14 `META` → HOLD (fwd 5d=n/a)
```
TradeSignal META → HOLD
  raw_score=+0.31950   confidence=0.248   position_weight=0.0000   agents=1
  contributing partials:
    · technical_cs  score=+0.3195  conf=0.25  — CS_panel d=2026-05-14 α=+0.319 regime=HIGH_VOL | HIGH_VOL | HIGH_VOL vol_adj ic=+0.071×+1 | - **mom2…
  combined reasoning: CS_panel d=2026-05-14 α=+0.319 regime=HIGH_VOL | HIGH_VOL | HIGH_VOL vol_adj ic=+0.071×+1 | - **mom20:** IC=-0.0533  enabled=True  invert=True  (off if |IC|<0.02) - **mom60:** IC=-0.0217  enabled=True  invert=True  (off if |IC|<0.02) - *…
```

### 2026-05-14 `MRK` → HOLD (fwd 5d=n/a)
```
TradeSignal MRK → HOLD
  raw_score=+0.27500   confidence=0.620   position_weight=0.0000   agents=1
  contributing partials:
    · technical_cs  score=+0.2750  conf=0.62  — CS_panel d=2026-05-14 α=+0.275 regime=TREND | TREND | TREND mom20:ic=-0.053×-1; mom60:ic=-0.022×-1; …
  combined reasoning: CS_panel d=2026-05-14 α=+0.275 regime=TREND | TREND | TREND mom20:ic=-0.053×-1; mom60:ic=-0.022×-1; dist_ma:ic=-0.043×-1; rev5:ic=+0.025×+1 | - **mom20:** IC=-0.0533  enabled=True  invert=True  (off if |IC|<0.02) - **mom60:** IC=-0.0217 …
```

### 2026-05-14 `MSFT` → BUY (fwd 5d=n/a)
```
TradeSignal MSFT → BUY
  raw_score=+0.74010   confidence=0.620   position_weight=0.4788   agents=1
  contributing partials:
    · technical_cs  score=+0.7401  conf=0.62  — CS_panel d=2026-05-14 α=+0.740 regime=TREND | TREND | TREND mom20:ic=-0.053×-1; mom60:ic=-0.022×-1; …
  combined reasoning: CS_panel d=2026-05-14 α=+0.740 regime=TREND | TREND | TREND mom20:ic=-0.053×-1; mom60:ic=-0.022×-1; dist_ma:ic=-0.043×-1; rev5:ic=+0.025×+1 | - **mom20:** IC=-0.0533  enabled=True  invert=True  (off if |IC|<0.02) - **mom60:** IC=-0.0217 …
```

### 2026-05-14 `NVDA` → BUY (fwd 5d=n/a)
```
TradeSignal NVDA → BUY
  raw_score=+1.39540   confidence=0.248   position_weight=0.5680   agents=1
  contributing partials:
    · technical_cs  score=+1.3954  conf=0.25  — CS_panel d=2026-05-14 α=+1.395 regime=HIGH_VOL | HIGH_VOL | HIGH_VOL vol_adj ic=+0.071×+1 | - **mom2…
  combined reasoning: CS_panel d=2026-05-14 α=+1.395 regime=HIGH_VOL | HIGH_VOL | HIGH_VOL vol_adj ic=+0.071×+1 | - **mom20:** IC=-0.0533  enabled=True  invert=True  (off if |IC|<0.02) - **mom60:** IC=-0.0217  enabled=True  invert=True  (off if |IC|<0.02) - *…
```

### 2026-05-14 `PEP` → HOLD (fwd 5d=n/a)
```
TradeSignal PEP → HOLD
  raw_score=+0.00000   confidence=0.620   position_weight=0.0000   agents=1
  contributing partials:
    · technical_cs  score=+0.0000  conf=0.62  — CS_panel d=2026-05-14 α=+0.000 regime=MEAN_REV | MEAN_REV | MR mean_rsi_z ic=-0.001 off | - **mom20:…
  combined reasoning: CS_panel d=2026-05-14 α=+0.000 regime=MEAN_REV | MEAN_REV | MR mean_rsi_z ic=-0.001 off | - **mom20:** IC=-0.0533  enabled=True  invert=True  (off if |IC|<0.02) - **mom60:** IC=-0.0217  enabled=True  invert=True  (off if |IC|<0.02) - **d…
```

### 2026-05-14 `PG` → HOLD (fwd 5d=n/a)
```
TradeSignal PG → HOLD
  raw_score=+0.00000   confidence=0.620   position_weight=0.0000   agents=1
  contributing partials:
    · technical_cs  score=+0.0000  conf=0.62  — CS_panel d=2026-05-14 α=+0.000 regime=MEAN_REV | MEAN_REV | MR mean_rsi_z ic=-0.001 off | - **mom20:…
  combined reasoning: CS_panel d=2026-05-14 α=+0.000 regime=MEAN_REV | MEAN_REV | MR mean_rsi_z ic=-0.001 off | - **mom20:** IC=-0.0533  enabled=True  invert=True  (off if |IC|<0.02) - **mom60:** IC=-0.0217  enabled=True  invert=True  (off if |IC|<0.02) - **d…
```

### 2026-05-14 `TSLA` → SELL (fwd 5d=n/a)
```
TradeSignal TSLA → SELL
  raw_score=-0.86700   confidence=0.620   position_weight=0.4400   agents=1
  contributing partials:
    · technical_cs  score=-0.8670  conf=0.62  — CS_panel d=2026-05-14 α=-0.867 regime=TREND | TREND | TREND mom20:ic=-0.053×-1; mom60:ic=-0.022×-1; …
  combined reasoning: CS_panel d=2026-05-14 α=-0.867 regime=TREND | TREND | TREND mom20:ic=-0.053×-1; mom60:ic=-0.022×-1; dist_ma:ic=-0.043×-1; rev5:ic=+0.025×+1 | - **mom20:** IC=-0.0533  enabled=True  invert=True  (off if |IC|<0.02) - **mom60:** IC=-0.0217 …
```

### 2026-05-14 `UNH` → SELL (fwd 5d=n/a)
```
TradeSignal UNH → SELL
  raw_score=-1.89510   confidence=0.620   position_weight=0.5800   agents=1
  contributing partials:
    · technical_cs  score=-1.8951  conf=0.62  — CS_panel d=2026-05-14 α=-1.895 regime=TREND | TREND | TREND mom20:ic=-0.053×-1; mom60:ic=-0.022×-1; …
  combined reasoning: CS_panel d=2026-05-14 α=-1.895 regime=TREND | TREND | TREND mom20:ic=-0.053×-1; mom60:ic=-0.022×-1; dist_ma:ic=-0.043×-1; rev5:ic=+0.025×+1 | - **mom20:** IC=-0.0533  enabled=True  invert=True  (off if |IC|<0.02) - **mom60:** IC=-0.0217 …
```

### 2026-05-14 `V` → HOLD (fwd 5d=n/a)
```
TradeSignal V → HOLD
  raw_score=+0.00000   confidence=0.620   position_weight=0.0000   agents=1
  contributing partials:
    · technical_cs  score=+0.0000  conf=0.62  — CS_panel d=2026-05-14 α=+0.000 regime=MEAN_REV | MEAN_REV | MR mean_rsi_z ic=-0.001 off | - **mom20:…
  combined reasoning: CS_panel d=2026-05-14 α=+0.000 regime=MEAN_REV | MEAN_REV | MR mean_rsi_z ic=-0.001 off | - **mom20:** IC=-0.0533  enabled=True  invert=True  (off if |IC|<0.02) - **mom60:** IC=-0.0217  enabled=True  invert=True  (off if |IC|<0.02) - **d…
```

### 2026-05-14 `XOM` → HOLD (fwd 5d=n/a)
```
TradeSignal XOM → HOLD
  raw_score=-0.14370   confidence=0.620   position_weight=0.0000   agents=1
  contributing partials:
    · technical_cs  score=-0.1437  conf=0.62  — CS_panel d=2026-05-14 α=-0.144 regime=TREND | TREND | TREND mom20:ic=-0.053×-1; mom60:ic=-0.022×-1; …
  combined reasoning: CS_panel d=2026-05-14 α=-0.144 regime=TREND | TREND | TREND mom20:ic=-0.053×-1; mom60:ic=-0.022×-1; dist_ma:ic=-0.043×-1; rev5:ic=+0.025×+1 | - **mom20:** IC=-0.0533  enabled=True  invert=True  (off if |IC|<0.02) - **mom60:** IC=-0.0217 …
```

---

_Replay: cross-sectional panel alpha (`orchestrator/cs_technical.py`) unless `ALPHAGENT_BACKTEST_CS_PANEL=0` (legacy per-bar orchestrator path)._