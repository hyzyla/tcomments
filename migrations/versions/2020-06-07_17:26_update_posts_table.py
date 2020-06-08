"""Update posts table

Revision ID: cd638f8e1d5b
Revises: 605a9a27c9c1
Create Date: 2020-06-07 17:26:55.413965

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'cd638f8e1d5b'
down_revision = '605a9a27c9c1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('date', sa.DateTime(), nullable=False))
    op.add_column('posts', sa.Column('message_id', sa.Text(), nullable=False))
    op.add_column('posts', sa.Column('telegram_data', sa.JSON(), nullable=False))
    op.alter_column(
        'posts',
        'text',
        existing_type=sa.TEXT(),
        nullable=False
    )


def downgrade():
    op.alter_column(
        'posts',
        'text',
        existing_type=sa.TEXT(),
        nullable=True
    )
    op.drop_column('posts', 'telegram_data')
    op.drop_column('posts', 'message_id')
    op.drop_column('posts', 'date')
