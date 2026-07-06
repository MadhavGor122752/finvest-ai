from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class InvestmentCreateRequest(BaseModel):
    scheme_code: int

    scheme_name: str

    investment_amount: Decimal = Field(gt=0)

    purchase_nav: Decimal = Field(gt=0)

    units: Decimal = Field(gt=0)


class InvestmentResponse(BaseModel):
    id: UUID

    scheme_code: int

    scheme_name: str

    investment_amount: Decimal

    purchase_nav: Decimal

    units: Decimal

    model_config = ConfigDict(
        from_attributes=True,
    )