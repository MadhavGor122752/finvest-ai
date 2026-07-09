"""create mutual funds table

Revision ID: 062aa70400d3
Revises: c25579b5e5d1
Create Date: 2026-07-08 15:46:52.742684

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "062aa70400d3"
down_revision: Union[str, Sequence[str], None] = "c25579b5e5d1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "mutual_funds",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("scheme_code", sa.Integer(), nullable=False),
        sa.Column("scheme_name", sa.String(length=255), nullable=False),
        sa.Column("fund_house", sa.String(length=255), nullable=False),
        sa.Column(
            "category",
            sa.Enum(
                "LARGE_CAP",
                "MID_CAP",
                "SMALL_CAP",
                "FLEXI_CAP",
                "MULTI_CAP",
                "ELSS",
                "INDEX",
                "DEBT",
                "HYBRID",
                name="fundcategory",
            ),
            nullable=False,
        ),
        sa.Column(
            "risk_level",
            sa.Enum(
                "LOW",
                "MODERATE",
                "HIGH",
                name="risklevel",
            ),
            nullable=False,
        ),
        sa.Column("nav", sa.Numeric(10, 4), nullable=False),
        sa.Column("expense_ratio", sa.Numeric(5, 2), nullable=False),
        sa.Column("aum", sa.Numeric(18, 2), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        op.f("ix_mutual_funds_scheme_code"),
        "mutual_funds",
        ["scheme_code"],
        unique=True,
    )

    op.create_index(
        op.f("ix_mutual_funds_scheme_name"),
        "mutual_funds",
        ["scheme_name"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        op.f("ix_mutual_funds_scheme_name"),
        table_name="mutual_funds",
    )

    op.drop_index(
        op.f("ix_mutual_funds_scheme_code"),
        table_name="mutual_funds",
    )

    op.drop_table("mutual_funds")