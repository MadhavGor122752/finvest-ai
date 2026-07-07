"""add user roles

Revision ID: c25579b5e5d1
Revises: 2268707a3444
Create Date: 2026-07-07 13:57:26.866448

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c25579b5e5d1'
down_revision: Union[str, Sequence[str], None] = '2268707a3444'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    user_role = sa.Enum(
        "USER",
        "ADMIN",
        name="userrole",
    )

    user_role.create(
        op.get_bind(),
        checkfirst=True,
    )

    op.add_column(
        "users",
        sa.Column(
            "role",
            user_role,
            nullable=False,
            server_default="USER",
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_column(
        "users",
        "role",
    )

    user_role = sa.Enum(
        "USER",
        "ADMIN",
        name="userrole",
    )

    user_role.drop(
        op.get_bind(),
        checkfirst=True,
    )
