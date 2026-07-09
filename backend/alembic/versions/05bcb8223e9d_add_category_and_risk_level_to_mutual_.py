"""add category and risk level to mutual funds"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "05bcb8223e9d"
down_revision: Union[str, Sequence[str], None] = "062aa70400d3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    fund_category = sa.Enum(
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
    )

    risk_level = sa.Enum(
        "LOW",
        "MODERATE",
        "HIGH",
        name="risklevel",
    )

    # Create enum types
    fund_category.create(op.get_bind(), checkfirst=True)
    risk_level.create(op.get_bind(), checkfirst=True)

    # Add columns
    op.add_column(
        "mutual_funds",
        sa.Column("category", fund_category, nullable=True),
    )

    op.add_column(
        "mutual_funds",
        sa.Column("risk_level", risk_level, nullable=True),
    )


def downgrade() -> None:
    op.drop_column("mutual_funds", "risk_level")
    op.drop_column("mutual_funds", "category")