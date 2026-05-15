"""
Sentiment: FinBERT (ProsusAI/finbert) or fast keyword mode.

Set HF_TOKEN for better Hugging Face Hub limits. Uses CUDA, Apple MPS, or CPU.
"""

from __future__ import annotations

import asyncio
import logging
import os
import re
from datetime import datetime, timezone
from typing import Optional

from core.models import EventType, MarketEvent

from .orchestrator import PartialSignal, SubAgent

logger = logging.getLogger("FinBERTSentiment")


def extract_sentiment_text(event: MarketEvent) -> str:
    """Pull one string to score from the event."""
    p = event.payload or {}
    if event.event_type == EventType.NEWS_ARTICLE:
        return f"{p.get('headline', '')} {p.get('body', '')}"
    if event.event_type == EventType.SOCIAL_POST:
        return str(p.get("text", ""))
    if event.event_type == EventType.SEC_FILING:
        ex = str(p.get("text_excerpt", ""))
        if ex.strip():
            return ex
        return f"{p.get('form_type', '')} filing {p.get('filed_date', '')}"
    if event.event_type == EventType.EARNINGS_CALL:
        return str(p.get("text", ""))
    return ""


def _infer_pipeline_device():
    try:
        import torch

        if torch.cuda.is_available():
            return 0
        if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
            return "mps"
    except Exception:
        pass
    return -1


class HeuristicSentimentAgent(SubAgent):
    """Keyword-based sentiment (no model)."""

    name = "sentiment"

    def _heuristic(self, text: str) -> tuple[float, float, str]:
        t = text.lower()
        pos_hits = len(re.findall(r"\b(beats?|bull|growth|upgrade|strong|surge)\b", t))
        neg_hits = len(re.findall(r"\b(miss|bear|weak|downgrade|lawsuit|probe)\b", t))
        if pos_hits == 0 and neg_hits == 0:
            return 0.0, 0.32, "Heuristic: neutral / no keywords"
        raw = (pos_hits - neg_hits) / max(pos_hits + neg_hits, 1)
        score = max(-1.0, min(1.0, 0.45 * raw))
        conf = min(0.38 + 0.1 * (pos_hits + neg_hits), 0.78)
        return score, conf, f"Heuristic: pos={pos_hits} neg={neg_hits}"

    async def process(self, event: MarketEvent) -> Optional[PartialSignal]:
        if event.event_type not in (
            EventType.NEWS_ARTICLE,
            EventType.SOCIAL_POST,
            EventType.SEC_FILING,
            EventType.EARNINGS_CALL,
        ):
            return None
        text = extract_sentiment_text(event).strip()
        if len(text) < 2:
            return None
        score, conf, reason = self._heuristic(text)
        eid = [event.event_id] if event.event_id else []
        return PartialSignal(
            agent_name="sentiment",
            ticker=event.ticker,
            score=score,
            confidence=conf,
            timestamp=datetime.now(timezone.utc),
            reasoning=reason,
            decay_hours=6.0,
            source_event_ids=eid,
        )


class FinBERTSentimentAgent(SubAgent):
    """FinBERT via Hugging Face pipelines."""

    name = "sentiment"

    def __init__(self, max_chars: int = 512, eager_load: bool = True):
        self._pipe = None
        self._load_failed = False
        self._max_chars = max_chars
        if eager_load:
            if self._ensure_pipeline():
                logger.info("FinBERT pipeline ready (ProsusAI/finbert).")
            else:
                logger.warning(
                    "FinBERT did not load at startup (missing deps or network). "
                    "Sentiment will use the keyword heuristic until torch+transformers work."
                )

    def _ensure_pipeline(self) -> bool:
        if self._load_failed:
            return False
        if self._pipe is not None:
            return True
        try:
            from transformers import pipeline
        except ImportError:
            logger.warning("transformers not installed — using heuristic sentiment")
            self._load_failed = True
            return False
        try:
            token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")
            device = _infer_pipeline_device()
            pl_kwargs: dict = {
                "model": "ProsusAI/finbert",
                "tokenizer": "ProsusAI/finbert",
                "truncation": True,
                "max_length": 512,
                "device": device,
            }
            if token:
                pl_kwargs["token"] = token
            self._pipe = pipeline("sentiment-analysis", **pl_kwargs)
            if not token:
                logger.info(
                    "FinBERT: no HF_TOKEN set — Hub downloads use anonymous limits; "
                    "see https://huggingface.co/settings/tokens"
                )
        except Exception as e:
            logger.error("Failed to load FinBERT: %s", e)
            self._load_failed = True
            return False
        return True

    def _heuristic(self, text: str) -> tuple[float, float, str]:
        t = text.lower()
        pos_hits = len(re.findall(r"\b(beats?|bull|growth|upgrade|strong|surge)\b", t))
        neg_hits = len(re.findall(r"\b(miss|bear|weak|downgrade|lawsuit|probe)\b", t))
        if pos_hits == 0 and neg_hits == 0:
            return 0.0, 0.30, "Heuristic: neutral / no keywords"
        raw = (pos_hits - neg_hits) / max(pos_hits + neg_hits, 1)
        score = max(-1.0, min(1.0, 0.45 * raw))
        conf = min(0.35 + 0.1 * (pos_hits + neg_hits), 0.75)
        return score, conf, f"Heuristic: pos={pos_hits} neg={neg_hits}"

    async def process(self, event: MarketEvent) -> Optional[PartialSignal]:
        if event.event_type not in (
            EventType.NEWS_ARTICLE,
            EventType.SOCIAL_POST,
            EventType.SEC_FILING,
            EventType.EARNINGS_CALL,
        ):
            return None

        text = extract_sentiment_text(event).strip()
        if len(text) < 2:
            return None

        eid = [event.event_id] if event.event_id else []

        if not self._ensure_pipeline():
            score, conf, reason = self._heuristic(text)
            return PartialSignal(
                agent_name="sentiment",
                ticker=event.ticker,
                score=score,
                confidence=conf,
                timestamp=datetime.now(timezone.utc),
                reasoning=reason,
                decay_hours=6.0,
                source_event_ids=eid,
            )

        snippet = text[: self._max_chars]

        def _infer() -> dict:
            out = self._pipe(snippet)
            return out[0] if isinstance(out, list) else out

        try:
            row = await asyncio.to_thread(_infer)
        except Exception as e:
            logger.warning("FinBERT inference failed: %s", e)
            score, conf, reason = self._heuristic(text)
            return PartialSignal(
                agent_name="sentiment",
                ticker=event.ticker,
                score=score,
                confidence=conf * 0.85,
                timestamp=datetime.now(timezone.utc),
                reasoning=reason + " (fallback)",
                decay_hours=6.0,
                source_event_ids=eid,
            )

        label = str(row.get("label", "")).upper()
        p = float(row.get("score", 0.5))
        # ProsusAI/finbert labels: positive, negative, neutral (or LABEL_* from raw head).
        if "NEG" in label:
            s = -p
        elif "POS" in label:
            s = p
        else:
            s = 0.0

        score = max(-1.0, min(1.0, s))
        confidence = min(0.55 + abs(s) * 0.35, 0.95)

        return PartialSignal(
            agent_name="sentiment",
            ticker=event.ticker,
            score=score,
            confidence=confidence,
            timestamp=datetime.now(timezone.utc),
            reasoning=f"FinBERT {label} (p={p:.2f})",
            decay_hours=6.0,
            source_event_ids=eid,
        )


def build_sentiment_agent(use_finbert: bool = True) -> SubAgent:
    """Factory: FinBERT when use_finbert; else fast HeuristicSentimentAgent."""
    if use_finbert:
        return FinBERTSentimentAgent(eager_load=True)
    return HeuristicSentimentAgent()
