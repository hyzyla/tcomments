from flask_security import RoleMixin, UserMixin

from . import db


class UserRoles(db.Model):
    __tablename__ = 'user_roles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Text, unique=True)
    description = db.Column(db.Text)

    def __repr__(self):
        return self.name


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary='user_roles')
