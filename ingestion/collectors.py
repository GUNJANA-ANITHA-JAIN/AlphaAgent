"""
collectors.py — Pull price, news, SEC filings, StockTwits.

Each class: fetch() -> raw rows, normalize() -> MarketEvent. Needs
yfinance, feedparser, requests.
"""

import os
import uuid
import logging
from datetime import datetime, timezone
from typing import Optional

import yfinance as yf
import feedparser
import requests

from core.models import MarketEvent, EventType, DataSource
from ingestion.base_collector import BaseCollector, DedupStore, SourceUnavailableError
from ingestion.form4_enrichment import enrich_form4_from_url

logger = logging.getLogger(__name__)


# --- Price: yfinance daily bars ---

class PriceCollector(BaseCollector):
    """
    Daily OHLCV per ticker. yfinance is fine for demos; live may use a paid feed.
    auto_adjust=True matches split-adjusted history (good for simple backtests).
    """

    def __init__(self, dedup: DedupStore, tickers: list[str], period: str = "5d"):
        super().__init__(dedup, tickers)
        self.period = period  # yfinance window string

    def fetch(self, ticker: str) -> list[dict]:
        try:
            # history() avoids broken MultiIndex columns from download().
            hist = yf.Ticker(ticker).history(period=self.period, auto_adjust=True)
            if hist.empty:
                return []
            records = []
            for ts, row in hist.iterrows():
                records.append({
                    "ticker": ticker,
                    "timestamp": ts.to_pydatetime().replace(tzinfo=timezone.utc),
                    "open": float(row["Open"]),
                    "high": float(row["High"]),
                    "low": float(row["Low"]),
                    "close": float(row["Close"]),
                    "volume": int(row["Volume"]),
                })
            return records
        except Exception as e:
            raise SourceUnavailableError(f"yFinance failed for {ticker}: {e}")

    def normalize(self, raw: dict, ticker: str) -> Optional[MarketEvent]:
        if any(v is None for v in [raw.get("close"), raw.get("volume")]):
            return None
        return MarketEvent(
            event_id=str(uuid.uuid4()),
            event_type=EventType.PRICE_UPDATE,
            source=DataSource.YFINANCE,
            ticker=ticker,
            timestamp=raw["timestamp"],
            ingested_at=datetime.utcnow(),
            payload={
                "open":     raw["open"],
                "high":     raw["high"],
                "low":      raw["low"],
                "close":    raw["close"],
                "volume":   raw["volume"],
                "interval": "1d",
            },
            raw=raw,
        )


# --- News: RSS ---

NEWS_FEEDS = {
    "yahoo_finance": "https://finance.yahoo.com/news/rssindex",
    "reuters_markets": "https://feeds.reuters.com/reuters/businessNews",
    "seeking_alpha": "https://seekingalpha.com/feed.xml",
}

class NewsCollector(BaseCollector):
    """
    RSS feeds; keeps items whose title/summary mention the ticker (string match).
    Feed time is often "published" time, not true event time—fine for demos only.
    """

    def __init__(self, dedup: DedupStore, tickers: list[str], feeds: dict = None):
        super().__init__(dedup, tickers)
        self.feeds = feeds or NEWS_FEEDS

    def fetch(self, ticker: str) -> list[dict]:
        results = []
        for feed_name, feed_url in self.feeds.items():
            try:
                parsed = feedparser.parse(feed_url)
                for entry in parsed.entries:
                    title = entry.get("title", "")
                    summary = entry.get("summary", "")
                    # crude ticker filter
                    if ticker.upper() not in (title + summary).upper():
                        continue
                    results.append({
                        "feed": feed_name,
                        "ticker": ticker,
                        "title": title,
                        "summary": summary,
                        "url": entry.get("link", ""),
                        "published": entry.get("published_parsed"),
                    })
            except Exception as e:
                logger.warning(f"RSS feed {feed_name} failed: {e}")
        return results

    def normalize(self, raw: dict, ticker: str) -> Optional[MarketEvent]:
        published = raw.get("published")
        if published:
            ts = datetime(*published[:6], tzinfo=timezone.utc)
        else:
            ts = datetime.utcnow().replace(tzinfo=timezone.utc)

        headline = raw.get("title", "").strip()
        if not headline:
            return None

        return MarketEvent(
            event_id=str(uuid.uuid4()),
            event_type=EventType.NEWS_ARTICLE,
            source=DataSource.REUTERS_RSS,
            ticker=ticker,
            timestamp=ts,
            ingested_at=datetime.utcnow(),
            payload={
                "headline": headline,
                "body":     raw.get("summary", ""),
                "url":      raw.get("url", ""),
                "feed":     raw.get("feed", ""),
                "sentiment_raw": None,  # filled later by sentiment agent
            },
            raw=raw,
            confidence=0.8,  # RSS is weaker than a direct news API
        )


# --- SEC: EDGAR filings ---

EDGAR_HEADERS = {"User-Agent": "AlphaAgent research@example.com"}  # SEC wants a user-agent

class EdgarCollector(BaseCollector):
    """
    Recent 8-K / 10-K / 10-Q / Form 4 per ticker from EDGAR JSON.
    Free; throttle in production. Filing date != event date for strict backtests.
    """

    TICKER_TO_CIK_URL = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&ticker={ticker}&type=&dateb=&owner=include&count=1&search_text=&output=atom"
    SUBMISSIONS_URL   = "https://data.sec.gov/submissions/CIK{cik}.json"
    FILING_BASE_URL   = "https://www.sec.gov/Archives/edgar/data/{cik}/{accession}/{filename}"

    FORM_TYPES = ["8-K", "10-K", "10-Q", "4"]

    def __init__(self, dedup: DedupStore, tickers: list[str]):
        super().__init__(dedup, tickers)
        self._cik_cache: dict[str, str] = {}

    def _get_cik(self, ticker: str) -> Optional[str]:
        """Ticker to 10-digit CIK."""
        if ticker in self._cik_cache:
            return self._cik_cache[ticker]
        try:
            # company_tickers.json is faster than ATOM lookup
            resp = requests.get(
                "https://www.sec.gov/files/company_tickers.json",
                headers=EDGAR_HEADERS, timeout=10
            )
            data = resp.json()
            for entry in data.values():
                if entry.get("ticker", "").upper() == ticker.upper():
                    cik = str(entry["cik_str"]).zfill(10)
                    self._cik_cache[ticker] = cik
                    return cik
        except Exception as e:
            logger.warning(f"CIK lookup failed for {ticker}: {e}")
        return None

    def fetch(self, ticker: str) -> list[dict]:
        cik = self._get_cik(ticker)
        if not cik:
            return []
        try:
            resp = requests.get(
                self.SUBMISSIONS_URL.format(cik=cik),
                headers=EDGAR_HEADERS, timeout=15
            )
            data = resp.json()
            filings = data.get("filings", {}).get("recent", {})
            results = []
            for i, form_type in enumerate(filings.get("form", [])):
                if form_type not in self.FORM_TYPES:
                    continue
                results.append({
                    "ticker":       ticker,
                    "cik":          cik,
                    "form_type":    form_type,
                    "filed_date":   filings["filingDate"][i],
                    "accession":    filings["accessionNumber"][i].replace("-", ""),
                    "primary_doc":  filings["primaryDocument"][i],
                })
                if len(results) >= 10:  # keep last 10
                    break
            return results
        except Exception as e:
            raise SourceUnavailableError(f"EDGAR fetch failed for {ticker}: {e}")

    def normalize(self, raw: dict, ticker: str) -> Optional[MarketEvent]:
        try:
            filed_date = datetime.strptime(raw["filed_date"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
        except Exception:
            return None

        doc_url = self.FILING_BASE_URL.format(
            cik=raw["cik"],
            accession=raw["accession"],
            filename=raw["primary_doc"],
        )
        payload: dict = {
            "form_type": raw["form_type"],
            "filed_date": raw["filed_date"],
            "text_excerpt": "",
            "url": doc_url,
        }
        if raw.get("form_type") == "4":
            fetch_on = os.environ.get("ALPHAGENT_FORM4_FETCH", "1").strip().lower() not in (
                "0",
                "false",
                "no",
            )
            if fetch_on:
                tmo = float(os.environ.get("ALPHAGENT_FORM4_FETCH_TIMEOUT", "12"))
                ex = enrich_form4_from_url(doc_url, timeout=tmo)
                payload["transaction_code"] = ex.get("transaction_code")
                payload["transaction_codes"] = ex.get("transaction_codes") or []
                payload["acquired_disposed"] = ex.get("acquired_disposed")
                payload["is_purchase"] = ex.get("is_purchase")
            else:
                payload["transaction_code"] = None
                payload["transaction_codes"] = []
                payload["acquired_disposed"] = None
                payload["is_purchase"] = None

        return MarketEvent(
            event_id=str(uuid.uuid4()),
            event_type=EventType.SEC_FILING,
            source=DataSource.EDGAR,
            ticker=ticker,
            timestamp=filed_date,
            ingested_at=datetime.utcnow(),
            payload=payload,
            raw=raw,
            confidence=1.0,  # treat SEC as ground truth
            tags=[raw["form_type"]],
        )


# --- StockTwits public stream ---

STOCKTWITS_HEADERS = {
    # clear User-Agent reduces random blocks
    "User-Agent": "AlphaAgent/1.0 (research; contact: research@example.com)",
    "Accept": "application/json",
}


class StockTwitsCollector(BaseCollector):
    """Latest messages for a symbol (free tier, no key)."""

    def __init__(self, dedup: DedupStore, tickers: list[str], max_messages: int = 30):
        super().__init__(dedup, tickers)
        self.max_messages = max_messages

    def fetch(self, ticker: str) -> list[dict]:
        url = f"https://api.stocktwits.com/api/2/streams/symbol/{ticker}.json"
        try:
            resp = requests.get(url, headers=STOCKTWITS_HEADERS, timeout=15)
            resp.raise_for_status()
            payload = resp.json()
        except Exception as e:
            raise SourceUnavailableError(f"StockTwits failed for {ticker}: {e}")

        if not isinstance(payload, dict):
            raise SourceUnavailableError(f"StockTwits unexpected JSON for {ticker}: {type(payload).__name__}")
        messages = payload.get("messages") or []
        if not isinstance(messages, list):
            messages = []
        results = []
        for msg in messages[: self.max_messages]:
            if not isinstance(msg, dict):
                continue
            body = (msg.get("body") or "").strip()
            if not body:
                continue

            user = msg.get("user")
            if not isinstance(user, dict):
                user = {}
            username = user.get("username") or "unknown"
            mid = msg.get("id")
            link = f"https://stocktwits.com/{username}/message/{mid}" if mid else ""

            likes_obj = msg.get("likes")
            if isinstance(likes_obj, dict):
                likes = int(likes_obj.get("total") or 0)
            elif isinstance(likes_obj, int):
                likes = likes_obj
            else:
                likes = 0

            discussion = msg.get("discussion")
            if not isinstance(discussion, dict):
                discussion = {}
            replies = int(discussion.get("count") or discussion.get("message_count") or 0)

            created = msg.get("created_at") or ""
            results.append({
                "ticker":        ticker,
                "text":          body,
                "score":         likes,
                "num_comments":  replies,
                "subreddit":     None,
                "created_at":    created,
                "url":           link,
                "username":      username,
                "message_id":    mid,
                "raw_message":   msg,
            })
        return results

    def normalize(self, raw: dict, ticker: str) -> Optional[MarketEvent]:
        text = raw.get("text", "").strip()
        if not text:
            return None

        ca = raw.get("created_at") or ""
        try:
            ts = datetime.fromisoformat(ca.replace("Z", "+00:00"))
        except ValueError:
            ts = datetime.now(timezone.utc)

        likes = int(raw.get("score") or 0)
        confidence = min(likes / 500.0, 1.0) if likes > 0 else 0.35

        uname = raw.get("username") or ""
        tags = ["social", "stocktwits"]
        if uname:
            tags.append(uname)

        return MarketEvent(
            event_id=str(uuid.uuid4()),
            event_type=EventType.SOCIAL_POST,
            source=DataSource.STOCKTWITS,
            ticker=ticker,
            timestamp=ts,
            ingested_at=datetime.utcnow(),
            payload={
                "text":          text,
                "score":         likes,
                "num_comments":  raw.get("num_comments", 0),
                "subreddit":     None,
                "url":           raw.get("url", ""),
                "message_id":    raw.get("message_id"),
            },
            raw=raw.get("raw_message"),
            confidence=confidence,
            tags=tags,
        )
