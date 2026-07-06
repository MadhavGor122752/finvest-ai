from decimal import Decimal
from enum import Enum
from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class TransactionType(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class TransactionCreateRequest(BaseModel):
    scheme_code: int

    scheme_name: str

    transaction_type: TransactionType

    amount: Decimal = Field(gt=0)

    nav: Decimal = Field(gt=0)

    units: Decimal = Field(gt=0)


class TransactionResponse(BaseModel):
    id: UUID

    scheme_code: int

    scheme_name: str

    transaction_type: TransactionType

    amount: Decimal

    nav: Decimal

    units: Decimal

    model_config = ConfigDict(
        from_attributes=True,
    )