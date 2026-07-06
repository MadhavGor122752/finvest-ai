from pydantic import BaseModel
from pydantic import Field


class SIPRequest(BaseModel):
    monthly_investment: float = Field(gt=0)

    annual_return: float = Field(gt=0)

    years: int = Field(gt=0)


class SIPResponse(BaseModel):
    total_investment: float

    estimated_returns: float

    maturity_amount: float