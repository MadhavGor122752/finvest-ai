from pydantic import BaseModel


class RecommendationResponse(BaseModel):
    scheme_code: int
    scheme_name: str
    category: str
    risk_level: str
    recommendation_score: int
    reason: str