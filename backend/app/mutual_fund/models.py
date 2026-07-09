import uuid
from decimal import Decimal
from enum import Enum

from sqlalchemy import Boolean
from sqlalchemy import Enum as SqlEnum
from sqlalchemy import Numeric
from sqlalchemy import String

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.common.models import TimestampMixin
from app.core.database import Base


class FundCategory(str, Enum):
    LARGE_CAP = "LARGE_CAP"
    MID_CAP = "MID_CAP"
    SMALL_CAP = "SMALL_CAP"
    FLEXI_CAP = "FLEXI_CAP"
    MULTI_CAP = "MULTI_CAP"
    ELSS = "ELSS"
    INDEX = "INDEX"
    DEBT = "DEBT"
    HYBRID = "HYBRID"


class RiskLevel(str, Enum):
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"


class MutualFund(
    TimestampMixin,
    Base,
):
    __tablename__ = "mutual_funds"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    scheme_code: Mapped[int] = mapped_column(
        unique=True,
        nullable=False,
        index=True,
    )

    scheme_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    fund_house: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    category: Mapped[FundCategory] = mapped_column(
        SqlEnum(FundCategory),
        nullable=False,
    )

    risk_level: Mapped[RiskLevel] = mapped_column(
        SqlEnum(RiskLevel),
        nullable=False,
    )

    nav: Mapped[Decimal] = mapped_column(
        Numeric(10, 4),
        nullable=False,
    )

    expense_ratio: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        nullable=False,
    )

    aum: Mapped[Decimal] = mapped_column(
        Numeric(18, 2),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )