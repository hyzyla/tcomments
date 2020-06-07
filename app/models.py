import columns
from . import db


class User(db.Model):
    __tablename__ = 'users'

    id = columns.ID()


class Post(db.Model):
    __tablename__ = 'posts'

    id = columns.ID()
    text = db.Column(db.Text)


class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = columns.ID()
    text = columns.Text()
    parent_id = columns.ForeignID('comments.id', nullable=True)
    post_id = columns.ForeignID('posts.id')
