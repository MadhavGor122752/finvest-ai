from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query

from app.mutual_fund.schemas import (
    MutualFundDetailResponse,
    MutualFundResponse,
)
from app.mutual_fund.service import (
    get_mutual_fund_details,
    search_mutual_funds,
)

router = APIRouter(
    prefix="/api/v1/mutual-funds",
    tags=["Mutual Funds"],
)


@router.get(
    "/search",
    response_model=list[MutualFundResponse],
)
def search(
    query: str | None = Query(
        default=None,
        description="Search by mutual fund name",
    ),
):
    return search_mutual_funds(query)


@router.get(
    "/{scheme_code}",
    response_model=MutualFundDetailResponse,
)
def get_details(
    scheme_code: int,
):

    fund = get_mutual_fund_details(scheme_code)

    if fund is None:
        raise HTTPException(
            status_code=404,
            detail="Mutual fund not found.",
        )

    return fund