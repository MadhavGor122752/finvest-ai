from decimal import Decimal

import httpx
from sqlalchemy.orm import Session

from app.authentication.models import User
from app.core.config import settings
from app.portfolio.models import Portfolio
from app.portfolio.schemas import InvestmentCreateRequest


def create_investment(
    db: Session,
    user: User,
    request: InvestmentCreateRequest,
) -> Portfolio:

    investment = Portfolio(
        user_id=user.id,
        scheme_code=request.scheme_code,
        scheme_name=request.scheme_name,
        investment_amount=request.investment_amount,
        purchase_nav=request.purchase_nav,
        units=request.units,
    )

    db.add(investment)
    db.commit()
    db.refresh(investment)

    return investment


def get_live_nav(
    scheme_code: int,
) -> Decimal:

    with httpx.Client(timeout=20.0) as client:
        response = client.get(
            f"{settings.MF_API_BASE_URL}/{scheme_code}"
        )

    response.raise_for_status()

    data = response.json()

    latest_nav = Decimal(data["data"][0]["nav"])

    return latest_nav


def get_user_portfolio(
    db: Session,
    user: User,
) -> list[Portfolio]:

    investments = (
        db.query(Portfolio)
        .filter(Portfolio.user_id == user.id)
        .all()
    )

    for investment in investments:

        current_nav = get_live_nav(
            investment.scheme_code
        )

        current_value = (
            investment.units * current_nav
        ).quantize(Decimal("0.01"))

        profit_loss = (
            current_value
            - investment.investment_amount
        ).quantize(Decimal("0.01"))

        return_percentage = (
            (
                profit_loss
                / investment.investment_amount
            ) * Decimal("100")
        ).quantize(Decimal("0.01"))

        investment.current_nav = current_nav
        investment.current_value = current_value
        investment.profit_loss = profit_loss
        investment.return_percentage = return_percentage

    return investments