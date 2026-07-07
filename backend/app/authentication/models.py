import uuid
from enum import Enum

from sqlalchemy import Boolean
from sqlalchemy import Enum as SqlEnum
from sqlalchemy import String

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.common.models import TimestampMixin
from app.core.database import Base


class UserRole(str, Enum):
    USER = "USER"
    ADMIN = "ADMIN"


class User(
    TimestampMixin,
    Base,
):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    is_email_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    role: Mapped[UserRole] = mapped_column(
        SqlEnum(UserRole),
        nullable=False,
        default=UserRole.USER,
    )