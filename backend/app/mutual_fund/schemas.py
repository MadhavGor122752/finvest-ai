from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.mutual_fund.models import (
    FundCategory,
    RiskLevel,
)


class MutualFundCreateRequest(BaseModel):
    scheme_code: int
    scheme_name: str
    fund_house: str
    category: FundCategory
    risk_level: RiskLevel
    nav: Decimal
    expense_ratio: Decimal
    aum: Decimal


class MutualFundUpdateRequest(BaseModel):
    scheme_name: str
    fund_house: str
    category: FundCategory
    risk_level: RiskLevel
    nav: Decimal
    expense_ratio: Decimal
    aum: Decimal
    is_active: bool


class MutualFundResponse(BaseModel):
    id: UUID
    scheme_code: int
    scheme_name: str
    fund_house: str
    category: FundCategory
    risk_level: RiskLevel
    nav: Decimal
    expense_ratio: Decimal
    aum: Decimal
    is_active: bool

    model_config = ConfigDict(
        from_attributes=True,
    )