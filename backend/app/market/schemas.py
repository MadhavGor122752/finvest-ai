from datetime import datetime

from pydantic import BaseModel


class MarketOverviewResponse(BaseModel):
    market_status: str

    nifty_50: float

    sensex: float

    market_sentiment: str

    last_updated: datetime