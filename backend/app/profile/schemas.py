from datetime import date
from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from app.profile.models import (
    InvestmentLevel,
    RiskTolerance,
)


class ProfileCreateRequest(BaseModel):

    first_name: str = Field(
        min_length=2,
        max_length=100,
    )

    last_name: str = Field(
        min_length=2,
        max_length=100,
    )

    phone_number: str = Field(
        min_length=10,
        max_length=20,
    )

    date_of_birth: date

    occupation: str = Field(
        min_length=2,
        max_length=100,
    )

    monthly_income: Decimal

    investment_level: InvestmentLevel

    risk_tolerance: RiskTolerance


class ProfileResponse(BaseModel):

    id: UUID

    first_name: str

    last_name: str

    phone_number: str

    date_of_birth: date

    occupation: str

    monthly_income: Decimal

    investment_level: InvestmentLevel

    risk_tolerance: RiskTolerance

    profile_completed: bool

    model_config = ConfigDict(
        from_attributes=True,
    )