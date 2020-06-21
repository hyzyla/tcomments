"""Add new columns for comments

Revision ID: eb392352ce75
Revises: cd638f8e1d5b
Create Date: 2020-06-21 16:45:51.033275

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'eb392352ce75'
down_revision = 'cd638f8e1d5b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('comments', sa.Column('author_id', postgresql.UUID(), nullable=False))
    op.add_column('comments', sa.Column('date_created', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    op.create_foreign_key(None, 'comments', 'users', ['author_id'], ['id'])


def downgrade():
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'date_created')
    op.drop_column('comments', 'author_id')
