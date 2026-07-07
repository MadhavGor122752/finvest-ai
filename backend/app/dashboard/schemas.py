from decimal import Decimal

from pydantic import BaseModel

from app.recommendation.schemas import RecommendationResponse


class DashboardResponse(BaseModel):
    first_name: str

    total_investments: int

    total_portfolio_value: Decimal

    total_profit_loss: Decimal

    active_sips: int

    monthly_sip_amount: Decimal

    recommendations: list[RecommendationResponse]