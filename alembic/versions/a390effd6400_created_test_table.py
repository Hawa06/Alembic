"""created test table

Revision ID: a390effd6400
Revises: 7f5f2f582aed
Create Date: 2026-09-21 15:43:23.995445

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a390effd6400'
down_revision: Union[str, Sequence[str], None] = '7f5f2f582aed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "test",
        sa.Column("name",sa.String(100),nullable=True)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("test")
