from fastapi import APIRouter

from app.mutual_fund.schemas import (
    MutualFundDetailResponse,
    MutualFundResponse,
)
from app.mutual_fund.service import (
    get_mutual_fund_details,
    search_mutual_funds,
)

router = APIRouter(
    prefix="/api/v1/mutual-fund",
    tags=["Mutual Fund"],
)


@router.get(
    "/search",
    response_model=list[MutualFundResponse],
)
def search_funds(
    query: str | None = None,
):

    return search_mutual_funds(query)


@router.get(
    "/{scheme_code}",
    response_model=MutualFundDetailResponse,
)
def fund_details(
    scheme_code: int,
):

    return get_mutual_fund_details(scheme_code)