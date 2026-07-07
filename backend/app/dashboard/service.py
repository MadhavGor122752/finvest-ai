from decimal import Decimal

from sqlalchemy.orm import Session

from app.authentication.models import User
from app.portfolio.models import Portfolio
from app.profile.models import UserProfile
from app.recommendation.service import get_recommendations
from app.sip.models import SIP

from app.dashboard.schemas import DashboardResponse


def get_dashboard(
    db: Session,
    user: User,
) -> DashboardResponse:

    profile = (
        db.query(UserProfile)
        .filter(UserProfile.user_id == user.id)
        .first()
    )

    investments = (
        db.query(Portfolio)
        .filter(Portfolio.user_id == user.id)
        .all()
    )

    sips = (
        db.query(SIP)
        .filter(
            SIP.user_id == user.id,
            SIP.status == "ACTIVE",
        )
        .all()
    )

    total_portfolio_value = Decimal("0")

    total_profit_loss = Decimal("0")

    for investment in investments:

        current_value = (
            getattr(
                investment,
                "current_value",
                investment.investment_amount,
            )
        )

        total_portfolio_value += current_value

        total_profit_loss += (
            current_value
            - investment.investment_amount
        )

    monthly_sip_amount = sum(
        sip.monthly_amount
        for sip in sips
    )

    recommendations = get_recommendations(
        db=db,
        user=user,
    )

    return DashboardResponse(
        first_name=profile.first_name if profile else "User",
        total_investments=len(investments),
        total_portfolio_value=total_portfolio_value,
        total_profit_loss=total_profit_loss,
        active_sips=len(sips),
        monthly_sip_amount=monthly_sip_amount,
        recommendations=recommendations,
    )