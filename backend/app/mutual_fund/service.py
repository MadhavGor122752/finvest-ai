from app.mutual_fund.schemas import (
    MutualFundDetailResponse,
    MutualFundResponse,
)

FUNDS = [
    MutualFundResponse(
        scheme_code=119551,
        scheme_name="Axis Bluechip Fund Direct Growth",
    ),
    MutualFundResponse(
        scheme_code=120503,
        scheme_name="SBI Small Cap Fund Direct Growth",
    ),
    MutualFundResponse(
        scheme_code=118834,
        scheme_name="Parag Parikh Flexi Cap Fund Direct Growth",
    ),
]


def search_mutual_funds(
    query: str | None = None,
) -> list[MutualFundResponse]:

    if not query:
        return FUNDS

    query = query.lower()

    return [
        fund
        for fund in FUNDS
        if query in fund.scheme_name.lower()
    ]


def get_mutual_fund_details(
    scheme_code: int,
) -> MutualFundDetailResponse | None:

    details = {
        119551: MutualFundDetailResponse(
            scheme_code=119551,
            scheme_name="Axis Bluechip Fund Direct Growth",
            fund_house="Axis Mutual Fund",
            category="Large Cap",
            risk_level="Moderate",
            expense_ratio=0.54,
            nav=72.48,
        ),
        120503: MutualFundDetailResponse(
            scheme_code=120503,
            scheme_name="SBI Small Cap Fund Direct Growth",
            fund_house="SBI Mutual Fund",
            category="Small Cap",
            risk_level="High",
            expense_ratio=0.68,
            nav=156.20,
        ),
        118834: MutualFundDetailResponse(
            scheme_code=118834,
            scheme_name="Parag Parikh Flexi Cap Fund Direct Growth",
            fund_house="PPFAS Mutual Fund",
            category="Flexi Cap",
            risk_level="Moderately High",
            expense_ratio=0.63,
            nav=89.75,
        ),
    }

    return details.get(scheme_code)