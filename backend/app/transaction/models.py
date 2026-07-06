import uuid
from decimal import Decimal
from enum import Enum

from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Enum as SqlEnum

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.authentication.models import User
from app.common.models import TimestampMixin
from app.core.database import Base


class TransactionType(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class Transaction(
    TimestampMixin,
    Base,
):
    __tablename__ = "transactions"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
    )

    scheme_code: Mapped[int] = mapped_column(
        nullable=False,
    )

    scheme_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    transaction_type: Mapped[TransactionType] = mapped_column(
        SqlEnum(TransactionType),
        nullable=False,
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    nav: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    units: Mapped[Decimal] = mapped_column(
        Numeric(12, 4),
        nullable=False,
    )

    user: Mapped["User"] = relationship(
        backref="transactions",
    )