# AlphaAgent — pipeline run summary

| Field | Value |
|-------|-------|
| Run start (UTC) | `2026-05-15T09:11:37+00:00` |
| Run end (UTC) | `2026-05-15T09:15:15+00:00` |
| Duration | **218.1 s** |
| Tickers | AAPL, MSFT, GOOGL, AMZN, META, NVDA, TSLA, JPM, V, JNJ, WMT, PG, MA, UNH, HD, DIS, BAC, XOM, CVX, COST |

## Configuration (from environment)

- `HF_TOKEN` / Hub token: **set**
- `FRED_API_KEY`: **not set**
- `ALPHAGENT_DEBUG_AGENTS` = `1`
- `ALPHAGENT_FORM4_FETCH` = `1`

## Orchestrator counters

| Metric | Value |
|--------|-------|
| Events Processed | 825 |
| Signals Emitted | 825 |
| Ttl Forced | 0 |

## Fused `TradeSignal` directions

| Direction | Count |
|-----------|-------|
| BUY | 98 |
| SELL | 67 |
| HOLD | 660 |

## Trade signals (chronological)

### 1. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.84)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.84) | [macro] Calm backdrop (VIX≈18.7)
```

### 2. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.80)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.80) | [macro] Calm backdrop (VIX≈18.7)
```

### 3. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 4. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.82)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.82) | [macro] Calm backdrop (VIX≈18.7)
```

### 5. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.51)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.51) | [macro] Calm backdrop (VIX≈18.7)
```

### 6. `AAPL` → **SELL**  (raw_score=-0.9426, conf=0.805, pos_w=0.580, agents=2)

```
TradeSignal AAPL → SELL
  raw_score=-0.94260   confidence=0.805   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.9670  conf=0.89  — FinBERT NEGATIVE (p=0.97)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.97) | [macro] Calm backdrop (VIX≈18.7)
```

### 7. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 8. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.82)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.82) | [macro] Calm backdrop (VIX≈18.7)
```

### 9. `AAPL` → **SELL**  (raw_score=-0.7832, conf=0.760, pos_w=0.580, agents=2)

```
TradeSignal AAPL → SELL
  raw_score=-0.78320   confidence=0.760   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.8014  conf=0.83  — FinBERT NEGATIVE (p=0.80)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.80) | [macro] Calm backdrop (VIX≈18.7)
```

### 10. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 11. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.75)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.75) | [macro] Calm backdrop (VIX≈18.7)
```

### 12. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 13. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.85)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.85) | [macro] Calm backdrop (VIX≈18.7)
```

### 14. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.66)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.66) | [macro] Calm backdrop (VIX≈18.7)
```

### 15. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.81)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.81) | [macro] Calm backdrop (VIX≈18.7)
```

### 16. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 17. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 18. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 19. `AAPL` → **BUY**  (raw_score=+0.8410, conf=0.776, pos_w=0.580, agents=2)

```
TradeSignal AAPL → BUY
  raw_score=+0.84100   confidence=0.776   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.8592  conf=0.85  — FinBERT POSITIVE (p=0.86)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.86) | [macro] Calm backdrop (VIX≈18.7)
```

### 20. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 21. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.76)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.76) | [macro] Calm backdrop (VIX≈18.7)
```

### 22. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.83)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.83) | [macro] Calm backdrop (VIX≈18.7)
```

### 23. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 24. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 25. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 26. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 27. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 28. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.81)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.81) | [macro] Calm backdrop (VIX≈18.7)
```

### 29. `AAPL` → **SELL**  (raw_score=-0.7745, conf=0.757, pos_w=0.573, agents=2)

```
TradeSignal AAPL → SELL
  raw_score=-0.77450   confidence=0.757   position_weight=0.5726   agents=2
  contributing partials:
    · sentiment     score=-0.7923  conf=0.83  — FinBERT NEGATIVE (p=0.79)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.79) | [macro] Calm backdrop (VIX≈18.7)
```

### 30. `AAPL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.68)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.68) | [macro] Calm backdrop (VIX≈18.7)
```

### 31. `AAPL` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 32. `AAPL` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 33. `AAPL` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈85.1 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈85.1 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 34. `AAPL` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈94.4 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈94.4 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 35. `AAPL` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈85.7 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈85.7 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 36. `MSFT` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 37. `MSFT` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 38. `MSFT` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈0.0 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈0.0 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 39. `MSFT` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈0.0 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈0.0 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 40. `MSFT` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈29.9 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈29.9 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 41. `GOOGL` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 42. `GOOGL` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 43. `GOOGL` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈0.0 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈0.0 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 44. `GOOGL` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈53.2 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈53.2 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 45. `GOOGL` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈50.4 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈50.4 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 46. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 47. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.71)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.71) | [macro] Calm backdrop (VIX≈18.7)
```

### 48. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 49. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 50. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.84)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.84) | [macro] Calm backdrop (VIX≈18.7)
```

### 51. `MSFT` → **SELL**  (raw_score=-0.8907, conf=0.790, pos_w=0.580, agents=2)

```
TradeSignal MSFT → SELL
  raw_score=-0.89070   confidence=0.790   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.9132  conf=0.87  — FinBERT NEGATIVE (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 52. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 53. `MSFT` → **SELL**  (raw_score=-0.9426, conf=0.805, pos_w=0.580, agents=2)

```
TradeSignal MSFT → SELL
  raw_score=-0.94260   confidence=0.805   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.9670  conf=0.89  — FinBERT NEGATIVE (p=0.97)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.97) | [macro] Calm backdrop (VIX≈18.7)
```

### 54. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 55. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 56. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.65)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.65) | [macro] Calm backdrop (VIX≈18.7)
```

### 57. `MSFT` → **SELL**  (raw_score=-0.8505, conf=0.779, pos_w=0.580, agents=2)

```
TradeSignal MSFT → SELL
  raw_score=-0.85050   confidence=0.779   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.8715  conf=0.86  — FinBERT NEGATIVE (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 58. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.84)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.84) | [macro] Calm backdrop (VIX≈18.7)
```

### 59. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.71)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.71) | [macro] Calm backdrop (VIX≈18.7)
```

### 60. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 61. `MSFT` → **BUY**  (raw_score=+0.9280, conf=0.800, pos_w=0.580, agents=2)

```
TradeSignal MSFT → BUY
  raw_score=+0.92800   confidence=0.800   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.9495  conf=0.88  — FinBERT POSITIVE (p=0.95)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.95) | [macro] Calm backdrop (VIX≈18.7)
```

### 62. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.95)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.95) | [macro] Calm backdrop (VIX≈18.7)
```

### 63. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 64. `MSFT` → **BUY**  (raw_score=+0.8346, conf=0.774, pos_w=0.580, agents=2)

```
TradeSignal MSFT → BUY
  raw_score=+0.83460   confidence=0.774   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.8525  conf=0.85  — FinBERT POSITIVE (p=0.85)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.85) | [macro] Calm backdrop (VIX≈18.7)
```

### 65. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.55)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.55) | [macro] Calm backdrop (VIX≈18.7)
```

### 66. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.65)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.65) | [macro] Calm backdrop (VIX≈18.7)
```

### 67. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 68. `MSFT` → **SELL**  (raw_score=-0.5073, conf=0.680, pos_w=0.318, agents=2)

```
TradeSignal MSFT → SELL
  raw_score=-0.50730   confidence=0.680   position_weight=0.3179   agents=2
  contributing partials:
    · sentiment     score=-0.5127  conf=0.73  — FinBERT NEGATIVE (p=0.51)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.51) | [macro] Calm backdrop (VIX≈18.7)
```

### 69. `MSFT` → **BUY**  (raw_score=+0.7153, conf=0.740, pos_w=0.512, agents=2)

```
TradeSignal MSFT → BUY
  raw_score=+0.71530   confidence=0.740   position_weight=0.5119   agents=2
  contributing partials:
    · sentiment     score=+0.7281  conf=0.80  — FinBERT POSITIVE (p=0.73)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.73) | [macro] Calm backdrop (VIX≈18.7)
```

### 70. `MSFT` → **SELL**  (raw_score=-0.8688, conf=0.784, pos_w=0.580, agents=2)

```
TradeSignal MSFT → SELL
  raw_score=-0.86880   confidence=0.784   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.8904  conf=0.86  — FinBERT NEGATIVE (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 71. `MSFT` → **BUY**  (raw_score=+0.5219, conf=0.684, pos_w=0.330, agents=2)

```
TradeSignal MSFT → BUY
  raw_score=+0.52190   confidence=0.684   position_weight=0.3304   agents=2
  contributing partials:
    · sentiment     score=+0.5252  conf=0.73  — FinBERT POSITIVE (p=0.53)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.53) | [macro] Calm backdrop (VIX≈18.7)
```

### 72. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.75)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.75) | [macro] Calm backdrop (VIX≈18.7)
```

### 73. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 74. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.79)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.79) | [macro] Calm backdrop (VIX≈18.7)
```

### 75. `MSFT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 76. `AMZN` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 77. `AMZN` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 78. `AMZN` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈0.0 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈0.0 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 79. `AMZN` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈38.6 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈38.6 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 80. `AMZN` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈30.6 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈30.6 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 81. `META` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 82. `META` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 83. `META` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈27.8 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈27.8 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 84. `META` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈62.3 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈62.3 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 85. `META` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈64.5 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈64.5 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 86. `NVDA` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 87. `NVDA` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 88. `NVDA` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈100.0 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈100.0 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 89. `NVDA` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈100.0 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈100.0 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 90. `NVDA` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈100.0 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈100.0 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 91. `GOOGL` → **SELL**  (raw_score=-0.9174, conf=0.798, pos_w=0.580, agents=2)

```
TradeSignal GOOGL → SELL
  raw_score=-0.91740   confidence=0.798   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.9408  conf=0.88  — FinBERT NEGATIVE (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 92. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.80)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.80) | [macro] Calm backdrop (VIX≈18.7)
```

### 93. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.51)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.51) | [macro] Calm backdrop (VIX≈18.7)
```

### 94. `GOOGL` → **SELL**  (raw_score=-0.7832, conf=0.760, pos_w=0.580, agents=2)

```
TradeSignal GOOGL → SELL
  raw_score=-0.78320   confidence=0.760   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.8014  conf=0.83  — FinBERT NEGATIVE (p=0.80)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.80) | [macro] Calm backdrop (VIX≈18.7)
```

### 95. `GOOGL` → **SELL**  (raw_score=-0.7554, conf=0.752, pos_w=0.553, agents=2)

```
TradeSignal GOOGL → SELL
  raw_score=-0.75540   confidence=0.752   position_weight=0.5529   agents=2
  contributing partials:
    · sentiment     score=-0.7725  conf=0.82  — FinBERT NEGATIVE (p=0.77)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.77) | [macro] Calm backdrop (VIX≈18.7)
```

### 96. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 97. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.84)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.84) | [macro] Calm backdrop (VIX≈18.7)
```

### 98. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 99. `GOOGL` → **BUY**  (raw_score=+0.6404, conf=0.718, pos_w=0.439, agents=2)

```
TradeSignal GOOGL → BUY
  raw_score=+0.64040   confidence=0.718   position_weight=0.4389   agents=2
  contributing partials:
    · sentiment     score=+0.6498  conf=0.78  — FinBERT POSITIVE (p=0.65)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.65) | [macro] Calm backdrop (VIX≈18.7)
```

### 100. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 101. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 102. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.84)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.84) | [macro] Calm backdrop (VIX≈18.7)
```

### 103. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.73)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.73) | [macro] Calm backdrop (VIX≈18.7)
```

### 104. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 105. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 106. `GOOGL` → **SELL**  (raw_score=-0.6711, conf=0.728, pos_w=0.469, agents=2)

```
TradeSignal GOOGL → SELL
  raw_score=-0.67110   confidence=0.728   position_weight=0.4688   agents=2
  contributing partials:
    · sentiment     score=-0.6845  conf=0.79  — FinBERT NEGATIVE (p=0.68)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.68) | [macro] Calm backdrop (VIX≈18.7)
```

### 107. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.79)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.79) | [macro] Calm backdrop (VIX≈18.7)
```

### 108. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.70)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.70) | [macro] Calm backdrop (VIX≈18.7)
```

### 109. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 110. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 111. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 112. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 113. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.73)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.73) | [macro] Calm backdrop (VIX≈18.7)
```

### 114. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 115. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 116. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 117. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 118. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 119. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.81)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.81) | [macro] Calm backdrop (VIX≈18.7)
```

### 120. `GOOGL` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 121. `TSLA` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 122. `TSLA` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 123. `TSLA` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈59.0 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈59.0 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 124. `TSLA` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈71.1 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈71.1 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 125. `TSLA` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈67.8 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈67.8 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 126. `JPM` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 127. `JPM` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 128. `JPM` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈69.9 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈69.9 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 129. `JPM` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈42.0 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈42.0 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 130. `JPM` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈40.8 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈40.8 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 131. `V` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 132. `V` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 133. `V` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈100.0 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈100.0 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 134. `V` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈57.6 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈57.6 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 135. `V` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈63.2 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈63.2 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 136. `AMZN` → **SELL**  (raw_score=-0.9174, conf=0.798, pos_w=0.580, agents=2)

```
TradeSignal AMZN → SELL
  raw_score=-0.91740   confidence=0.798   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.9408  conf=0.88  — FinBERT NEGATIVE (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 137. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 138. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.80)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.80) | [macro] Calm backdrop (VIX≈18.7)
```

### 139. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 140. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.85)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.85) | [macro] Calm backdrop (VIX≈18.7)
```

### 141. `AMZN` → **BUY**  (raw_score=+0.6626, conf=0.724, pos_w=0.460, agents=2)

```
TradeSignal AMZN → BUY
  raw_score=+0.66260   confidence=0.724   position_weight=0.4601   agents=2
  contributing partials:
    · sentiment     score=+0.6730  conf=0.79  — FinBERT POSITIVE (p=0.67)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.67) | [macro] Calm backdrop (VIX≈18.7)
```

### 142. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 143. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 144. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 145. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.76)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.76) | [macro] Calm backdrop (VIX≈18.7)
```

### 146. `AMZN` → **SELL**  (raw_score=-0.5073, conf=0.680, pos_w=0.318, agents=2)

```
TradeSignal AMZN → SELL
  raw_score=-0.50730   confidence=0.680   position_weight=0.3179   agents=2
  contributing partials:
    · sentiment     score=-0.5127  conf=0.73  — FinBERT NEGATIVE (p=0.51)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.51) | [macro] Calm backdrop (VIX≈18.7)
```

### 147. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 148. `AMZN` → **SELL**  (raw_score=-0.5787, conf=0.701, pos_w=0.382, agents=2)

```
TradeSignal AMZN → SELL
  raw_score=-0.57870   confidence=0.701   position_weight=0.3816   agents=2
  contributing partials:
    · sentiment     score=-0.5877  conf=0.76  — FinBERT NEGATIVE (p=0.59)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.59) | [macro] Calm backdrop (VIX≈18.7)
```

### 149. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.85)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.85) | [macro] Calm backdrop (VIX≈18.7)
```

### 150. `AMZN` → **SELL**  (raw_score=-0.9182, conf=0.798, pos_w=0.580, agents=2)

```
TradeSignal AMZN → SELL
  raw_score=-0.91820   confidence=0.798   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.9417  conf=0.88  — FinBERT NEGATIVE (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 151. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 152. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 153. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.86)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.86) | [macro] Calm backdrop (VIX≈18.7)
```

### 154. `AMZN` → **SELL**  (raw_score=-0.6711, conf=0.728, pos_w=0.469, agents=2)

```
TradeSignal AMZN → SELL
  raw_score=-0.67110   confidence=0.728   position_weight=0.4688   agents=2
  contributing partials:
    · sentiment     score=-0.6845  conf=0.79  — FinBERT NEGATIVE (p=0.68)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.68) | [macro] Calm backdrop (VIX≈18.7)
```

### 155. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.79)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.79) | [macro] Calm backdrop (VIX≈18.7)
```

### 156. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.70)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.70) | [macro] Calm backdrop (VIX≈18.7)
```

### 157. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 158. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 159. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 160. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 161. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 162. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 163. `AMZN` → **SELL**  (raw_score=-0.8071, conf=0.767, pos_w=0.580, agents=2)

```
TradeSignal AMZN → SELL
  raw_score=-0.80710   confidence=0.767   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.8263  conf=0.84  — FinBERT NEGATIVE (p=0.83)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.83) | [macro] Calm backdrop (VIX≈18.7)
```

### 164. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.73)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.73) | [macro] Calm backdrop (VIX≈18.7)
```

### 165. `AMZN` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 166. `JNJ` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 167. `JNJ` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 168. `JNJ` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈100.0 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈100.0 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 169. `JNJ` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈100.0 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈100.0 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 170. `JNJ` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈100.0 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈100.0 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 171. `WMT` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 172. `WMT` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 173. `WMT` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈49.3 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈49.3 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 174. `WMT` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈57.7 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈57.7 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 175. `WMT` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈63.2 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈63.2 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 176. `PG` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 177. `PG` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 178. `PG` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈15.2 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈15.2 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 179. `PG` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈10.4 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈10.4 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 180. `PG` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈17.7 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈17.7 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 181. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.81)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.81) | [macro] Calm backdrop (VIX≈18.7)
```

### 182. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.81)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.81) | [macro] Calm backdrop (VIX≈18.7)
```

### 183. `META` → **SELL**  (raw_score=-0.5174, conf=0.683, pos_w=0.327, agents=2)

```
TradeSignal META → SELL
  raw_score=-0.51740   confidence=0.683   position_weight=0.3267   agents=2
  contributing partials:
    · sentiment     score=-0.5232  conf=0.73  — FinBERT NEGATIVE (p=0.52)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.52) | [macro] Calm backdrop (VIX≈18.7)
```

### 184. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 185. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 186. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 187. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.76)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.76) | [macro] Calm backdrop (VIX≈18.7)
```

### 188. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.51)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.51) | [macro] Calm backdrop (VIX≈18.7)
```

### 189. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 190. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.78)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.78) | [macro] Calm backdrop (VIX≈18.7)
```

### 191. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.84)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.84) | [macro] Calm backdrop (VIX≈18.7)
```

### 192. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 193. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 194. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 195. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 196. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 197. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 198. `META` → **BUY**  (raw_score=+0.5819, conf=0.701, pos_w=0.384, agents=2)

```
TradeSignal META → BUY
  raw_score=+0.58190   confidence=0.701   position_weight=0.3842   agents=2
  contributing partials:
    · sentiment     score=+0.5883  conf=0.76  — FinBERT POSITIVE (p=0.59)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.59) | [macro] Calm backdrop (VIX≈18.7)
```

### 199. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 200. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.76)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.76) | [macro] Calm backdrop (VIX≈18.7)
```

### 201. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 202. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 203. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.80)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.80) | [macro] Calm backdrop (VIX≈18.7)
```

### 204. `META` → **SELL**  (raw_score=-0.7886, conf=0.761, pos_w=0.580, agents=2)

```
TradeSignal META → SELL
  raw_score=-0.78860   confidence=0.761   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.8071  conf=0.83  — FinBERT NEGATIVE (p=0.81)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.81) | [macro] Calm backdrop (VIX≈18.7)
```

### 205. `META` → **SELL**  (raw_score=-0.8611, conf=0.782, pos_w=0.580, agents=2)

```
TradeSignal META → SELL
  raw_score=-0.86110   confidence=0.782   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.8824  conf=0.86  — FinBERT NEGATIVE (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 206. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.65)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.65) | [macro] Calm backdrop (VIX≈18.7)
```

### 207. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.84)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.84) | [macro] Calm backdrop (VIX≈18.7)
```

### 208. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.60)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.60) | [macro] Calm backdrop (VIX≈18.7)
```

### 209. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.75)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.75) | [macro] Calm backdrop (VIX≈18.7)
```

### 210. `META` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal META → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 211. `MA` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 212. `MA` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 213. `MA` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈100.0 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈100.0 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 214. `MA` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈32.1 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈32.1 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 215. `MA` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈30.5 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈30.5 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 216. `UNH` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 217. `UNH` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 218. `UNH` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈100.0 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈100.0 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 219. `UNH` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈100.0 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈100.0 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 220. `UNH` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈91.1 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈91.1 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 221. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.55)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.55) | [macro] Calm backdrop (VIX≈18.7)
```

### 222. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.72)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.72) | [macro] Calm backdrop (VIX≈18.7)
```

### 223. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.78)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.78) | [macro] Calm backdrop (VIX≈18.7)
```

### 224. `NVDA` → **SELL**  (raw_score=-0.8108, conf=0.768, pos_w=0.580, agents=2)

```
TradeSignal NVDA → SELL
  raw_score=-0.81080   confidence=0.768   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.8302  conf=0.84  — FinBERT NEGATIVE (p=0.83)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.83) | [macro] Calm backdrop (VIX≈18.7)
```

### 225. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.85)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.85) | [macro] Calm backdrop (VIX≈18.7)
```

### 226. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 227. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.74)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.74) | [macro] Calm backdrop (VIX≈18.7)
```

### 228. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 229. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 230. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.95)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.95) | [macro] Calm backdrop (VIX≈18.7)
```

### 231. `NVDA` → **SELL**  (raw_score=-0.6064, conf=0.709, pos_w=0.407, agents=2)

```
TradeSignal NVDA → SELL
  raw_score=-0.60640   confidence=0.709   position_weight=0.4072   agents=2
  contributing partials:
    · sentiment     score=-0.6167  conf=0.77  — FinBERT NEGATIVE (p=0.62)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.62) | [macro] Calm backdrop (VIX≈18.7)
```

### 232. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 233. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 234. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 235. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.66)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.66) | [macro] Calm backdrop (VIX≈18.7)
```

### 236. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 237. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 238. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 239. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 240. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.50)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.50) | [macro] Calm backdrop (VIX≈18.7)
```

### 241. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 242. `NVDA` → **SELL**  (raw_score=-0.8923, conf=0.791, pos_w=0.580, agents=2)

```
TradeSignal NVDA → SELL
  raw_score=-0.89230   confidence=0.791   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.9148  conf=0.87  — FinBERT NEGATIVE (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 243. `NVDA` → **SELL**  (raw_score=-0.9491, conf=0.807, pos_w=0.580, agents=2)

```
TradeSignal NVDA → SELL
  raw_score=-0.94910   confidence=0.807   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.9738  conf=0.89  — FinBERT NEGATIVE (p=0.97)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.97) | [macro] Calm backdrop (VIX≈18.7)
```

### 244. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 245. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 246. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.84)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.84) | [macro] Calm backdrop (VIX≈18.7)
```

### 247. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 248. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.63)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.63) | [macro] Calm backdrop (VIX≈18.7)
```

### 249. `NVDA` → **BUY**  (raw_score=+0.5226, conf=0.684, pos_w=0.331, agents=2)

```
TradeSignal NVDA → BUY
  raw_score=+0.52260   confidence=0.684   position_weight=0.3310   agents=2
  contributing partials:
    · sentiment     score=+0.5260  conf=0.73  — FinBERT POSITIVE (p=0.53)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.53) | [macro] Calm backdrop (VIX≈18.7)
```

### 250. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 251. `HD` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 252. `HD` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 253. `HD` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈0.0 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈0.0 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 254. `HD` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈0.0 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈0.0 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 255. `HD` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈10.8 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈10.8 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 256. `DIS` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 257. `DIS` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 258. `DIS` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈30.4 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈30.4 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 259. `DIS` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈24.0 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈24.0 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 260. `DIS` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈30.1 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈30.1 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 261. `BAC` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 262. `BAC` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 263. `BAC` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈23.2 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈23.2 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 264. `BAC` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈11.9 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈11.9 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 265. `BAC` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈12.4 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈12.4 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 266. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 267. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.85)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.85) | [macro] Calm backdrop (VIX≈18.7)
```

### 268. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.85)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.85) | [macro] Calm backdrop (VIX≈18.7)
```

### 269. `TSLA` → **BUY**  (raw_score=+0.7090, conf=0.738, pos_w=0.506, agents=2)

```
TradeSignal TSLA → BUY
  raw_score=+0.70900   confidence=0.738   position_weight=0.5056   agents=2
  contributing partials:
    · sentiment     score=+0.7215  conf=0.80  — FinBERT POSITIVE (p=0.72)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.72) | [macro] Calm backdrop (VIX≈18.7)
```

### 270. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 271. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 272. `TSLA` → **SELL**  (raw_score=-0.5950, conf=0.706, pos_w=0.397, agents=2)

```
TradeSignal TSLA → SELL
  raw_score=-0.59500   confidence=0.706   position_weight=0.3966   agents=2
  contributing partials:
    · sentiment     score=-0.6048  conf=0.76  — FinBERT NEGATIVE (p=0.60)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.60) | [macro] Calm backdrop (VIX≈18.7)
```

### 273. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 274. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.65)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.65) | [macro] Calm backdrop (VIX≈18.7)
```

### 275. `TSLA` → **SELL**  (raw_score=-0.9247, conf=0.800, pos_w=0.580, agents=2)

```
TradeSignal TSLA → SELL
  raw_score=-0.92470   confidence=0.800   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.9485  conf=0.88  — FinBERT NEGATIVE (p=0.95)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.95) | [macro] Calm backdrop (VIX≈18.7)
```

### 276. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 277. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 278. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 279. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.82)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.82) | [macro] Calm backdrop (VIX≈18.7)
```

### 280. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 281. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 282. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 283. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 284. `TSLA` → **SELL**  (raw_score=-0.8727, conf=0.785, pos_w=0.580, agents=2)

```
TradeSignal TSLA → SELL
  raw_score=-0.87270   confidence=0.785   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.8945  conf=0.86  — FinBERT NEGATIVE (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 285. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 286. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 287. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 288. `TSLA` → **SELL**  (raw_score=-0.8118, conf=0.768, pos_w=0.580, agents=2)

```
TradeSignal TSLA → SELL
  raw_score=-0.81180   confidence=0.768   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.8312  conf=0.84  — FinBERT NEGATIVE (p=0.83)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.83) | [macro] Calm backdrop (VIX≈18.7)
```

### 289. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.83)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.83) | [macro] Calm backdrop (VIX≈18.7)
```

### 290. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.75)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.75) | [macro] Calm backdrop (VIX≈18.7)
```

### 291. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 292. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 293. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 294. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.86)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.86) | [macro] Calm backdrop (VIX≈18.7)
```

### 295. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 296. `XOM` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 297. `XOM` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 298. `XOM` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈100.0 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈100.0 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 299. `XOM` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈100.0 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈100.0 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 300. `XOM` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈100.0 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈100.0 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 301. `AAPL` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 302. `JPM` → **SELL**  (raw_score=-0.9389, conf=0.804, pos_w=0.580, agents=2)

```
TradeSignal JPM → SELL
  raw_score=-0.93890   confidence=0.804   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.9632  conf=0.89  — FinBERT NEGATIVE (p=0.96)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.96) | [macro] Calm backdrop (VIX≈18.7)
```

### 303. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 304. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.56)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.56) | [macro] Calm backdrop (VIX≈18.7)
```

### 305. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.62)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.62) | [macro] Calm backdrop (VIX≈18.7)
```

### 306. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.83)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.83) | [macro] Calm backdrop (VIX≈18.7)
```

### 307. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 308. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.86)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.86) | [macro] Calm backdrop (VIX≈18.7)
```

### 309. `JPM` → **SELL**  (raw_score=-0.8366, conf=0.775, pos_w=0.580, agents=2)

```
TradeSignal JPM → SELL
  raw_score=-0.83660   confidence=0.775   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.8570  conf=0.85  — FinBERT NEGATIVE (p=0.86)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.86) | [macro] Calm backdrop (VIX≈18.7)
```

### 310. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 311. `JPM` → **BUY**  (raw_score=+0.9239, conf=0.799, pos_w=0.580, agents=2)

```
TradeSignal JPM → BUY
  raw_score=+0.92390   confidence=0.799   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.9453  conf=0.88  — FinBERT POSITIVE (p=0.95)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.95) | [macro] Calm backdrop (VIX≈18.7)
```

### 312. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.84)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.84) | [macro] Calm backdrop (VIX≈18.7)
```

### 313. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.84)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.84) | [macro] Calm backdrop (VIX≈18.7)
```

### 314. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.79)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.79) | [macro] Calm backdrop (VIX≈18.7)
```

### 315. `JPM` → **BUY**  (raw_score=+0.4949, conf=0.676, pos_w=0.307, agents=2)

```
TradeSignal JPM → BUY
  raw_score=+0.49490   confidence=0.676   position_weight=0.3068   agents=2
  contributing partials:
    · sentiment     score=+0.4968  conf=0.72  — FinBERT POSITIVE (p=0.50)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.50) | [macro] Calm backdrop (VIX≈18.7)
```

### 316. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 317. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.72)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.72) | [macro] Calm backdrop (VIX≈18.7)
```

### 318. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 319. `JPM` → **BUY**  (raw_score=+0.7181, conf=0.740, pos_w=0.515, agents=2)

```
TradeSignal JPM → BUY
  raw_score=+0.71810   confidence=0.740   position_weight=0.5147   agents=2
  contributing partials:
    · sentiment     score=+0.7310  conf=0.81  — FinBERT POSITIVE (p=0.73)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.73) | [macro] Calm backdrop (VIX≈18.7)
```

### 320. `JPM` → **SELL**  (raw_score=-0.6378, conf=0.718, pos_w=0.437, agents=2)

```
TradeSignal JPM → SELL
  raw_score=-0.63780   confidence=0.718   position_weight=0.4368   agents=2
  contributing partials:
    · sentiment     score=-0.6496  conf=0.78  — FinBERT NEGATIVE (p=0.65)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.65) | [macro] Calm backdrop (VIX≈18.7)
```

### 321. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 322. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.56)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.56) | [macro] Calm backdrop (VIX≈18.7)
```

### 323. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 324. `JPM` → **SELL**  (raw_score=-0.6841, conf=0.731, pos_w=0.482, agents=2)

```
TradeSignal JPM → SELL
  raw_score=-0.68410   confidence=0.731   position_weight=0.4816   agents=2
  contributing partials:
    · sentiment     score=-0.6981  conf=0.79  — FinBERT NEGATIVE (p=0.70)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.70) | [macro] Calm backdrop (VIX≈18.7)
```

### 325. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 326. `JPM` → **SELL**  (raw_score=-0.9431, conf=0.805, pos_w=0.580, agents=2)

```
TradeSignal JPM → SELL
  raw_score=-0.94310   confidence=0.805   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.9675  conf=0.89  — FinBERT NEGATIVE (p=0.97)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.97) | [macro] Calm backdrop (VIX≈18.7)
```

### 327. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 328. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.60)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.60) | [macro] Calm backdrop (VIX≈18.7)
```

### 329. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 330. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.78)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.78) | [macro] Calm backdrop (VIX≈18.7)
```

### 331. `JPM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JPM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.49)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.49) | [macro] Calm backdrop (VIX≈18.7)
```

### 332. `AAPL` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 333. `AAPL` → **HOLD**  (raw_score=+0.0337, conf=0.464, pos_w=0.000, agents=3)

```
TradeSignal AAPL → HOLD
  raw_score=+0.03370   confidence=0.464   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0400  conf=0.35  — 10-Q: periodic disclosure (low directional edge)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 10-Q: periodic disclosure (low directional edge) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 334. `AAPL` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal AAPL → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 335. `CVX` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 336. `CVX` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 337. `CVX` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈100.0 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈100.0 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 338. `CVX` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈100.0 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈100.0 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 339. `CVX` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈100.0 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈100.0 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 340. `AAPL` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 341. `AAPL` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal AAPL → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 342. `COST` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (1/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (1/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 343. `COST` → **HOLD**  (raw_score=+0.0081, conf=0.285, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00810   confidence=0.285   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.22  — Warming price buffer (2/3+ closes for RSI)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming price buffer (2/3+ closes for RSI) | [macro] Calm backdrop (VIX≈18.7)
```

### 344. `COST` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (3/20+ closes; RSI≈70.6 p=2)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (3/20+ closes; RSI≈70.6 p=2) | [macro] Calm backdrop (VIX≈18.7)
```

### 345. `COST` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (4/20+ closes; RSI≈78.3 p=3)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (4/20+ closes; RSI≈78.3 p=3) | [macro] Calm backdrop (VIX≈18.7)
```

### 346. `COST` → **HOLD**  (raw_score=+0.0077, conf=0.300, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00770   confidence=0.300   position_weight=0.0000   agents=2
  contributing partials:
    · technical     score=+0.0000  conf=0.24  — Warming MA trend (5/20+ closes; RSI≈81.8 p=4)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [technical] Warming MA trend (5/20+ closes; RSI≈81.8 p=4) | [macro] Calm backdrop (VIX≈18.7)
```

### 347. `AAPL` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 348. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 349. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 350. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.66)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.66) | [macro] Calm backdrop (VIX≈18.7)
```

### 351. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 352. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.86)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.86) | [macro] Calm backdrop (VIX≈18.7)
```

### 353. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.85)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.85) | [macro] Calm backdrop (VIX≈18.7)
```

### 354. `V` → **SELL**  (raw_score=-0.5809, conf=0.702, pos_w=0.384, agents=2)

```
TradeSignal V → SELL
  raw_score=-0.58090   confidence=0.702   position_weight=0.3837   agents=2
  contributing partials:
    · sentiment     score=-0.5900  conf=0.76  — FinBERT NEGATIVE (p=0.59)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.59) | [macro] Calm backdrop (VIX≈18.7)
```

### 355. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.83)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.83) | [macro] Calm backdrop (VIX≈18.7)
```

### 356. `V` → **BUY**  (raw_score=+0.7875, conf=0.760, pos_w=0.580, agents=2)

```
TradeSignal V → BUY
  raw_score=+0.78750   confidence=0.760   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.8034  conf=0.83  — FinBERT POSITIVE (p=0.80)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.80) | [macro] Calm backdrop (VIX≈18.7)
```

### 357. `V` → **BUY**  (raw_score=+0.6763, conf=0.728, pos_w=0.473, agents=2)

```
TradeSignal V → BUY
  raw_score=+0.67630   confidence=0.728   position_weight=0.4735   agents=2
  contributing partials:
    · sentiment     score=+0.6874  conf=0.79  — FinBERT POSITIVE (p=0.69)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.69) | [macro] Calm backdrop (VIX≈18.7)
```

### 358. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 359. `V` → **SELL**  (raw_score=-0.3954, conf=0.648, pos_w=0.224, agents=2)

```
TradeSignal V → SELL
  raw_score=-0.39540   confidence=0.648   position_weight=0.2244   agents=2
  contributing partials:
    · sentiment     score=-0.3945  conf=0.69  — FinBERT NEGATIVE (p=0.39)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.39) | [macro] Calm backdrop (VIX≈18.7)
```

### 360. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.56)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.56) | [macro] Calm backdrop (VIX≈18.7)
```

### 361. `V` → **SELL**  (raw_score=-0.3954, conf=0.648, pos_w=0.224, agents=2)

```
TradeSignal V → SELL
  raw_score=-0.39540   confidence=0.648   position_weight=0.2244   agents=2
  contributing partials:
    · sentiment     score=-0.3945  conf=0.69  — FinBERT NEGATIVE (p=0.39)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.39) | [macro] Calm backdrop (VIX≈18.7)
```

### 362. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.62)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.62) | [macro] Calm backdrop (VIX≈18.7)
```

### 363. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 364. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 365. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.82)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.82) | [macro] Calm backdrop (VIX≈18.7)
```

### 366. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.73)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.73) | [macro] Calm backdrop (VIX≈18.7)
```

### 367. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 368. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.54)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.54) | [macro] Calm backdrop (VIX≈18.7)
```

### 369. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.85)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.85) | [macro] Calm backdrop (VIX≈18.7)
```

### 370. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.75)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.75) | [macro] Calm backdrop (VIX≈18.7)
```

### 371. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.59)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.59) | [macro] Calm backdrop (VIX≈18.7)
```

### 372. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 373. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 374. `V` → **BUY**  (raw_score=+0.5464, conf=0.691, pos_w=0.352, agents=2)

```
TradeSignal V → BUY
  raw_score=+0.54640   confidence=0.691   position_weight=0.3520   agents=2
  contributing partials:
    · sentiment     score=+0.5510  conf=0.74  — FinBERT POSITIVE (p=0.55)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.55) | [macro] Calm backdrop (VIX≈18.7)
```

### 375. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 376. `V` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal V → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.95)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.95) | [macro] Calm backdrop (VIX≈18.7)
```

### 377. `AAPL` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal AAPL → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 378. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.83)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.83) | [macro] Calm backdrop (VIX≈18.7)
```

### 379. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 380. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.79)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.79) | [macro] Calm backdrop (VIX≈18.7)
```

### 381. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.73)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.73) | [macro] Calm backdrop (VIX≈18.7)
```

### 382. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.84)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.84) | [macro] Calm backdrop (VIX≈18.7)
```

### 383. `JNJ` → **BUY**  (raw_score=+0.6667, conf=0.726, pos_w=0.464, agents=2)

```
TradeSignal JNJ → BUY
  raw_score=+0.66670   confidence=0.726   position_weight=0.4642   agents=2
  contributing partials:
    · sentiment     score=+0.6773  conf=0.79  — FinBERT POSITIVE (p=0.68)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.68) | [macro] Calm backdrop (VIX≈18.7)
```

### 384. `JNJ` → **BUY**  (raw_score=+0.5846, conf=0.702, pos_w=0.387, agents=2)

```
TradeSignal JNJ → BUY
  raw_score=+0.58460   confidence=0.702   position_weight=0.3867   agents=2
  contributing partials:
    · sentiment     score=+0.5912  conf=0.76  — FinBERT POSITIVE (p=0.59)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.59) | [macro] Calm backdrop (VIX≈18.7)
```

### 385. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.78)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.78) | [macro] Calm backdrop (VIX≈18.7)
```

### 386. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 387. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 388. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 389. `JNJ` → **BUY**  (raw_score=+0.5965, conf=0.705, pos_w=0.398, agents=2)

```
TradeSignal JNJ → BUY
  raw_score=+0.59650   confidence=0.705   position_weight=0.3976   agents=2
  contributing partials:
    · sentiment     score=+0.6036  conf=0.76  — FinBERT POSITIVE (p=0.60)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.60) | [macro] Calm backdrop (VIX≈18.7)
```

### 390. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 391. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.74)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.74) | [macro] Calm backdrop (VIX≈18.7)
```

### 392. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 393. `JNJ` → **BUY**  (raw_score=+0.9322, conf=0.802, pos_w=0.580, agents=2)

```
TradeSignal JNJ → BUY
  raw_score=+0.93220   confidence=0.802   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.9539  conf=0.88  — FinBERT POSITIVE (p=0.95)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.95) | [macro] Calm backdrop (VIX≈18.7)
```

### 394. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 395. `JNJ` → **BUY**  (raw_score=+0.8572, conf=0.780, pos_w=0.580, agents=2)

```
TradeSignal JNJ → BUY
  raw_score=+0.85720   confidence=0.780   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.8760  conf=0.86  — FinBERT POSITIVE (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 396. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.85)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.85) | [macro] Calm backdrop (VIX≈18.7)
```

### 397. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.47)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.47) | [macro] Calm backdrop (VIX≈18.7)
```

### 398. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.63)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.63) | [macro] Calm backdrop (VIX≈18.7)
```

### 399. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 400. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 401. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 402. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 403. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 404. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.85)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.85) | [macro] Calm backdrop (VIX≈18.7)
```

### 405. `JNJ` → **SELL**  (raw_score=-0.8199, conf=0.770, pos_w=0.580, agents=2)

```
TradeSignal JNJ → SELL
  raw_score=-0.81990   confidence=0.770   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.8396  conf=0.84  — FinBERT NEGATIVE (p=0.84)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.84) | [macro] Calm backdrop (VIX≈18.7)
```

### 406. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 407. `JNJ` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.84)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.84) | [macro] Calm backdrop (VIX≈18.7)
```

### 408. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.81)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.81) | [macro] Calm backdrop (VIX≈18.7)
```

### 409. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.75)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.75) | [macro] Calm backdrop (VIX≈18.7)
```

### 410. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 411. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.55)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.55) | [macro] Calm backdrop (VIX≈18.7)
```

### 412. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.70)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.70) | [macro] Calm backdrop (VIX≈18.7)
```

### 413. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 414. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.52)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.52) | [macro] Calm backdrop (VIX≈18.7)
```

### 415. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.79)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.79) | [macro] Calm backdrop (VIX≈18.7)
```

### 416. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 417. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.83)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.83) | [macro] Calm backdrop (VIX≈18.7)
```

### 418. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.50)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.50) | [macro] Calm backdrop (VIX≈18.7)
```

### 419. `WMT` → **BUY**  (raw_score=+0.6920, conf=0.733, pos_w=0.489, agents=2)

```
TradeSignal WMT → BUY
  raw_score=+0.69200   confidence=0.733   position_weight=0.4888   agents=2
  contributing partials:
    · sentiment     score=+0.7038  conf=0.80  — FinBERT POSITIVE (p=0.70)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.70) | [macro] Calm backdrop (VIX≈18.7)
```

### 420. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 421. `WMT` → **BUY**  (raw_score=+0.7852, conf=0.760, pos_w=0.580, agents=2)

```
TradeSignal WMT → BUY
  raw_score=+0.78520   confidence=0.760   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.8010  conf=0.83  — FinBERT POSITIVE (p=0.80)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.80) | [macro] Calm backdrop (VIX≈18.7)
```

### 422. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.78)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.78) | [macro] Calm backdrop (VIX≈18.7)
```

### 423. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 424. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.48)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.48) | [macro] Calm backdrop (VIX≈18.7)
```

### 425. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 426. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.78)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.78) | [macro] Calm backdrop (VIX≈18.7)
```

### 427. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.44)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.44) | [macro] Calm backdrop (VIX≈18.7)
```

### 428. `WMT` → **SELL**  (raw_score=-0.8938, conf=0.791, pos_w=0.580, agents=2)

```
TradeSignal WMT → SELL
  raw_score=-0.89380   confidence=0.791   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.9164  conf=0.87  — FinBERT NEGATIVE (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 429. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.95)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.95) | [macro] Calm backdrop (VIX≈18.7)
```

### 430. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 431. `WMT` → **SELL**  (raw_score=-0.5598, conf=0.695, pos_w=0.364, agents=2)

```
TradeSignal WMT → SELL
  raw_score=-0.55980   confidence=0.695   position_weight=0.3645   agents=2
  contributing partials:
    · sentiment     score=-0.5678  conf=0.75  — FinBERT NEGATIVE (p=0.57)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.57) | [macro] Calm backdrop (VIX≈18.7)
```

### 432. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.84)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.84) | [macro] Calm backdrop (VIX≈18.7)
```

### 433. `WMT` → **SELL**  (raw_score=-0.4548, conf=0.665, pos_w=0.273, agents=2)

```
TradeSignal WMT → SELL
  raw_score=-0.45480   confidence=0.665   position_weight=0.2730   agents=2
  contributing partials:
    · sentiment     score=-0.4572  conf=0.71  — FinBERT NEGATIVE (p=0.46)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.46) | [macro] Calm backdrop (VIX≈18.7)
```

### 434. `WMT` → **BUY**  (raw_score=+0.7713, conf=0.756, pos_w=0.569, agents=2)

```
TradeSignal WMT → BUY
  raw_score=+0.77130   confidence=0.756   position_weight=0.5687   agents=2
  contributing partials:
    · sentiment     score=+0.7866  conf=0.83  — FinBERT POSITIVE (p=0.79)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.79) | [macro] Calm backdrop (VIX≈18.7)
```

### 435. `WMT` → **SELL**  (raw_score=-0.5796, conf=0.701, pos_w=0.383, agents=2)

```
TradeSignal WMT → SELL
  raw_score=-0.57960   confidence=0.701   position_weight=0.3825   agents=2
  contributing partials:
    · sentiment     score=-0.5887  conf=0.76  — FinBERT NEGATIVE (p=0.59)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.59) | [macro] Calm backdrop (VIX≈18.7)
```

### 436. `WMT` → **SELL**  (raw_score=-0.8863, conf=0.789, pos_w=0.580, agents=2)

```
TradeSignal WMT → SELL
  raw_score=-0.88630   confidence=0.789   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.9086  conf=0.87  — FinBERT NEGATIVE (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 437. `WMT` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal WMT → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 438. `MSFT` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal MSFT → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 439. `MSFT` → **HOLD**  (raw_score=+0.0337, conf=0.464, pos_w=0.000, agents=3)

```
TradeSignal MSFT → HOLD
  raw_score=+0.03370   confidence=0.464   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0400  conf=0.35  — 10-Q: periodic disclosure (low directional edge)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 10-Q: periodic disclosure (low directional edge) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 440. `MSFT` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal MSFT → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 441. `MSFT` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 442. `MSFT` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 443. `PG` → **BUY**  (raw_score=+0.5197, conf=0.683, pos_w=0.328, agents=2)

```
TradeSignal PG → BUY
  raw_score=+0.51970   confidence=0.683   position_weight=0.3284   agents=2
  contributing partials:
    · sentiment     score=+0.5229  conf=0.73  — FinBERT POSITIVE (p=0.52)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.52) | [macro] Calm backdrop (VIX≈18.7)
```

### 444. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.76)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.76) | [macro] Calm backdrop (VIX≈18.7)
```

### 445. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.76)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.76) | [macro] Calm backdrop (VIX≈18.7)
```

### 446. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 447. `PG` → **BUY**  (raw_score=+0.8559, conf=0.780, pos_w=0.580, agents=2)

```
TradeSignal PG → BUY
  raw_score=+0.85590   confidence=0.780   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.8746  conf=0.86  — FinBERT POSITIVE (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 448. `PG` → **SELL**  (raw_score=-0.6264, conf=0.715, pos_w=0.426, agents=2)

```
TradeSignal PG → SELL
  raw_score=-0.62640   confidence=0.715   position_weight=0.4260   agents=2
  contributing partials:
    · sentiment     score=-0.6377  conf=0.77  — FinBERT NEGATIVE (p=0.64)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.64) | [macro] Calm backdrop (VIX≈18.7)
```

### 449. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 450. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.80)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.80) | [macro] Calm backdrop (VIX≈18.7)
```

### 451. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 452. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.95)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.95) | [macro] Calm backdrop (VIX≈18.7)
```

### 453. `PG` → **BUY**  (raw_score=+0.6352, conf=0.716, pos_w=0.434, agents=2)

```
TradeSignal PG → BUY
  raw_score=+0.63520   confidence=0.716   position_weight=0.4339   agents=2
  contributing partials:
    · sentiment     score=+0.6443  conf=0.78  — FinBERT POSITIVE (p=0.64)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.64) | [macro] Calm backdrop (VIX≈18.7)
```

### 454. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 455. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.95)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.95) | [macro] Calm backdrop (VIX≈18.7)
```

### 456. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.85)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.85) | [macro] Calm backdrop (VIX≈18.7)
```

### 457. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.86)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.86) | [macro] Calm backdrop (VIX≈18.7)
```

### 458. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 459. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 460. `PG` → **BUY**  (raw_score=+0.5127, conf=0.681, pos_w=0.322, agents=2)

```
TradeSignal PG → BUY
  raw_score=+0.51270   confidence=0.681   position_weight=0.3222   agents=2
  contributing partials:
    · sentiment     score=+0.5155  conf=0.73  — FinBERT POSITIVE (p=0.52)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.52) | [macro] Calm backdrop (VIX≈18.7)
```

### 461. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 462. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.84)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.84) | [macro] Calm backdrop (VIX≈18.7)
```

### 463. `PG` → **BUY**  (raw_score=+0.7417, conf=0.747, pos_w=0.538, agents=2)

```
TradeSignal PG → BUY
  raw_score=+0.74170   confidence=0.747   position_weight=0.5385   agents=2
  contributing partials:
    · sentiment     score=+0.7557  conf=0.81  — FinBERT POSITIVE (p=0.76)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.76) | [macro] Calm backdrop (VIX≈18.7)
```

### 464. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.71)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.71) | [macro] Calm backdrop (VIX≈18.7)
```

### 465. `PG` → **BUY**  (raw_score=+0.7867, conf=0.760, pos_w=0.580, agents=2)

```
TradeSignal PG → BUY
  raw_score=+0.78670   confidence=0.760   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.8026  conf=0.83  — FinBERT POSITIVE (p=0.80)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.80) | [macro] Calm backdrop (VIX≈18.7)
```

### 466. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.86)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.86) | [macro] Calm backdrop (VIX≈18.7)
```

### 467. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.62)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.62) | [macro] Calm backdrop (VIX≈18.7)
```

### 468. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.85)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.85) | [macro] Calm backdrop (VIX≈18.7)
```

### 469. `PG` → **BUY**  (raw_score=+0.9260, conf=0.800, pos_w=0.580, agents=2)

```
TradeSignal PG → BUY
  raw_score=+0.92600   confidence=0.800   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.9475  conf=0.88  — FinBERT POSITIVE (p=0.95)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.95) | [macro] Calm backdrop (VIX≈18.7)
```

### 470. `PG` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal PG → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.76)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.76) | [macro] Calm backdrop (VIX≈18.7)
```

### 471. `PG` → **SELL**  (raw_score=-0.9408, conf=0.805, pos_w=0.580, agents=2)

```
TradeSignal PG → SELL
  raw_score=-0.94080   confidence=0.805   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.9651  conf=0.89  — FinBERT NEGATIVE (p=0.97)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.97) | [macro] Calm backdrop (VIX≈18.7)
```

### 472. `PG` → **SELL**  (raw_score=-0.9408, conf=0.805, pos_w=0.580, agents=2)

```
TradeSignal PG → SELL
  raw_score=-0.94080   confidence=0.805   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.9651  conf=0.89  — FinBERT NEGATIVE (p=0.97)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.97) | [macro] Calm backdrop (VIX≈18.7)
```

### 473. `MSFT` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal MSFT → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 474. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 475. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.79)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.79) | [macro] Calm backdrop (VIX≈18.7)
```

### 476. `MA` → **BUY**  (raw_score=+0.9305, conf=0.801, pos_w=0.580, agents=2)

```
TradeSignal MA → BUY
  raw_score=+0.93050   confidence=0.801   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.9522  conf=0.88  — FinBERT POSITIVE (p=0.95)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.95) | [macro] Calm backdrop (VIX≈18.7)
```

### 477. `MA` → **BUY**  (raw_score=+0.6106, conf=0.709, pos_w=0.411, agents=2)

```
TradeSignal MA → BUY
  raw_score=+0.61060   confidence=0.709   position_weight=0.4107   agents=2
  contributing partials:
    · sentiment     score=+0.6185  conf=0.77  — FinBERT POSITIVE (p=0.62)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.62) | [macro] Calm backdrop (VIX≈18.7)
```

### 478. `MA` → **BUY**  (raw_score=+0.7669, conf=0.754, pos_w=0.564, agents=2)

```
TradeSignal MA → BUY
  raw_score=+0.76690   confidence=0.754   position_weight=0.5642   agents=2
  contributing partials:
    · sentiment     score=+0.7820  conf=0.82  — FinBERT POSITIVE (p=0.78)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.78) | [macro] Calm backdrop (VIX≈18.7)
```

### 479. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 480. `MA` → **SELL**  (raw_score=-0.7654, conf=0.755, pos_w=0.563, agents=2)

```
TradeSignal MA → SELL
  raw_score=-0.76540   confidence=0.755   position_weight=0.5632   agents=2
  contributing partials:
    · sentiment     score=-0.7829  conf=0.82  — FinBERT NEGATIVE (p=0.78)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.78) | [macro] Calm backdrop (VIX≈18.7)
```

### 481. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.77)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.77) | [macro] Calm backdrop (VIX≈18.7)
```

### 482. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 483. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.85)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.85) | [macro] Calm backdrop (VIX≈18.7)
```

### 484. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.61)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.61) | [macro] Calm backdrop (VIX≈18.7)
```

### 485. `MA` → **SELL**  (raw_score=-0.7650, conf=0.754, pos_w=0.563, agents=2)

```
TradeSignal MA → SELL
  raw_score=-0.76500   confidence=0.754   position_weight=0.5628   agents=2
  contributing partials:
    · sentiment     score=-0.7825  conf=0.82  — FinBERT NEGATIVE (p=0.78)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.78) | [macro] Calm backdrop (VIX≈18.7)
```

### 486. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.75)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.75) | [macro] Calm backdrop (VIX≈18.7)
```

### 487. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.75)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.75) | [macro] Calm backdrop (VIX≈18.7)
```

### 488. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 489. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.48)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.48) | [macro] Calm backdrop (VIX≈18.7)
```

### 490. `MA` → **SELL**  (raw_score=-0.7279, conf=0.744, pos_w=0.525, agents=2)

```
TradeSignal MA → SELL
  raw_score=-0.72790   confidence=0.744   position_weight=0.5250   agents=2
  contributing partials:
    · sentiment     score=-0.7438  conf=0.81  — FinBERT NEGATIVE (p=0.74)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.74) | [macro] Calm backdrop (VIX≈18.7)
```

### 491. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.85)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.85) | [macro] Calm backdrop (VIX≈18.7)
```

### 492. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 493. `MA` → **BUY**  (raw_score=+0.8992, conf=0.792, pos_w=0.580, agents=2)

```
TradeSignal MA → BUY
  raw_score=+0.89920   confidence=0.792   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.9196  conf=0.87  — FinBERT POSITIVE (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 494. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 495. `MA` → **BUY**  (raw_score=+0.8921, conf=0.790, pos_w=0.580, agents=2)

```
TradeSignal MA → BUY
  raw_score=+0.89210   confidence=0.790   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.9123  conf=0.87  — FinBERT POSITIVE (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 496. `MA` → **SELL**  (raw_score=-0.8819, conf=0.788, pos_w=0.580, agents=2)

```
TradeSignal MA → SELL
  raw_score=-0.88190   confidence=0.788   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.9040  conf=0.87  — FinBERT NEGATIVE (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 497. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 498. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.75)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.75) | [macro] Calm backdrop (VIX≈18.7)
```

### 499. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 500. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.82)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.82) | [macro] Calm backdrop (VIX≈18.7)
```

### 501. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.77)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.77) | [macro] Calm backdrop (VIX≈18.7)
```

### 502. `MA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal MA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 503. `UNH` → **BUY**  (raw_score=+0.6008, conf=0.707, pos_w=0.402, agents=2)

```
TradeSignal UNH → BUY
  raw_score=+0.60080   confidence=0.707   position_weight=0.4017   agents=2
  contributing partials:
    · sentiment     score=+0.6083  conf=0.76  — FinBERT POSITIVE (p=0.61)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.61) | [macro] Calm backdrop (VIX≈18.7)
```

### 504. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 505. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 506. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.78)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.78) | [macro] Calm backdrop (VIX≈18.7)
```

### 507. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 508. `UNH` → **BUY**  (raw_score=+0.6682, conf=0.726, pos_w=0.466, agents=2)

```
TradeSignal UNH → BUY
  raw_score=+0.66820   confidence=0.726   position_weight=0.4656   agents=2
  contributing partials:
    · sentiment     score=+0.6789  conf=0.79  — FinBERT POSITIVE (p=0.68)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.68) | [macro] Calm backdrop (VIX≈18.7)
```

### 509. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 510. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 511. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.61)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.61) | [macro] Calm backdrop (VIX≈18.7)
```

### 512. `UNH` → **SELL**  (raw_score=-0.5345, conf=0.688, pos_w=0.342, agents=2)

```
TradeSignal UNH → SELL
  raw_score=-0.53450   confidence=0.688   position_weight=0.3419   agents=2
  contributing partials:
    · sentiment     score=-0.5413  conf=0.74  — FinBERT NEGATIVE (p=0.54)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.54) | [macro] Calm backdrop (VIX≈18.7)
```

### 513. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 514. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 515. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 516. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.83)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.83) | [macro] Calm backdrop (VIX≈18.7)
```

### 517. `UNH` → **SELL**  (raw_score=-0.5478, conf=0.692, pos_w=0.354, agents=2)

```
TradeSignal UNH → SELL
  raw_score=-0.54780   confidence=0.692   position_weight=0.3537   agents=2
  contributing partials:
    · sentiment     score=-0.5552  conf=0.74  — FinBERT NEGATIVE (p=0.56)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.56) | [macro] Calm backdrop (VIX≈18.7)
```

### 518. `UNH` → **BUY**  (raw_score=+0.7630, conf=0.753, pos_w=0.560, agents=2)

```
TradeSignal UNH → BUY
  raw_score=+0.76300   confidence=0.753   position_weight=0.5602   agents=2
  contributing partials:
    · sentiment     score=+0.7779  conf=0.82  — FinBERT POSITIVE (p=0.78)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.78) | [macro] Calm backdrop (VIX≈18.7)
```

### 519. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 520. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.81)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.81) | [macro] Calm backdrop (VIX≈18.7)
```

### 521. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.80)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.80) | [macro] Calm backdrop (VIX≈18.7)
```

### 522. `UNH` → **SELL**  (raw_score=-0.6537, conf=0.723, pos_w=0.452, agents=2)

```
TradeSignal UNH → SELL
  raw_score=-0.65370   confidence=0.723   position_weight=0.4520   agents=2
  contributing partials:
    · sentiment     score=-0.6663  conf=0.78  — FinBERT NEGATIVE (p=0.67)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.67) | [macro] Calm backdrop (VIX≈18.7)
```

### 523. `UNH` → **BUY**  (raw_score=+0.9082, conf=0.795, pos_w=0.580, agents=2)

```
TradeSignal UNH → BUY
  raw_score=+0.90820   confidence=0.795   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.9290  conf=0.88  — FinBERT POSITIVE (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 524. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.56)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.56) | [macro] Calm backdrop (VIX≈18.7)
```

### 525. `UNH` → **BUY**  (raw_score=+0.9206, conf=0.798, pos_w=0.580, agents=2)

```
TradeSignal UNH → BUY
  raw_score=+0.92060   confidence=0.798   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.9419  conf=0.88  — FinBERT POSITIVE (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 526. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 527. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.80)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.80) | [macro] Calm backdrop (VIX≈18.7)
```

### 528. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.58)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.58) | [macro] Calm backdrop (VIX≈18.7)
```

### 529. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.95)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.95) | [macro] Calm backdrop (VIX≈18.7)
```

### 530. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 531. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.83)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.83) | [macro] Calm backdrop (VIX≈18.7)
```

### 532. `UNH` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal UNH → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 533. `GOOGL` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal GOOGL → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 534. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.95)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.95) | [macro] Calm backdrop (VIX≈18.7)
```

### 535. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.84)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.84) | [macro] Calm backdrop (VIX≈18.7)
```

### 536. `HD` → **SELL**  (raw_score=-0.6798, conf=0.730, pos_w=0.477, agents=2)

```
TradeSignal HD → SELL
  raw_score=-0.67980   confidence=0.730   position_weight=0.4773   agents=2
  contributing partials:
    · sentiment     score=-0.6935  conf=0.79  — FinBERT NEGATIVE (p=0.69)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.69) | [macro] Calm backdrop (VIX≈18.7)
```

### 537. `HD` → **SELL**  (raw_score=-0.7050, conf=0.737, pos_w=0.502, agents=2)

```
TradeSignal HD → SELL
  raw_score=-0.70500   confidence=0.737   position_weight=0.5022   agents=2
  contributing partials:
    · sentiment     score=-0.7200  conf=0.80  — FinBERT NEGATIVE (p=0.72)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.72) | [macro] Calm backdrop (VIX≈18.7)
```

### 538. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 539. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 540. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.66)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.66) | [macro] Calm backdrop (VIX≈18.7)
```

### 541. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 542. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 543. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.63)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.63) | [macro] Calm backdrop (VIX≈18.7)
```

### 544. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.67)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.67) | [macro] Calm backdrop (VIX≈18.7)
```

### 545. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.86)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.86) | [macro] Calm backdrop (VIX≈18.7)
```

### 546. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 547. `HD` → **SELL**  (raw_score=-0.8320, conf=0.774, pos_w=0.580, agents=2)

```
TradeSignal HD → SELL
  raw_score=-0.83200   confidence=0.774   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.8523  conf=0.85  — FinBERT NEGATIVE (p=0.85)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.85) | [macro] Calm backdrop (VIX≈18.7)
```

### 548. `HD` → **BUY**  (raw_score=+0.7692, conf=0.755, pos_w=0.567, agents=2)

```
TradeSignal HD → BUY
  raw_score=+0.76920   confidence=0.755   position_weight=0.5666   agents=2
  contributing partials:
    · sentiment     score=+0.7844  conf=0.82  — FinBERT POSITIVE (p=0.78)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.78) | [macro] Calm backdrop (VIX≈18.7)
```

### 549. `HD` → **SELL**  (raw_score=-0.6591, conf=0.724, pos_w=0.457, agents=2)

```
TradeSignal HD → SELL
  raw_score=-0.65910   confidence=0.724   position_weight=0.4572   agents=2
  contributing partials:
    · sentiment     score=-0.6720  conf=0.79  — FinBERT NEGATIVE (p=0.67)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.67) | [macro] Calm backdrop (VIX≈18.7)
```

### 550. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.59)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.59) | [macro] Calm backdrop (VIX≈18.7)
```

### 551. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 552. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.67)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.67) | [macro] Calm backdrop (VIX≈18.7)
```

### 553. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.64)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.64) | [macro] Calm backdrop (VIX≈18.7)
```

### 554. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.68)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.68) | [macro] Calm backdrop (VIX≈18.7)
```

### 555. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.66)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.66) | [macro] Calm backdrop (VIX≈18.7)
```

### 556. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.75)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.75) | [macro] Calm backdrop (VIX≈18.7)
```

### 557. `HD` → **BUY**  (raw_score=+0.4401, conf=0.660, pos_w=0.260, agents=2)

```
TradeSignal HD → BUY
  raw_score=+0.44010   confidence=0.660   position_weight=0.2604   agents=2
  contributing partials:
    · sentiment     score=+0.4388  conf=0.70  — FinBERT POSITIVE (p=0.44)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.44) | [macro] Calm backdrop (VIX≈18.7)
```

### 558. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.51)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.51) | [macro] Calm backdrop (VIX≈18.7)
```

### 559. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.46)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.46) | [macro] Calm backdrop (VIX≈18.7)
```

### 560. `HD` → **BUY**  (raw_score=+0.6535, conf=0.722, pos_w=0.451, agents=2)

```
TradeSignal HD → BUY
  raw_score=+0.65350   confidence=0.722   position_weight=0.4514   agents=2
  contributing partials:
    · sentiment     score=+0.6635  conf=0.78  — FinBERT POSITIVE (p=0.66)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.66) | [macro] Calm backdrop (VIX≈18.7)
```

### 561. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.86)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.86) | [macro] Calm backdrop (VIX≈18.7)
```

### 562. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.74)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.74) | [macro] Calm backdrop (VIX≈18.7)
```

### 563. `HD` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal HD → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.64)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.64) | [macro] Calm backdrop (VIX≈18.7)
```

### 564. `GOOGL` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 565. `GOOGL` → **HOLD**  (raw_score=+0.0337, conf=0.464, pos_w=0.000, agents=3)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.03370   confidence=0.464   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0400  conf=0.35  — 10-Q: periodic disclosure (low directional edge)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 10-Q: periodic disclosure (low directional edge) | [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 566. `GOOGL` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 567. `GOOGL` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal GOOGL → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 568. `GOOGL` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 569. `DIS` → **BUY**  (raw_score=+0.7079, conf=0.737, pos_w=0.505, agents=2)

```
TradeSignal DIS → BUY
  raw_score=+0.70790   confidence=0.737   position_weight=0.5046   agents=2
  contributing partials:
    · sentiment     score=+0.7204  conf=0.80  — FinBERT POSITIVE (p=0.72)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.72) | [macro] Calm backdrop (VIX≈18.7)
```

### 570. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 571. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 572. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 573. `DIS` → **SELL**  (raw_score=-0.7638, conf=0.754, pos_w=0.561, agents=2)

```
TradeSignal DIS → SELL
  raw_score=-0.76380   confidence=0.754   position_weight=0.5615   agents=2
  contributing partials:
    · sentiment     score=-0.7812  conf=0.82  — FinBERT NEGATIVE (p=0.78)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.78) | [macro] Calm backdrop (VIX≈18.7)
```

### 574. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 575. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.81)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.81) | [macro] Calm backdrop (VIX≈18.7)
```

### 576. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 577. `DIS` → **BUY**  (raw_score=+0.4401, conf=0.660, pos_w=0.260, agents=2)

```
TradeSignal DIS → BUY
  raw_score=+0.44010   confidence=0.660   position_weight=0.2604   agents=2
  contributing partials:
    · sentiment     score=+0.4388  conf=0.70  — FinBERT POSITIVE (p=0.44)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.44) | [macro] Calm backdrop (VIX≈18.7)
```

### 578. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 579. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 580. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 581. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.79)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.79) | [macro] Calm backdrop (VIX≈18.7)
```

### 582. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.79)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.79) | [macro] Calm backdrop (VIX≈18.7)
```

### 583. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.80)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.80) | [macro] Calm backdrop (VIX≈18.7)
```

### 584. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.71)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.71) | [macro] Calm backdrop (VIX≈18.7)
```

### 585. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.82)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.82) | [macro] Calm backdrop (VIX≈18.7)
```

### 586. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.84)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.84) | [macro] Calm backdrop (VIX≈18.7)
```

### 587. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 588. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.86)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.86) | [macro] Calm backdrop (VIX≈18.7)
```

### 589. `DIS` → **SELL**  (raw_score=-0.4995, conf=0.678, pos_w=0.311, agents=2)

```
TradeSignal DIS → SELL
  raw_score=-0.49950   confidence=0.678   position_weight=0.3111   agents=2
  contributing partials:
    · sentiment     score=-0.5044  conf=0.73  — FinBERT NEGATIVE (p=0.50)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.50) | [macro] Calm backdrop (VIX≈18.7)
```

### 590. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 591. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 592. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 593. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 594. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.84)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.84) | [macro] Calm backdrop (VIX≈18.7)
```

### 595. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 596. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 597. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 598. `DIS` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal DIS → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.79)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.79) | [macro] Calm backdrop (VIX≈18.7)
```

### 599. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 600. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 601. `BAC` → **SELL**  (raw_score=-0.5616, conf=0.696, pos_w=0.366, agents=2)

```
TradeSignal BAC → SELL
  raw_score=-0.56160   confidence=0.696   position_weight=0.3661   agents=2
  contributing partials:
    · sentiment     score=-0.5698  conf=0.75  — FinBERT NEGATIVE (p=0.57)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.57) | [macro] Calm backdrop (VIX≈18.7)
```

### 602. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.83)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.83) | [macro] Calm backdrop (VIX≈18.7)
```

### 603. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 604. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 605. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.86)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.86) | [macro] Calm backdrop (VIX≈18.7)
```

### 606. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.69)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.69) | [macro] Calm backdrop (VIX≈18.7)
```

### 607. `BAC` → **BUY**  (raw_score=+0.4949, conf=0.676, pos_w=0.307, agents=2)

```
TradeSignal BAC → BUY
  raw_score=+0.49490   confidence=0.676   position_weight=0.3068   agents=2
  contributing partials:
    · sentiment     score=+0.4968  conf=0.72  — FinBERT POSITIVE (p=0.50)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.50) | [macro] Calm backdrop (VIX≈18.7)
```

### 608. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.85)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.85) | [macro] Calm backdrop (VIX≈18.7)
```

### 609. `BAC` → **BUY**  (raw_score=+0.9176, conf=0.797, pos_w=0.580, agents=2)

```
TradeSignal BAC → BUY
  raw_score=+0.91760   confidence=0.797   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.9387  conf=0.88  — FinBERT POSITIVE (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 610. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.63)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.63) | [macro] Calm backdrop (VIX≈18.7)
```

### 611. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 612. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 613. `BAC` → **SELL**  (raw_score=-0.6841, conf=0.731, pos_w=0.482, agents=2)

```
TradeSignal BAC → SELL
  raw_score=-0.68410   confidence=0.731   position_weight=0.4816   agents=2
  contributing partials:
    · sentiment     score=-0.6981  conf=0.79  — FinBERT NEGATIVE (p=0.70)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.70) | [macro] Calm backdrop (VIX≈18.7)
```

### 614. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 615. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 616. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.49)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.49) | [macro] Calm backdrop (VIX≈18.7)
```

### 617. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.50)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.50) | [macro] Calm backdrop (VIX≈18.7)
```

### 618. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.55)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.55) | [macro] Calm backdrop (VIX≈18.7)
```

### 619. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 620. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 621. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.86)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.86) | [macro] Calm backdrop (VIX≈18.7)
```

### 622. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 623. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 624. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.73)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.73) | [macro] Calm backdrop (VIX≈18.7)
```

### 625. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 626. `BAC` → **BUY**  (raw_score=+0.9227, conf=0.799, pos_w=0.580, agents=2)

```
TradeSignal BAC → BUY
  raw_score=+0.92270   confidence=0.799   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.9441  conf=0.88  — FinBERT POSITIVE (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 627. `BAC` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal BAC → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.74)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.74) | [macro] Calm backdrop (VIX≈18.7)
```

### 628. `BAC` → **SELL**  (raw_score=-0.7361, conf=0.746, pos_w=0.533, agents=2)

```
TradeSignal BAC → SELL
  raw_score=-0.73610   confidence=0.746   position_weight=0.5333   agents=2
  contributing partials:
    · sentiment     score=-0.7524  conf=0.81  — FinBERT NEGATIVE (p=0.75)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.75) | [macro] Calm backdrop (VIX≈18.7)
```

### 629. `GOOGL` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal GOOGL → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 630. `XOM` → **BUY**  (raw_score=+0.6430, conf=0.719, pos_w=0.441, agents=2)

```
TradeSignal XOM → BUY
  raw_score=+0.64300   confidence=0.719   position_weight=0.4413   agents=2
  contributing partials:
    · sentiment     score=+0.6524  conf=0.78  — FinBERT POSITIVE (p=0.65)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.65) | [macro] Calm backdrop (VIX≈18.7)
```

### 631. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 632. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 633. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.74)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.74) | [macro] Calm backdrop (VIX≈18.7)
```

### 634. `XOM` → **BUY**  (raw_score=+0.9043, conf=0.794, pos_w=0.580, agents=2)

```
TradeSignal XOM → BUY
  raw_score=+0.90430   confidence=0.794   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.9250  conf=0.87  — FinBERT POSITIVE (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 635. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 636. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 637. `XOM` → **BUY**  (raw_score=+0.9242, conf=0.799, pos_w=0.580, agents=2)

```
TradeSignal XOM → BUY
  raw_score=+0.92420   confidence=0.799   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.9456  conf=0.88  — FinBERT POSITIVE (p=0.95)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.95) | [macro] Calm backdrop (VIX≈18.7)
```

### 638. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 639. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 640. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 641. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 642. `XOM` → **BUY**  (raw_score=+0.5429, conf=0.690, pos_w=0.349, agents=2)

```
TradeSignal XOM → BUY
  raw_score=+0.54290   confidence=0.690   position_weight=0.3489   agents=2
  contributing partials:
    · sentiment     score=+0.5473  conf=0.74  — FinBERT POSITIVE (p=0.55)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.55) | [macro] Calm backdrop (VIX≈18.7)
```

### 643. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 644. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 645. `XOM` → **BUY**  (raw_score=+0.6738, conf=0.728, pos_w=0.471, agents=2)

```
TradeSignal XOM → BUY
  raw_score=+0.67380   confidence=0.728   position_weight=0.4710   agents=2
  contributing partials:
    · sentiment     score=+0.6847  conf=0.79  — FinBERT POSITIVE (p=0.68)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.68) | [macro] Calm backdrop (VIX≈18.7)
```

### 646. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 647. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.86)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.86) | [macro] Calm backdrop (VIX≈18.7)
```

### 648. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 649. `XOM` → **SELL**  (raw_score=-0.6975, conf=0.735, pos_w=0.495, agents=2)

```
TradeSignal XOM → SELL
  raw_score=-0.69750   confidence=0.735   position_weight=0.4947   agents=2
  contributing partials:
    · sentiment     score=-0.7121  conf=0.80  — FinBERT NEGATIVE (p=0.71)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.71) | [macro] Calm backdrop (VIX≈18.7)
```

### 650. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 651. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 652. `XOM` → **SELL**  (raw_score=-0.8119, conf=0.768, pos_w=0.580, agents=2)

```
TradeSignal XOM → SELL
  raw_score=-0.81190   confidence=0.768   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.8313  conf=0.84  — FinBERT NEGATIVE (p=0.83)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.83) | [macro] Calm backdrop (VIX≈18.7)
```

### 653. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 654. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 655. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.75)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.75) | [macro] Calm backdrop (VIX≈18.7)
```

### 656. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 657. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 658. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 659. `XOM` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal XOM → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.83)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.83) | [macro] Calm backdrop (VIX≈18.7)
```

### 660. `AMZN` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 661. `AMZN` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 662. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 663. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.57)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.57) | [macro] Calm backdrop (VIX≈18.7)
```

### 664. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 665. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 666. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 667. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 668. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 669. `CVX` → **BUY**  (raw_score=+0.9242, conf=0.799, pos_w=0.580, agents=2)

```
TradeSignal CVX → BUY
  raw_score=+0.92420   confidence=0.799   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.9456  conf=0.88  — FinBERT POSITIVE (p=0.95)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.95) | [macro] Calm backdrop (VIX≈18.7)
```

### 670. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 671. `CVX` → **SELL**  (raw_score=-0.6318, conf=0.716, pos_w=0.431, agents=2)

```
TradeSignal CVX → SELL
  raw_score=-0.63180   confidence=0.716   position_weight=0.4312   agents=2
  contributing partials:
    · sentiment     score=-0.6434  conf=0.78  — FinBERT NEGATIVE (p=0.64)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.64) | [macro] Calm backdrop (VIX≈18.7)
```

### 672. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.76)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.76) | [macro] Calm backdrop (VIX≈18.7)
```

### 673. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 674. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 675. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 676. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 677. `CVX` → **SELL**  (raw_score=-0.6975, conf=0.735, pos_w=0.495, agents=2)

```
TradeSignal CVX → SELL
  raw_score=-0.69750   confidence=0.735   position_weight=0.4947   agents=2
  contributing partials:
    · sentiment     score=-0.7121  conf=0.80  — FinBERT NEGATIVE (p=0.71)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.71) | [macro] Calm backdrop (VIX≈18.7)
```

### 678. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.95)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.95) | [macro] Calm backdrop (VIX≈18.7)
```

### 679. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 680. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 681. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 682. `CVX` → **SELL**  (raw_score=-0.8119, conf=0.768, pos_w=0.580, agents=2)

```
TradeSignal CVX → SELL
  raw_score=-0.81190   confidence=0.768   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=-0.8313  conf=0.84  — FinBERT NEGATIVE (p=0.83)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEGATIVE (p=0.83) | [macro] Calm backdrop (VIX≈18.7)
```

### 683. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.76)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.76) | [macro] Calm backdrop (VIX≈18.7)
```

### 684. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 685. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.75)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.75) | [macro] Calm backdrop (VIX≈18.7)
```

### 686. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 687. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.63)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.63) | [macro] Calm backdrop (VIX≈18.7)
```

### 688. `CVX` → **BUY**  (raw_score=+0.9337, conf=0.802, pos_w=0.580, agents=2)

```
TradeSignal CVX → BUY
  raw_score=+0.93370   confidence=0.802   position_weight=0.5800   agents=2
  contributing partials:
    · sentiment     score=+0.9555  conf=0.88  — FinBERT POSITIVE (p=0.96)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.96) | [macro] Calm backdrop (VIX≈18.7)
```

### 689. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.74)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.74) | [macro] Calm backdrop (VIX≈18.7)
```

### 690. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 691. `CVX` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal CVX → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 692. `AMZN` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 693. `AMZN` → **HOLD**  (raw_score=+0.0337, conf=0.464, pos_w=0.000, agents=3)

```
TradeSignal AMZN → HOLD
  raw_score=+0.03370   confidence=0.464   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0400  conf=0.35  — 10-Q: periodic disclosure (low directional edge)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 10-Q: periodic disclosure (low directional edge) | [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 694. `AMZN` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal AMZN → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 695. `AMZN` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 696. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 697. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.71)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.71) | [macro] Calm backdrop (VIX≈18.7)
```

### 698. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 699. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 700. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.86)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.86) | [macro] Calm backdrop (VIX≈18.7)
```

### 701. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 702. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 703. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 704. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.81)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.81) | [macro] Calm backdrop (VIX≈18.7)
```

### 705. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 706. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.86)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.86) | [macro] Calm backdrop (VIX≈18.7)
```

### 707. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 708. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 709. `COST` → **BUY**  (raw_score=+0.7310, conf=0.744, pos_w=0.528, agents=2)

```
TradeSignal COST → BUY
  raw_score=+0.73100   confidence=0.744   position_weight=0.5277   agents=2
  contributing partials:
    · sentiment     score=+0.7445  conf=0.81  — FinBERT POSITIVE (p=0.74)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.74) | [macro] Calm backdrop (VIX≈18.7)
```

### 710. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 711. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 712. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.59)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.59) | [macro] Calm backdrop (VIX≈18.7)
```

### 713. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 714. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.50)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.50) | [macro] Calm backdrop (VIX≈18.7)
```

### 715. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.89)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.89) | [macro] Calm backdrop (VIX≈18.7)
```

### 716. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 717. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 718. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.75)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.75) | [macro] Calm backdrop (VIX≈18.7)
```

### 719. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.87)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.87) | [macro] Calm backdrop (VIX≈18.7)
```

### 720. `COST` → **BUY**  (raw_score=+0.7354, conf=0.745, pos_w=0.532, agents=2)

```
TradeSignal COST → BUY
  raw_score=+0.73540   confidence=0.745   position_weight=0.5321   agents=2
  contributing partials:
    · sentiment     score=+0.7491  conf=0.81  — FinBERT POSITIVE (p=0.75)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT POSITIVE (p=0.75) | [macro] Calm backdrop (VIX≈18.7)
```

### 721. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.57)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.57) | [macro] Calm backdrop (VIX≈18.7)
```

### 722. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.68)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.68) | [macro] Calm backdrop (VIX≈18.7)
```

### 723. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.83)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.83) | [macro] Calm backdrop (VIX≈18.7)
```

### 724. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.54)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.54) | [macro] Calm backdrop (VIX≈18.7)
```

### 725. `COST` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal COST → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

### 726. `AMZN` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 727. `AMZN` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal AMZN → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 728. `AMZN` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal AMZN → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 729. `META` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal META → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 730. `META` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal META → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 731. `META` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal META → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 732. `META` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal META → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 733. `META` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal META → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 734. `META` → **HOLD**  (raw_score=+0.0337, conf=0.464, pos_w=0.000, agents=3)

```
TradeSignal META → HOLD
  raw_score=+0.03370   confidence=0.464   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0400  conf=0.35  — 10-Q: periodic disclosure (low directional edge)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 10-Q: periodic disclosure (low directional edge) | [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 735. `META` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal META → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 736. `META` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal META → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 737. `META` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal META → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 738. `META` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal META → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 739. `NVDA` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal NVDA → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 740. `NVDA` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal NVDA → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 741. `NVDA` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 742. `NVDA` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 743. `TSLA` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 744. `TSLA` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 745. `TSLA` → **HOLD**  (raw_score=+0.0337, conf=0.464, pos_w=0.000, agents=3)

```
TradeSignal TSLA → HOLD
  raw_score=+0.03370   confidence=0.464   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0400  conf=0.35  — 10-Q: periodic disclosure (low directional edge)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 10-Q: periodic disclosure (low directional edge) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 746. `TSLA` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal TSLA → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 747. `TSLA` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 748. `TSLA` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal TSLA → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 749. `TSLA` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 750. `TSLA` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 751. `TSLA` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 752. `TSLA` → **HOLD**  (raw_score=+0.0337, conf=0.464, pos_w=0.000, agents=3)

```
TradeSignal TSLA → HOLD
  raw_score=+0.03370   confidence=0.464   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0400  conf=0.35  — 10-K: periodic disclosure (low directional edge)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 10-K: periodic disclosure (low directional edge) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 753. `JPM` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal JPM → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 754. `JPM` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal JPM → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 755. `JPM` → **HOLD**  (raw_score=+0.0337, conf=0.464, pos_w=0.000, agents=3)

```
TradeSignal JPM → HOLD
  raw_score=+0.03370   confidence=0.464   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0400  conf=0.35  — 10-Q: periodic disclosure (low directional edge)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 10-Q: periodic disclosure (low directional edge) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 756. `JPM` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal JPM → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 757. `JPM` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal JPM → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 758. `JPM` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal JPM → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 759. `V` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal V → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 760. `V` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal V → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 761. `V` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal V → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 762. `V` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal V → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 763. `V` → **HOLD**  (raw_score=+0.0337, conf=0.464, pos_w=0.000, agents=3)

```
TradeSignal V → HOLD
  raw_score=+0.03370   confidence=0.464   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0400  conf=0.35  — 10-Q: periodic disclosure (low directional edge)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 10-Q: periodic disclosure (low directional edge) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 764. `V` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal V → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 765. `V` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal V → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 766. `V` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal V → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 767. `V` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal V → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 768. `JNJ` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 769. `JNJ` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal JNJ → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 770. `JNJ` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal JNJ → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 771. `WMT` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal WMT → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 772. `WMT` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal WMT → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 773. `WMT` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal WMT → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 774. `WMT` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal WMT → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 775. `WMT` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal WMT → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 776. `PG` → **HOLD**  (raw_score=+0.0337, conf=0.464, pos_w=0.000, agents=3)

```
TradeSignal PG → HOLD
  raw_score=+0.03370   confidence=0.464   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0400  conf=0.35  — 10-Q: periodic disclosure (low directional edge)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 10-Q: periodic disclosure (low directional edge) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 777. `PG` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal PG → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 778. `PG` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal PG → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 779. `PG` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal PG → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 780. `MA` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal MA → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 781. `MA` → **HOLD**  (raw_score=+0.0337, conf=0.464, pos_w=0.000, agents=3)

```
TradeSignal MA → HOLD
  raw_score=+0.03370   confidence=0.464   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0400  conf=0.35  — 10-Q: periodic disclosure (low directional edge)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.91)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 10-Q: periodic disclosure (low directional edge) | [sentiment] FinBERT NEUTRAL (p=0.91) | [macro] Calm backdrop (VIX≈18.7)
```

### 782. `MA` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal MA → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 783. `MA` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal MA → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 784. `UNH` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal UNH → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 785. `UNH` → **HOLD**  (raw_score=+0.0337, conf=0.464, pos_w=0.000, agents=3)

```
TradeSignal UNH → HOLD
  raw_score=+0.03370   confidence=0.464   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0400  conf=0.35  — 10-Q: periodic disclosure (low directional edge)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 10-Q: periodic disclosure (low directional edge) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 786. `UNH` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal UNH → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 787. `UNH` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal UNH → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 788. `UNH` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal UNH → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 789. `HD` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal HD → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 790. `HD` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal HD → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 791. `DIS` → **HOLD**  (raw_score=+0.0337, conf=0.464, pos_w=0.000, agents=3)

```
TradeSignal DIS → HOLD
  raw_score=+0.03370   confidence=0.464   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0400  conf=0.35  — 10-Q: periodic disclosure (low directional edge)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 10-Q: periodic disclosure (low directional edge) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 792. `DIS` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal DIS → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 793. `DIS` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal DIS → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 794. `BAC` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal BAC → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 795. `BAC` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal BAC → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 796. `BAC` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal BAC → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 797. `XOM` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal XOM → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 798. `XOM` → **HOLD**  (raw_score=+0.0337, conf=0.464, pos_w=0.000, agents=3)

```
TradeSignal XOM → HOLD
  raw_score=+0.03370   confidence=0.464   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0400  conf=0.35  — 10-Q: periodic disclosure (low directional edge)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 10-Q: periodic disclosure (low directional edge) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 799. `XOM` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal XOM → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 800. `XOM` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal XOM → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 801. `XOM` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal XOM → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 802. `XOM` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal XOM → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 803. `XOM` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal XOM → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 804. `XOM` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal XOM → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 805. `XOM` → **HOLD**  (raw_score=+0.0337, conf=0.464, pos_w=0.000, agents=3)

```
TradeSignal XOM → HOLD
  raw_score=+0.03370   confidence=0.464   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0400  conf=0.35  — 10-K: periodic disclosure (low directional edge)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 10-K: periodic disclosure (low directional edge) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 806. `XOM` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal XOM → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 807. `CVX` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal CVX → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 808. `CVX` → **HOLD**  (raw_score=+0.0337, conf=0.464, pos_w=0.000, agents=3)

```
TradeSignal CVX → HOLD
  raw_score=+0.03370   confidence=0.464   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0400  conf=0.35  — 10-Q: periodic disclosure (low directional edge)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 10-Q: periodic disclosure (low directional edge) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 809. `CVX` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal CVX → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 810. `CVX` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal CVX → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 811. `CVX` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal CVX → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 812. `CVX` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal CVX → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.94)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.94) | [macro] Calm backdrop (VIX≈18.7)
```

### 813. `CVX` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal CVX → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 814. `CVX` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal CVX → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 815. `COST` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal COST → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 816. `COST` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal COST → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 817. `COST` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal COST → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 818. `COST` → **HOLD**  (raw_score=+0.0337, conf=0.464, pos_w=0.000, agents=3)

```
TradeSignal COST → HOLD
  raw_score=+0.03370   confidence=0.464   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0400  conf=0.35  — 10-Q: periodic disclosure (low directional edge)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 10-Q: periodic disclosure (low directional edge) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 819. `COST` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal COST → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 820. `COST` → **BUY**  (raw_score=+0.0891, conf=0.516, pos_w=0.008, agents=3)

```
TradeSignal COST → BUY
  raw_score=+0.08910   confidence=0.516   position_weight=0.0079   agents=3
  contributing partials:
    · fundamental   score=+0.1200  conf=0.48  — 8-K: material corporate event (cautious positive prior)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] 8-K: material corporate event (cautious positive prior) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 821. `COST` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal COST → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.93)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.93) | [macro] Calm backdrop (VIX≈18.7)
```

### 822. `COST` → **HOLD**  (raw_score=+0.0029, conf=0.444, pos_w=0.000, agents=3)

```
TradeSignal COST → HOLD
  raw_score=+0.00290   confidence=0.444   position_weight=0.0000   agents=3
  contributing partials:
    · fundamental   score=+0.0000  conf=0.30  — Form 4 insider activity (no parsed side; no clear A/D — neutral)
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.92)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [fundamental] Form 4 insider activity (no parsed side; no clear A/D — neutral) | [sentiment] FinBERT NEUTRAL (p=0.92) | [macro] Calm backdrop (VIX≈18.7)
```

### 823. `NVDA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal NVDA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 824. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.90)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.90) | [macro] Calm backdrop (VIX≈18.7)
```

### 825. `TSLA` → **HOLD**  (raw_score=+0.0040, conf=0.539, pos_w=0.000, agents=2)

```
TradeSignal TSLA → HOLD
  raw_score=+0.00400   confidence=0.539   position_weight=0.0000   agents=2
  contributing partials:
    · sentiment     score=+0.0000  conf=0.55  — FinBERT NEUTRAL (p=0.88)
    · macro         score=+0.0200  conf=0.50  — Calm backdrop (VIX≈18.7)
  combined reasoning: [sentiment] FinBERT NEUTRAL (p=0.88) | [macro] Calm backdrop (VIX≈18.7)
```

---

This file is **overwritten** on every `python run_pipeline.py` run (unless disabled).
Path override: set `ALPHAGENT_RUN_REPORT_PATH` to a full file path.
Disable: `ALPHAGENT_RUN_REPORT=0`.