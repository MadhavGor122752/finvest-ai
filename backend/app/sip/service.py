from math import pow

from app.sip.schemas import (
    SIPRequest,
    SIPResponse,
)


def calculate_sip(
    request: SIPRequest,
) -> SIPResponse:
    """
    Calculate SIP maturity amount.

    Formula:
    M = P × [((1 + i)^n - 1) / i] × (1 + i)
    """

    monthly_rate = request.annual_return / 12 / 100

    months = request.years * 12

    maturity_amount = (
        request.monthly_investment
        * (
            (pow(1 + monthly_rate, months) - 1)
            / monthly_rate
        )
        * (1 + monthly_rate)
    )

    total_investment = (
        request.monthly_investment
        * months
    )

    estimated_returns = (
        maturity_amount
        - total_investment
    )

    return SIPResponse(
        total_investment=round(total_investment, 2),
        estimated_returns=round(
            estimated_returns,
            2,
        ),
        maturity_amount=round(
            maturity_amount,
            2,
        ),
    )