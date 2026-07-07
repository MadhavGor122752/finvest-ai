from sqlalchemy.orm import Session

from app.authentication.models import User
from app.profile.models import (
    InvestmentLevel,
    RiskTolerance,
    UserProfile,
)
from app.recommendation.schemas import RecommendationResponse


FUNDS = [
    {
        "scheme_code": 119551,
        "scheme_name": "Axis Bluechip Fund - Direct Plan - Growth",
        "category": "Large Cap",
        "risk": RiskTolerance.CONSERVATIVE,
    },
    {
        "scheme_code": 122639,
        "scheme_name": "Parag Parikh Flexi Cap Fund - Direct Plan - Growth",
        "category": "Flexi Cap",
        "risk": RiskTolerance.MODERATE,
    },
    {
        "scheme_code": 120503,
        "scheme_name": "SBI Small Cap Fund - Direct Plan - Growth",
        "category": "Small Cap",
        "risk": RiskTolerance.AGGRESSIVE,
    },
]


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

    recommendations = []

    for fund in FUNDS:

        score = 40

        if fund["risk"] == profile.risk_tolerance:
            score += 50

        if (
            profile.investment_level == InvestmentLevel.ADVANCED
            and fund["risk"] == RiskTolerance.AGGRESSIVE
        ):
            score += 10

        elif (
            profile.investment_level == InvestmentLevel.INTERMEDIATE
            and fund["risk"] == RiskTolerance.MODERATE
        ):
            score += 10

        elif (
            profile.investment_level == InvestmentLevel.BEGINNER
            and fund["risk"] == RiskTolerance.CONSERVATIVE
        ):
            score += 10

        recommendations.append(
            RecommendationResponse(
                scheme_code=fund["scheme_code"],
                scheme_name=fund["scheme_name"],
                category=fund["category"],
                risk_level=fund["risk"].value.title(),
                recommendation_score=score,
                reason=(
                    f"Recommended based on your "
                    f"{profile.risk_tolerance.value.lower()} "
                    f"risk tolerance and "
                    f"{profile.investment_level.value.lower()} "
                    f"investment level."
                ),
            )
        )

    recommendations.sort(
        key=lambda x: x.recommendation_score,
        reverse=True,
    )

    return recommendations[:3]