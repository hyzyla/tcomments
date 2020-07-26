"""Add post author

Revision ID: 846bfef273d7
Revises: eb392352ce75
Create Date: 2020-07-26 08:39:25.281921

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '846bfef273d7'
down_revision = 'eb392352ce75'
branch_labels = None
depends_on = None


def upgrade():
    # op.execute()
    op.add_column('posts', sa.Column('author_id', postgresql.UUID(), nullable=True))
    op.execute(
        '''
        -- insert authors to database
        WITH post_autors AS (
            SELECT telegram_data -> 'chat' ->> 'id'         as telegram_id,
                   telegram_data -> 'chat' ->> 'username'   as username,
                   telegram_data -> 'chat' ->> 'first_name' as first_name,
                   telegram_data -> 'chat' ->> 'last_name'  as last_name,
                   id                                       as post_id
            FROM posts
        )
        INSERT INTO users (id, telegram_id, first_name, last_name, username)
        SELECT
               uuid_generate_v4(),
               telegram_id,
               first_name,
               last_name,
               username
        FROM post_autors WHERE username not IN (SELECT username FROM users);
        
        -- connect posts and authors
        WITH post_autors AS (
            SELECT telegram_data -> 'chat' ->> 'id'         as telegram_id,
                   telegram_data -> 'chat' ->> 'username'   as username,
                   telegram_data -> 'chat' ->> 'first_name' as first_name,
                   telegram_data -> 'chat' ->> 'last_name'  as last_name,
                   id                                       as post_id
            FROM posts
        ), authrors AS (
            SELECT post_autors.post_id, users.id
            FROM post_autors
                     JOIN users ON post_autors.telegram_id = users.telegram_id
        )
        UPDATE posts 
        SET author_id = authrors.id 
        FROM authrors 
        WHERE posts.id = authrors.post_id;
        
        -- make author as required column
        ALTER TABLE posts ALTER COLUMN author_id SET NOT NULL;
        '''
    )
    op.create_foreign_key(None, 'posts', 'users', ['author_id'], ['id'])


def downgrade():
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'author_id')
