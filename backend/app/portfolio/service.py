from sqlalchemy.orm import Session

from app.authentication.models import User
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

def get_user_portfolio(
    db: Session,
    user: User,
) -> list[Portfolio]:

    return (
        db.query(Portfolio)
        .filter(Portfolio.user_id == user.id)
        .all()
    )