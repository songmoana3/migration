"""First migration script template

Revision ID: 1f486dc9fc67
Revises: 
Create Date: 2023-01-19 10:17:43.896087

"""
from alembic import op
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import LONGTEXT


# revision identifiers, used by Alembic.
revision = '1f486dc9fc67'
down_revision = None
branch_labels = None
depends_on = None

# Create img_url Column at notice, work_management table

def upgrade():
    op.add_column('groupware_notice', Column('img_url', LONGTEXT))
    op.add_column('groupware_work_management', Column('img_url', LONGTEXT))


def downgrade() -> None:
    op.drop_column('groupware_notice', 'img_url') 
    op.drop_column('groupware_work_management', 'img_url') 
