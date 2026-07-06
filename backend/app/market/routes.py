from fastapi import APIRouter

from app.market.schemas import MarketOverviewResponse
from app.market.service import get_market_overview

router = APIRouter(
    prefix="/api/v1/market",
    tags=["Market"],
)


@router.get(
    "/overview",
    response_model=MarketOverviewResponse,
)
def market_overview():

    return get_market_overview()