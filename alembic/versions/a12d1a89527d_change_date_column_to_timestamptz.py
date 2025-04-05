"""Change date column to timestamptz

Revision ID: a12d1a89527d
Revises: 08e59baa9617
Create Date: 2025-04-05 10:10:38.193941

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a12d1a89527d'
down_revision: Union[str, None] = '08e59baa9617'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("ALTER TABLE event ALTER COLUMN date TYPE TIMESTAMP WITH TIME ZONE USING date AT TIME ZONE 'UTC'")


def downgrade() -> None:
    """Downgrade schema."""
    pass
