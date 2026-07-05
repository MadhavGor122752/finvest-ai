import uuid
from decimal import Decimal
from enum import Enum

from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import Enum as SqlEnum
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.authentication.models import User
from app.common.models import TimestampMixin
from app.core.database import Base


class InvestmentLevel(str, Enum):
    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"
    ADVANCED = "ADVANCED"


class RiskTolerance(str, Enum):
    CONSERVATIVE = "CONSERVATIVE"
    MODERATE = "MODERATE"
    AGGRESSIVE = "AGGRESSIVE"


class UserProfile(
    TimestampMixin,
    Base,
):
    __tablename__ = "user_profiles"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        unique=True,
        nullable=False,
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    phone_number: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    date_of_birth: Mapped[Date] = mapped_column(
        Date,
        nullable=False,
    )

    occupation: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    monthly_income: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    investment_level: Mapped[InvestmentLevel] = mapped_column(
        SqlEnum(InvestmentLevel),
        nullable=False,
    )

    risk_tolerance: Mapped[RiskTolerance] = mapped_column(
        SqlEnum(RiskTolerance),
        nullable=False,
    )

    profile_completed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    user: Mapped["User"] = relationship(
        backref="profile",
    )