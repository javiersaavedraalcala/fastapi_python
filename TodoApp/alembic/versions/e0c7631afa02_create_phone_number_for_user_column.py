"""Create phone number for user column

Revision ID: e0c7631afa02
Revises: 
Create Date: 2025-02-11 14:50:32.541929

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0c7631afa02'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone_number", sa.String(14), nullable=True))


def downgrade() -> None:
    op.drop_column("users", "phone_number")
