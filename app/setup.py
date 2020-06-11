import os
from queue import Queue

import telegram
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters


def prepare_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.config['TELEGRAM_TOKEN'] = os.environ['TELEGRAM_TOKEN']
    app.config['TELEGRAM_BOT_USERNAME'] = os.environ['TELEGRAM_BOT_USERNAME']
    app.config['DOMAIN'] = os.environ['DOMAIN']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    app.secret_key = app.config['SECRET_KEY']
    app.config['FLASK_ENV'] = os.environ['FLASK_ENV']
    app.config['SESSION_COOKIE_DOMAIN'] = os.environ['SESSION_COOKIE_DOMAIN']
    # app.config['SERVER_NAME'] = os.environ['SERVER_NAME']
    return app


def prepare_db(app: Flask) -> SQLAlchemy:
    return SQLAlchemy(app)


def prepare_migration(app: Flask, db: SQLAlchemy) -> Migrate:
    return Migrate(app, db)


def prepare_cors(app: Flask) -> CORS:
    return CORS(app, supports_credentials=True)


def prepare_login(app: Flask) -> LoginManager:
    from app import utils

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return utils.get_user(user_id)

    return login_manager


def prepare_dispatcher(app: Flask) -> Dispatcher:
    bot = telegram.Bot(app.config['TELEGRAM_TOKEN'])
    update_queue = Queue()
    dispatcher = Dispatcher(bot, update_queue, use_context=True)

    return dispatcher


def prepare_handlers(dp: Dispatcher) -> None:
    from app import callbacks

    dp.add_handler(CommandHandler('start', callbacks.start))
    dp.add_handler(
        MessageHandler(
            filters=Filters.text('I did that'),
            callback=callbacks.after_promotion,
        ),
    )
    dp.add_handler(
        MessageHandler(
            filters=Filters.forwarded,
            callback=callbacks.forwarded_post,
        ),
    )
    dp.add_error_handler(callbacks.on_error)
