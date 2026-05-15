"""Shared opt-in debug logging for sub-agents (set ALPHAGENT_DEBUG_AGENTS=1)."""

from __future__ import annotations

import logging
import os

logger = logging.getLogger("AlphaAgent.agents")


def agent_debug_enabled() -> bool:
    return os.environ.get("ALPHAGENT_DEBUG_AGENTS", "0").strip().lower() in ("1", "true", "yes", "on")


def log_agent(agent: str, msg: str, *args: object) -> None:
    if agent_debug_enabled():
        logger.info("[%s] " + msg, agent, *args)
