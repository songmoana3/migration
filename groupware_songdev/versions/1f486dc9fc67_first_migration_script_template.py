"""First migration script template

Revision ID: 1f486dc9fc67
Revises: 
Create Date: 2023-01-19 10:17:43.896087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f486dc9fc67'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('')


def downgrade() -> None:
    pass
