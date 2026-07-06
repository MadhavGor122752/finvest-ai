import httpx

from app.core.config import settings
from app.mutual_fund.schemas import (
    MutualFundDetailResponse,
    MutualFundResponse,
)


def search_mutual_funds(
    query: str | None = None,
) -> list[MutualFundResponse]:

    with httpx.Client(timeout=20.0) as client:
        response = client.get(settings.MF_API_BASE_URL)

    response.raise_for_status()

    funds = response.json()

    if query:
        query = query.lower()

        funds = [
            fund
            for fund in funds
            if query in fund["schemeName"].lower()
        ]

    return [
        MutualFundResponse(
            scheme_code=fund["schemeCode"],
            scheme_name=fund["schemeName"],
        )
        for fund in funds
    ]


def get_mutual_fund_details(
    scheme_code: int,
) -> MutualFundDetailResponse | None:

    with httpx.Client(timeout=20.0) as client:
        response = client.get(
            f"{settings.MF_API_BASE_URL}/{scheme_code}"
        )

    if response.status_code != 200:
        return None

    data = response.json()

    latest_nav = float(data["data"][0]["nav"])

    return MutualFundDetailResponse(
        scheme_code=scheme_code,
        scheme_name=data["meta"]["scheme_name"],
        fund_house="Live via MFAPI",
        category="Not Available",
        risk_level="Not Available",
        expense_ratio=0.0,
        nav=latest_nav,
    )