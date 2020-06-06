import os

import flask
from flask_migrate import Migrate
from flask_security import SQLAlchemyUserDatastore, Security
from flask_sqlalchemy import SQLAlchemy
from redis import Redis

app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_ADMIN_SWATCH'] = 'default'
app.config['REDIS_URL'] = os.environ['REDIS_URL']

db = SQLAlchemy(app)
migrate = Migrate(app, db)
redis = Redis.from_url(app.config['REDIS_URL'])

from . import models

user_store = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_store)
