"""create phone number for user column

Revision ID: 39e3ed053303
Revises: 
Create Date: 2025-04-16 08:29:25.379762

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '39e3ed053303'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(length=10), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
