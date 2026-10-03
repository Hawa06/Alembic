"""created user schema

Revision ID: 3a3b5db2fbd8
Revises: 
Create Date: 2026-09-21 12:04:22.678976

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3a3b5db2fbd8'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'user',
        sa.Column("id",sa.Integer,primary_key=True),
        sa.Column("username",sa.String(100),nullable=False),
        sa.Column("email",sa.String(100),unique=True,nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('user')
