from decimal import Decimal

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.authentication.dependencies import get_current_user
from app.authentication.models import User
from app.core.database import get_db

from app.portfolio.schemas import (
    InvestmentCreateRequest,
    InvestmentResponse,
)
from app.portfolio.service import (
    create_investment,
    get_user_portfolio,
)

router = APIRouter(
    prefix="/api/v1/portfolio",
    tags=["Portfolio"],
)


@router.post(
    "/invest",
    response_model=InvestmentResponse,
)
def invest(
    request: InvestmentCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    investment = create_investment(
        db=db,
        user=current_user,
        request=request,
    )

    investment.current_nav = investment.purchase_nav
    investment.current_value = investment.investment_amount
    investment.profit_loss = Decimal("0.00")
    investment.return_percentage = Decimal("0.00")

    return InvestmentResponse.model_validate(investment)


@router.get(
    "/",
    response_model=list[InvestmentResponse],
)
def get_portfolio(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    investments = get_user_portfolio(
        db=db,
        user=current_user,
    )

    return [
        InvestmentResponse.model_validate(investment)
        for investment in investments
    ]