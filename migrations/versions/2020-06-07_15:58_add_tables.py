"""Add tables

Revision ID: 605a9a27c9c1
Revises: 
Create Date: 2020-06-07 15:58:29.109384

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '605a9a27c9c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', postgresql.UUID(), nullable=False),
        sa.Column('text', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'users',
        sa.Column('id', postgresql.UUID(), nullable=False),
        sa.Column('telegram_id', sa.Text(), nullable=False),
        sa.Column('first_name', sa.Text(), nullable=True),
        sa.Column('last_name', sa.Text(), nullable=True),
        sa.Column('username', sa.Text(), nullable=True),
        sa.Column('photo_url', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'comments',
        sa.Column('id', postgresql.UUID(), nullable=False),
        sa.Column('text', sa.Text(), nullable=False),
        sa.Column('parent_id', postgresql.UUID(), nullable=True),
        sa.Column('post_id', postgresql.UUID(), nullable=False),
        sa.ForeignKeyConstraint(('parent_id',), ['comments.id'], ),
        sa.ForeignKeyConstraint(('post_id',), ['posts.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('comments')
    op.drop_table('users')
    op.drop_table('posts')
