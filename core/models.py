"""
models.py — One shared shape for all pipeline events.

Each feed (price, news, filings, social) becomes a MarketEvent before agents see it.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any


class EventType(Enum):
    PRICE_UPDATE   = "price_update"    # OHLCV bar
    NEWS_ARTICLE   = "news_article"    # headline + body
    SEC_FILING     = "sec_filing"      # e.g. 10-K, 8-K
    SOCIAL_POST    = "social_post"     # e.g. StockTwits
    EARNINGS_CALL  = "earnings_call"   # transcript chunk


class DataSource(Enum):
    YFINANCE     = "yfinance"
    POLYGON      = "polygon"
    EDGAR        = "edgar"
    REUTERS_RSS  = "reuters_rss"
    REDDIT       = "reddit"
    STOCKTWITS   = "stocktwits"


@dataclass
class MarketEvent:
    """
    Normalized event for agents. Times in UTC; tickers upper-case.
    Use payload for content; raw is for debug only.
    """
    event_id:    str           # id for dedup
    event_type:  EventType
    source:      DataSource
    ticker:      str           # main symbol
    timestamp:   datetime      # when the thing happened (UTC)
    ingested_at: datetime      # when we got it
    payload:     dict          # normalized fields (see block below)
    raw:         Any = None    # raw API blob if you kept it
    confidence:  float = 1.0   # how much we trust this source (0..1)
    tags:        list  = field(default_factory=list)  # e.g. ["8-K"]

    def age_seconds(self) -> float:
        """Seconds since event time (for decay)."""
        return (datetime.utcnow() - self.timestamp).total_seconds()


# Example payload shapes (what to put in MarketEvent.payload):

# EventType.PRICE_UPDATE:
# {
#   "open": float, "high": float, "low": float,
#   "close": float, "volume": int, "interval": "1d" | "1h" | "5m"
# }

# EventType.NEWS_ARTICLE:
# {
#   "headline": str, "body": str, "url": str,
#   "sentiment_raw": str | None   # pre-scored if available
# }

# EventType.SEC_FILING:
# {
#   "form_type": str,
#   "filed_date": str,
#   "text_excerpt": str,
#   "url": str,
#   # Form 4 extras when EdgarCollector pulls the doc:
#   "transaction_code": str | None,      # first SEC transaction code, e.g. P, S
#   "transaction_codes": list[str],
#   "acquired_disposed": "A" | "D" | "mixed" | None,
#   "is_purchase": True | False | None,  # net buy / net sell / unclear
# }

# EventType.SOCIAL_POST:
# {
#   "text": str, "score": int, "num_comments": int,
#   "subreddit": str | None
# }
