from flask_login import UserMixin

from app import columns
from . import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = columns.ID()
    telegram_id = columns.Text()
    first_name = columns.Text(nullable=True)
    last_name = columns.Text(nullable=True)
    username = columns.Text(nullable=True)
    photo_url = columns.Text(nullable=True)


class Post(db.Model):
    __tablename__ = 'posts'

    id = columns.ID()
    message_id = columns.Text()
    text = columns.Text()
    date = columns.DateTime()

    telegram_data = columns.JSON()


class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = columns.ID()
    text = columns.Text()
    parent_id = columns.ForeignID('comments.id', nullable=True)
    post_id = columns.ForeignID('posts.id')
