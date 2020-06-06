from flask_security import RoleMixin, UserMixin

from . import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary='user_roles')


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.UUID(), primary_key=True)
    text = db.Column(db.Text)


class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.UUID(), primary_key=True)
    parent_id = db.Column(db.UUID(), db.ForeignKey(''))
    post_id = db.Column(db.UUID(), db.ForeignKey('comments.id'), nullable=True)
    


class Comments