from datetime import datetime

import httpx

from app.market.schemas import MarketOverviewResponse


def get_market_overview() -> MarketOverviewResponse:
    try:
        with httpx.Client(timeout=10.0) as client:
            response = client.get("https://api.mfapi.in/mf")
            print(f"MF API Status: {response.status_code}")

    except Exception as e:
        print(f"MF API unavailable: {e}")

    return MarketOverviewResponse(
        market_status="OPEN",
        nifty_50=25240.85,
        sensex=82890.94,
        market_sentiment="Bullish",
        last_updated=datetime.now(),
    )