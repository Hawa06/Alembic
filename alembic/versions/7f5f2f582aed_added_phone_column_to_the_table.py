"""added phone column to the table

Revision ID: 7f5f2f582aed
Revises: 3a3b5db2fbd8
Create Date: 2026-09-21 12:49:05.851866

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f5f2f582aed'
down_revision: Union[str, Sequence[str], None] = '3a3b5db2fbd8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "user",
        sa.Column("phone",sa.String(10),unique=True,nullable=True)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("user","phone")
