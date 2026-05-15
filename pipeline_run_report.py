"""
Markdown summary for each run_pipeline.py session (default: runs/latest_pipeline_run.md).
"""

from __future__ import annotations

import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from orchestrator.orchestrator import format_trade_signal_message


def _report_path(repo_root: Path) -> Path:
    custom = os.environ.get("ALPHAGENT_RUN_REPORT_PATH", "").strip()
    if custom:
        return Path(custom).expanduser()
    return repo_root / "runs" / "latest_pipeline_run.md"


def _config_lines() -> list[str]:
    lines: list[str] = []
    hf = bool(os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN"))
    lines.append(f"- `HF_TOKEN` / Hub token: **{'set' if hf else 'not set'}**")
    fred = bool(os.environ.get("FRED_API_KEY", "").strip())
    lines.append(f"- `FRED_API_KEY`: **{'set' if fred else 'not set'}**")

    keys = [
        "ALPHAGENT_TICKERS",
        "ALPHAGENT_USE_FINBERT",
        "ALPHAGENT_LOG_EVENTS",
        "ALPHAGENT_DEBUG_AGENTS",
        "ALPHAGENT_HOLD_DEADBAND",
        "ALPHAGENT_FUSION_NEUTRAL_SCORE_ABS",
        "ALPHAGENT_FUSION_NEUTRAL_WEIGHT_MULT",
        "ALPHAGENT_FUSION_AGREEMENT_BOOST",
        "ALPHAGENT_FORM4_FETCH",
        "ALPHAGENT_MACRO_CACHE_SEC",
    ]
    for k in keys:
        if k not in os.environ:
            continue
        v = os.environ.get(k, "")
        lines.append(f"- `{k}` = `{v}`")
    return lines


def build_markdown(
    *,
    tickers: list[str],
    started: datetime,
    ended: datetime,
    signals: list[Any],
    stats: dict[str, int],
) -> str:
    dur = (ended - started).total_seconds()
    lines = [
        "# AlphaAgent — pipeline run summary",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| Run start (UTC) | `{started.isoformat(timespec='seconds')}` |",
        f"| Run end (UTC) | `{ended.isoformat(timespec='seconds')}` |",
        f"| Duration | **{dur:.1f} s** |",
        f"| Tickers | {', '.join(tickers)} |",
        "",
        "## Configuration (from environment)",
        "",
        *_config_lines(),
        "",
        "## Orchestrator counters",
        "",
        "| Metric | Value |",
        "|--------|-------|",
    ]
    for k, v in sorted(stats.items()):
        label = k.replace("_", " ").title()
        lines.append(f"| {label} | {v} |")

    counts = Counter(s.direction.value for s in signals)
    lines.extend(
        [
            "",
            "## Fused `TradeSignal` directions",
            "",
            "| Direction | Count |",
            "|-----------|-------|",
            f"| BUY | {counts.get('BUY', 0)} |",
            f"| SELL | {counts.get('SELL', 0)} |",
            f"| HOLD | {counts.get('HOLD', 0)} |",
            "",
            "## Trade signals (chronological)",
            "",
        ]
    )
    if not signals:
        lines.append("_No fused `TradeSignal` was emitted during this run._")
    else:
        for i, sig in enumerate(signals, 1):
            d = sig.direction.value if hasattr(sig.direction, "value") else str(sig.direction)
            lines.append(
                f"### {i}. `{sig.ticker}` → **{d}**  (raw_score={sig.raw_score:+.4f}, "
                f"conf={sig.confidence:.3f}, pos_w={sig.position_weight:.3f}, agents={sig.num_agents})"
            )
            lines.append("")
            lines.append("```")
            lines.append(format_trade_signal_message(sig))
            lines.append("```")
            lines.append("")

    lines.extend(
        [
            "---",
            "",
            "This file is **overwritten** on every `python run_pipeline.py` run (unless disabled).",
            "Path override: set `ALPHAGENT_RUN_REPORT_PATH` to a full file path.",
            "Disable: `ALPHAGENT_RUN_REPORT=0`.",
        ]
    )
    return "\n".join(lines)


def write_latest_run_report(
    *,
    repo_root: Path,
    tickers: list[str],
    started: datetime,
    orch: Any,
) -> Path | None:
    if os.environ.get("ALPHAGENT_RUN_REPORT", "1").strip().lower() in ("0", "false", "no", "off"):
        return None
    ended = datetime.now(timezone.utc)
    signals = orch.signal_history()
    stats = orch.get_stats()
    body = build_markdown(
        tickers=tickers,
        started=started,
        ended=ended,
        signals=signals,
        stats=stats,
    )
    path = _report_path(repo_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")
    return path
