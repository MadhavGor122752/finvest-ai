from sqlalchemy.orm import Session

from app.authentication.models import User
from app.profile.models import UserProfile
from app.recommendation.ai_engine import recommend_funds
from app.recommendation.schemas import RecommendationResponse


def get_recommendations(
    db: Session,
    user: User,
) -> list[RecommendationResponse]:

    profile = (
        db.query(UserProfile)
        .filter(UserProfile.user_id == user.id)
        .first()
    )

    if not profile:
        return []

    risk = profile.risk_tolerance.value
    level = profile.investment_level.value
    income = float(profile.monthly_income)

    funds = recommend_funds(
        risk_tolerance=risk,
        investment_level=level,
        monthly_income=income,
    )

    recommendations = []

    for _, fund in funds.iterrows():

        reason = (
            f"Recommended because it matches your "
            f"{risk.lower()} risk profile, "
            f"has a {int(fund['rating'])}-star rating, "
            f"and strong historical performance."
        )

        recommendations.append(
            RecommendationResponse(
                scheme_code=0,
                scheme_name=fund["scheme_name"],
                category=fund["category"],
                risk_level=risk.title(),
                recommendation_score=int(fund["score"]),
                reason=reason,
            )
        )

    return recommendations