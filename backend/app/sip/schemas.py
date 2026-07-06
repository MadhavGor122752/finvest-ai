from datetime import date
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class SIPCreateRequest(BaseModel):
    scheme_code: int
    scheme_name: str
    monthly_amount: Decimal = Field(gt=0)
    sip_date: int = Field(ge=1, le=28)


class SIPResponse(BaseModel):
    id: UUID

    scheme_code: int
    scheme_name: str

    monthly_amount: Decimal
    sip_date: int

    next_investment_date: date

    status: str

    model_config = ConfigDict(
        from_attributes=True,
    )


class SIPStatusUpdateRequest(BaseModel):
    status: str