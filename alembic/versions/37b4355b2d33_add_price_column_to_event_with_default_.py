"""add price column to event with default for existing rows

Revision ID: 37b4355b2d33
Revises: a12d1a89527d
Create Date: 2025-04-05 12:40:12.571141

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37b4355b2d33'
down_revision: Union[str, None] = 'a12d1a89527d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # op.add_column(
    #     'event',
    #     sa.Column('price', sa.String(), nullable=True)
    # )

    op.execute("UPDATE event SET price = 'Бесплатно'")

    op.alter_column('event', 'price', nullable=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('event', 'price', nullable=True)
    op.execute("UPDATE event SET price = NULL")
    op.drop_column('event', 'price')
