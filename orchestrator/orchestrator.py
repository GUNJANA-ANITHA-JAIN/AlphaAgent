"""
Orchestrator: sits between ingestion and sub-agents.
Takes MarketEvents, runs the right agents in parallel, waits until enough
replies or a time limit (TTL), merges their scores into one TradeSignal, and
logs it. Hard part: short TTL for fast news, longer TTL for slow filings.
"""

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

import asyncio
import logging
import math
import os
import time
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Callable, Optional, Union

from core.event_codec import dict_to_market_event, market_event_to_dict
from core.models import MarketEvent

logger = logging.getLogger("Orchestrator")


# --- Shared types ---

class Direction(Enum):
    BUY  = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"


@dataclass
class PartialSignal:
    """One agent's vote for a ticker: score -1..+1, confidence 0..1."""
    agent_name:  str
    ticker:      str
    score:       float        # -1 sell .. +1 buy
    confidence:  float        # 0..1 trust in this vote
    timestamp:   datetime
    reasoning:   str = ""     # short text for logs / reports
    decay_hours: float = 24.0 # how fast this vote fades
    source_event_ids: list = field(default_factory=list)  # which events built this


@dataclass
class TradeSignal:
    """Merged output: raw_score is the blend; direction is BUY/SELL/HOLD from a band."""
    signal_id:         str
    ticker:            str
    direction:         Direction
    confidence:        float       # 0..1 overall trust
    raw_score:         float       # -1..+1 blended score
    contributing:      list        # PartialSignals that went in
    reasoning:         str         # joined agent notes
    timestamp:         datetime
    decay_hours:       float       # how long this stays “fresh”
    num_agents:        int         # how many agents spoke
    position_weight:   float = 0.0  # 0..1 size hint; 0 on HOLD


def format_trade_signal_message(signal: TradeSignal, fuse_reason: str = "") -> str:
    """Multi-line text for logs: shows each partial so a flat score is easy to debug."""
    fuse = f" (fuse: {fuse_reason})" if fuse_reason else ""
    lines = [
        f"TradeSignal {signal.ticker} → {signal.direction.value}{fuse}",
        f"  raw_score={signal.raw_score:+.5f}   confidence={signal.confidence:.3f}   "
        f"position_weight={signal.position_weight:.4f}   agents={signal.num_agents}",
        "  contributing partials:",
    ]
    for p in signal.contributing:
        lines.append(
            f"    · {p.agent_name:12s}  score={p.score:+.4f}  conf={p.confidence:.2f}  — {p.reasoning[:100]}"
            + ("…" if len(p.reasoning) > 100 else "")
        )
    r = signal.reasoning
    if len(r) > 240:
        r = r[:237] + "…"
    lines.append(f"  combined reasoning: {r}")
    return "\n".join(lines)


@dataclass
class TickerState:
    """Buffers partials for one ticker until we fuse; cleared after emit."""
    ticker:                    str
    partial_signals:          list = field(default_factory=list)
    created_at:               float = field(default_factory=time.monotonic)
    event_count:              int = 0
    trigger_event_type:       str = ""
    fuse_deadline_monotonic: float = 0.0  # fuse by this clock time even if agents lag

    def age_seconds(self) -> float:
        return time.monotonic() - self.created_at

    def agent_names(self) -> set:
        return {s.agent_name for s in self.partial_signals}


# --- Sub-agents inherit SubAgent and implement process() ---

class SubAgent:
    """Base for sentiment, fundamental, technical, macro. Keep process() fast."""
    name: str = "base"

    async def process(self, event: MarketEvent) -> Optional[PartialSignal]:
        """Return a PartialSignal or None; do not raise—handle errors inside."""
        raise NotImplementedError


# --- Which agents run for each event type ---

ROUTING_TABLE = {
    "news_article":  ["sentiment", "fundamental", "macro"],
    "price_update":  ["technical", "macro"],
    "sec_filing":    ["fundamental", "sentiment", "macro"],
    "social_post":   ["sentiment", "macro"],
    "earnings_call": ["sentiment", "fundamental", "macro"],
}

# Min distinct agents before we may fuse early (we still fuse at TTL if fewer).
MIN_AGENTS_REQUIRED = {
    "news_article":  2,
    "price_update":  1,
    "sec_filing":    1,
    "social_post":   1,
    "earnings_call": 2,
}

# Seconds to wait before we merge whatever we got (per event type).
TTL_BY_EVENT = {
    "news_article":  10,   # news: short wait
    "price_update":  5,    # prices: very short
    "sec_filing":    120,  # filings: can wait longer
    "social_post":   15,
    "earnings_call": 60,
}


# --- Merge partials into one score (weighted blend) ---

# How much each agent name counts (tune from backtests in real use).
AGENT_WEIGHTS = {
    "sentiment":   0.33,
    "fundamental": 0.28,
    "technical":   0.30,
    "macro":       0.09,
}

# Need |score| above this band to call BUY/SELL (else HOLD).
_HOLD_DEADBAND = float(os.environ.get("ALPHAGENT_HOLD_DEADBAND", "0.075"))
# Near-zero scores count less so they do not wash out strong views.
_FUSION_NEUTRAL_ABS = float(os.environ.get("ALPHAGENT_FUSION_NEUTRAL_SCORE_ABS", "0.032"))
_FUSION_NEUTRAL_WEIGHT_MULT = float(
    os.environ.get("ALPHAGENT_FUSION_NEUTRAL_WEIGHT_MULT", "0.38")
)
# Small push when everyone agrees on buy vs sell side.
_FUSION_AGREEMENT_BOOST = float(os.environ.get("ALPHAGENT_FUSION_AGREEMENT_BOOST", "0.030"))


def _normalized_agent_weights(partials: list[PartialSignal]) -> dict[str, float]:
    """Renormalize agent weights so only agents in this batch share 100%."""
    order: list[str] = []
    seen: set[str] = set()
    for p in partials:
        if p.agent_name not in seen:
            seen.add(p.agent_name)
            order.append(p.agent_name)
    raw = {n: float(AGENT_WEIGHTS.get(n, 0.1)) for n in order}
    s = sum(raw.values())
    if s < 1e-12:
        u = len(order)
        return {n: (1.0 / u) if u else 0.0 for n in order}
    return {n: raw[n] / s for n in order}


def fuse_signals(partials: list[PartialSignal], ticker: str) -> TradeSignal:
    """
    Blend partials into one raw_score: score × confidence × agent_weight × age_decay,
    summed and divided by the same weight sum. Old votes fade using decay_hours.

    Weights are AGENT_WEIGHTS but only for agents in this batch (renormalized).
    Very small |score| counts less. Tune with ALPHAGENT_HOLD_DEADBAND and ALPHAGENT_FUSION_*.
    """
    if not partials:
        raise ValueError("Cannot fuse zero signals")

    norm_w = _normalized_agent_weights(partials)

    weighted_sum = 0.0
    weight_total = 0.0
    blend_conf_num = 0.0
    pos_mass = 0.0  # buy-side weight before neutral shrink
    neg_mass = 0.0
    min_decay    = float("inf")
    reasoning_parts = []

    now = datetime.now(timezone.utc)

    for p in partials:
        ts = p.timestamp
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)
        age_hours = max(0.0, (now - ts.astimezone(timezone.utc)).total_seconds() / 3600.0)
        half_life_h = max(float(p.decay_hours), 1e-6)
        decay_mult = math.exp(-age_hours / half_life_h)
        decay_mult = max(decay_mult, 0.05)

        agent_weight = norm_w.get(p.agent_name, 1.0 / max(1, len(partials)))
        base_eff = p.confidence * agent_weight * decay_mult
        blend_conf_num += float(p.confidence) * agent_weight
        if abs(p.score) < _FUSION_NEUTRAL_ABS:
            effective_weight = base_eff * _FUSION_NEUTRAL_WEIGHT_MULT
        else:
            effective_weight = base_eff
        weighted_sum  += p.score * effective_weight
        weight_total  += effective_weight
        if p.score > _FUSION_NEUTRAL_ABS:
            pos_mass += base_eff
        elif p.score < -_FUSION_NEUTRAL_ABS:
            neg_mass += base_eff
        min_decay      = min(min_decay, p.decay_hours)
        if p.reasoning:
            reasoning_parts.append(f"[{p.agent_name}] {p.reasoning}")

    raw_score  = weighted_sum / weight_total if weight_total > 0 else 0.0

    # If all directional weight is one way, bump score a bit.
    if pos_mass > 0.0 and neg_mass <= 1e-12:
        raw_score += _FUSION_AGREEMENT_BOOST * min(1.0, pos_mass * 2.5)
    elif neg_mass > 0.0 and pos_mass <= 1e-12:
        raw_score -= _FUSION_AGREEMENT_BOOST * min(1.0, neg_mass * 2.5)
    elif pos_mass > neg_mass * 2.1 and neg_mass > 1e-12:
        raw_score += _FUSION_AGREEMENT_BOOST * 0.38
    elif neg_mass > pos_mass * 2.1 and pos_mass > 1e-12:
        raw_score -= _FUSION_AGREEMENT_BOOST * 0.38

    raw_score = max(-1.0, min(1.0, raw_score))
    _conf_floor = float(os.environ.get("ALPHAGENT_FUSION_CONF_FLOOR", "0.22"))
    blend_conf = blend_conf_num  # weighted avg confidence
    confidence = max(_conf_floor, min(1.0, blend_conf))

    # Turn continuous score into BUY / SELL / HOLD
    band = max(0.02, _HOLD_DEADBAND)
    if raw_score > band:
        direction = Direction.BUY
    elif raw_score < -band:
        direction = Direction.SELL
    else:
        direction = Direction.HOLD

    # Size hint: 0 on HOLD; else how far past the band × confidence
    if direction == Direction.HOLD:
        position_weight = 0.0
    else:
        mag = abs(raw_score)
        span = max(1e-9, 1.0 - band)
        strength = max(0.0, min(1.0, (mag - band) / span))
        _pos_cap = float(os.environ.get("ALPHAGENT_FUSION_POSITION_CAP", "0.58"))
        position_weight = min(_pos_cap, min(1.0, strength * confidence))

    return TradeSignal(
        signal_id=str(uuid.uuid4()),
        ticker=ticker,
        direction=direction,
        confidence=round(confidence, 3),
        raw_score=round(raw_score, 4),
        contributing=partials,
        reasoning=" | ".join(reasoning_parts),
        timestamp=datetime.now(timezone.utc),
        decay_hours=min_decay,
        num_agents=len(partials),
        position_weight=round(position_weight, 4),
    )


class Orchestrator:
    """
    Queue of events, registered agents, per-ticker buffers, TTL fuse, merge, callbacks.

    orch = Orchestrator(); orch.register_agent(...); orch.on_signal(...); await orch.run()
    """

    def __init__(self, queue_maxsize: int = 10_000):
        self._queue:       asyncio.Queue = asyncio.Queue(maxsize=queue_maxsize)
        self._agents:      dict[str, SubAgent] = {}
        self._state:       dict[str, TickerState] = {}   # ticker -> buffer
        self._ticker_locks: dict[str, asyncio.Lock] = {}
        self._signal_log:  list[TradeSignal] = []        # in-memory list; replace with DB if needed
        self._handlers:    list[Callable] = []            # callbacks on each TradeSignal
        self._running:     bool = False
        self._stats = {"events_processed": 0, "signals_emitted": 0, "ttl_forced": 0}

    def _lock_for_ticker(self, ticker: str) -> asyncio.Lock:
        if ticker not in self._ticker_locks:
            self._ticker_locks[ticker] = asyncio.Lock()
        return self._ticker_locks[ticker]

    def register_agent(self, name: str, agent: SubAgent):
        self._agents[name] = agent
        logger.info(f"Registered sub-agent: {name}")

    def on_signal(self, handler: Callable[[TradeSignal], None]):
        """Call handler(signal) after each fuse."""
        self._handlers.append(handler)

    def push_event(self, event: Union[MarketEvent, dict[str, Any]]):
        """
        Add one event to the async queue (dict or MarketEvent). Drops if queue is full.
        """
        env = market_event_to_dict(event) if isinstance(event, MarketEvent) else event
        try:
            self._queue.put_nowait(env)
        except asyncio.QueueFull:
            t = env.get("ticker") if isinstance(env, dict) else None
            logger.warning(f"Queue full — dropping event for {t}")

    async def process_event(self, event: Union[MarketEvent, dict[str, Any]]) -> None:
        """Handle one event now (no queue). Good for tests and replay; no TTL timer."""
        env = market_event_to_dict(event) if isinstance(event, MarketEvent) else event
        await self._handle_event(env)
        self._stats["events_processed"] += 1

    async def run(self):
        self._running = True
        logger.info("Orchestrator started.")
        # Event loop, TTL timer, and stats log together
        await asyncio.gather(
            self._event_loop(),
            self._ttl_watchdog(),
            self._stats_reporter(),
        )

    async def _event_loop(self):
        """Pull from queue and handle each event."""
        while self._running:
            try:
                event = await asyncio.wait_for(self._queue.get(), timeout=1.0)
            except asyncio.TimeoutError:
                continue

            await self._handle_event(event)
            self._stats["events_processed"] += 1

        # Drain queue on shutdown so late pushes are not lost.
        while True:
            try:
                event = self._queue.get_nowait()
            except asyncio.QueueEmpty:
                break
            await self._handle_event(event)
            self._stats["events_processed"] += 1

    async def _handle_event(self, envelope: dict[str, Any]):
        """Pick agents for this event type, run them in parallel, buffer, fuse if ready."""
        event = dict_to_market_event(envelope)
        ticker = event.ticker.upper()
        event_type = (
            event.event_type.value
            if hasattr(event.event_type, "value")
            else str(event.event_type)
        )
        lock = self._lock_for_ticker(ticker)
        async with lock:
            agent_names = ROUTING_TABLE.get(event_type, [])

            if not agent_names:
                logger.debug(f"No routing for event_type={event_type}")
                return

            if ticker not in self._state:
                ttl_sec = float(TTL_BY_EVENT.get(event_type, 30))
                self._state[ticker] = TickerState(
                    ticker=ticker,
                    fuse_deadline_monotonic=time.monotonic() + ttl_sec,
                    trigger_event_type=event_type,
                )
            self._state[ticker].event_count += 1

            tasks = [
                self._call_agent(name, event)
                for name in agent_names
                if name in self._agents
            ]
            if not tasks:
                logger.warning(f"No registered agents for event_type={event_type}")
                return

            results = await asyncio.gather(*tasks, return_exceptions=True)

            for result in results:
                if isinstance(result, PartialSignal):
                    self._state[ticker].partial_signals.append(result)
                elif isinstance(result, Exception):
                    logger.error(f"[{ticker}] agent error: {result}")

            min_required = MIN_AGENTS_REQUIRED.get(event_type, 1)
            state = self._state[ticker]
            if len(state.agent_names()) >= min_required:
                await self._fuse_and_emit(ticker, reason="min_agents_met")

    async def _call_agent(self, name: str, event: MarketEvent) -> Optional[PartialSignal]:
        """Run one agent with a 30s cap."""
        agent = self._agents[name]
        try:
            return await asyncio.wait_for(agent.process(event), timeout=30.0)
        except asyncio.TimeoutError:
            logger.warning(f"Agent {name} timed out for {event.ticker}")
            return None
        except Exception as e:
            logger.error(f"Agent {name} raised: {e}")
            return None

    async def _ttl_watchdog(self):
        """When the per-ticker fuse deadline hits, merge whatever partials exist."""
        while self._running:
            await asyncio.sleep(1.0)
            now_m = time.monotonic()
            to_fuse: list[str] = []
            for ticker, state in list(self._state.items()):
                if not state.partial_signals:
                    continue
                if state.fuse_deadline_monotonic <= 0:
                    continue
                if now_m >= state.fuse_deadline_monotonic:
                    to_fuse.append(ticker)

            for ticker in to_fuse:
                lock = self._lock_for_ticker(ticker)
                async with lock:
                    st = self._state.get(ticker)
                    if not st or not st.partial_signals:
                        continue
                    if st.fuse_deadline_monotonic > 0 and time.monotonic() < st.fuse_deadline_monotonic:
                        continue
                    await self._fuse_and_emit(ticker, reason="ttl_expired")
                    self._stats["ttl_forced"] += 1

    async def _fuse_and_emit(self, ticker: str, reason: str = ""):
        """Merge buffer, log, call handlers, clear buffer."""
        state = self._state.get(ticker)
        if not state or not state.partial_signals:
            return

        try:
            signal = fuse_signals(state.partial_signals, ticker)
        except Exception as e:
            logger.error(f"Fusion failed for {ticker}: {e}")
            return

        # Append to in-memory log
        self._signal_log.append(signal)
        self._stats["signals_emitted"] += 1

        # User callbacks
        for handler in self._handlers:
            try:
                handler(signal)
            except Exception as e:
                logger.error(f"Signal handler failed: {e}")

        # If no handlers, print to log for quick runs.
        if not self._handlers:
            logger.info("%s", format_trade_signal_message(signal, fuse_reason=reason))

        # Drop ticker state for the next batch
        del self._state[ticker]

    async def _stats_reporter(self):
        while self._running:
            for _ in range(60):
                if not self._running:
                    return
                await asyncio.sleep(1.0)
            logger.info(
                f"Orchestrator stats — "
                f"events: {self._stats['events_processed']} | "
                f"signals: {self._stats['signals_emitted']} | "
                f"ttl_forced: {self._stats['ttl_forced']} | "
                f"queue_depth: {self._queue.qsize()}"
            )

    def stop(self):
        self._running = False

    def get_stats(self) -> dict[str, int]:
        """events_processed, signals_emitted, ttl_forced."""
        return dict(self._stats)

    def signal_history(self) -> list[TradeSignal]:
        """Copy of all TradeSignals emitted this run."""
        return list(self._signal_log)


def print_signal(signal: TradeSignal):
    """Print one signal to stdout (demo)."""
    print("\n" + format_trade_signal_message(signal) + "\n")
