import uuid
from decimal import Decimal
from datetime import date
from sqlalchemy import Date
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


class SIP(
    TimestampMixin,
    Base,
):
    __tablename__ = "sips"

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

    monthly_amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    sip_date: Mapped[int] = mapped_column(
        nullable=False,
    )

    next_investment_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="ACTIVE",
        nullable=False,
    )

    user: Mapped["User"] = relationship(
        backref="sips",
    )