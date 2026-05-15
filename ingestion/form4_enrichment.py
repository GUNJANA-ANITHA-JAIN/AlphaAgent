"""
Download Form 4 XML from EDGAR and pull insider trade hints.

Fills payload fields used by EdgarCollector. Keep timeouts modest; throttle if you burst requests.
"""

from __future__ import annotations

import logging
import os
import re
import threading
import time
import xml.etree.ElementTree as ET
from typing import Any

import requests

logger = logging.getLogger(__name__)

SEC_REQUEST_HEADERS = {"User-Agent": "AlphaAgent research@example.com"}

# Common SEC transaction codes when XML lacks A/D. P/B often mean buy-like.
_PURCHASE_CODES = frozenset({"P", "B", "C", "I", "L", "W"})
_SALE_CODES = frozenset({"S", "G", "F"})


def _local_tag(tag: str | None) -> str:
    if not tag:
        return ""
    return tag.split("}", 1)[-1] if "}" in tag else tag


def parse_form4_document(content: bytes) -> dict[str, Any]:
    """Parse Form 4 XML for buy/sell codes. Always returns the four keys below."""
    out: dict[str, Any] = {
        "transaction_code": None,
        "transaction_codes": [],
        "acquired_disposed": None,
        "is_purchase": None,
    }
    if not content or len(content) < 50:
        return out

    text = content.decode("utf-8", errors="ignore")
    # Some filings are HTML; try XML first, else regex on text.
    ad_values: list[str] = []
    tx_codes: list[str] = []

    try:
        root = ET.fromstring(content[:800_000])
        for el in root.iter():
            ln = _local_tag(el.tag)
            if ln == "transactionCode" and el.text:
                t = el.text.strip().upper()
                if t and t not in tx_codes:
                    tx_codes.append(t)
            if ln == "transactionAcquiredDisposedCode":
                for ch in el:
                    if _local_tag(ch.tag) == "value" and ch.text:
                        v = ch.text.strip().upper()
                        if v in ("A", "D"):
                            ad_values.append(v)
    except ET.ParseError:
        pass

    if not ad_values:
        # regex fallback for A/D values
        for m in re.finditer(
            r"<transactionAcquiredDisposedCode>[^<]*<value>\s*([AD])\s*</value>",
            text,
            re.I | re.DOTALL,
        ):
            ad_values.append(m.group(1).upper())

    if not tx_codes:
        for m in re.finditer(
            r"<transactionCode>\s*([A-Za-z])\s*</transactionCode>", text
        ):
            c = m.group(1).upper()
            if c and c not in tx_codes:
                tx_codes.append(c)

    out["transaction_codes"] = tx_codes[:12]
    out["transaction_code"] = tx_codes[0] if tx_codes else None

    has_a = "A" in ad_values
    has_d = "D" in ad_values
    if has_a and not has_d:
        out["acquired_disposed"] = "A"
        out["is_purchase"] = True
    elif has_d and not has_a:
        out["acquired_disposed"] = "D"
        out["is_purchase"] = False
    elif has_a and has_d:
        out["acquired_disposed"] = "mixed"
        out["is_purchase"] = None
    else:
        # No A/D in XML — infer weakly from first transaction code
        tc = out["transaction_code"]
        if tc in _PURCHASE_CODES:
            out["acquired_disposed"] = None
            out["is_purchase"] = True
        elif tc in _SALE_CODES:
            out["acquired_disposed"] = None
            out["is_purchase"] = False

    return out


_SEC_LOCK = threading.Lock()
_SEC_LAST_MONO = 0.0


def _sec_request_throttle() -> None:
    delay_raw = os.environ.get("ALPHAGENT_SEC_REQUEST_DELAY_SEC") or os.environ.get(
        "ALPHAGENT_FORM4_FETCH_DELAY_SEC", "0.12"
    )
    delay = float(delay_raw)
    if delay <= 0:
        return
    global _SEC_LAST_MONO
    with _SEC_LOCK:
        now = time.monotonic()
        wait = delay - (now - _SEC_LAST_MONO)
        if wait > 0:
            time.sleep(wait)
        _SEC_LAST_MONO = time.monotonic()


def enrich_form4_from_url(url: str, *, timeout: float = 12.0) -> dict[str, Any]:
    """GET filing URL and parse; on error return empty-ish dict."""
    try:
        _sec_request_throttle()
        resp = requests.get(url, headers=SEC_REQUEST_HEADERS, timeout=timeout)
        resp.raise_for_status()
        body = resp.content
        if len(body) > 900_000:
            body = body[:900_000]
        parsed = parse_form4_document(body)
        if not parsed.get("transaction_codes") and parsed.get("is_purchase") is None:
            logger.debug("Form 4 parse: no transaction hints from %s", url[:80])
        return parsed
    except Exception as e:
        logger.debug("Form 4 fetch/parse failed %s: %s", url[:80], e)
        return {
            "transaction_code": None,
            "transaction_codes": [],
            "acquired_disposed": None,
            "is_purchase": None,
        }
