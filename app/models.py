from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property

from app import columns
from . import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = columns.ID()
    telegram_id = columns.Text(unique=True)
    first_name = columns.Text(nullable=True)
    last_name = columns.Text(nullable=True)
    username = columns.Text(nullable=True)
    photo_url = columns.Text(nullable=True)

    @hybrid_property
    def name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        if self.first_name:
            return self.first_name
        if self.last_name:
            return self.last_name
        return self.username


class Post(db.Model):
    __tablename__ = 'posts'

    id = columns.ID()
    message_id = columns.Text()
    text = columns.Text()
    date = columns.DateTime()
    author_id = columns.ForeignID('users.id', nullable=False)

    telegram_data = columns.JSONB()

    author = db.relationship('User')


class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = columns.ID()
    text = columns.Text()
    date_created = columns.DateCreated()
    author_id = columns.ForeignID('users.id', nullable=False)
    parent_id = columns.ForeignID('comments.id', nullable=True)
    post_id = columns.ForeignID('posts.id')

    author = db.relationship('User')
    post = db.relationship('Post')
    parent = db.relationship('Comment', remote_side=[id])
