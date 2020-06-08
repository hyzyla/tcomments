import hashlib
import hmac
from http import HTTPStatus
from typing import Dict, Optional
from urllib.parse import urlparse, urljoin

import telegram
from flask import request, abort, Response
from telegram import LoginUrl, InlineKeyboardButton

from app import dispatcher, app, db
from app.models import User, Post


def get_update_from_request():
    bot = dispatcher.bot
    return telegram.Update.de_json(request.get_json(force=True), bot)


def validate_telegram_auth():
    bot_token = app.config['TELEGRAM_TOKEN']
    m = hashlib.sha256()
    m.update(bot_token.encode())
    secret_key = m.digest()

    args = request.args.copy()
    next_url = args.pop('next_url', None)
    expected_hash = args.pop('hash')
    data = '\n'.join(sorted(map(lambda x: f'{x[0]}={x[1]}', args.items())))
    hash_ = hmac.new(
        secret_key,
        data.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()
    if expected_hash != hash_:
        abort(HTTPStatus.FORBIDDEN)
    return dict(args), next_url


def create_user(args: Dict[str, str]) -> User:
    telegram_id: str = args['id']
    first_name = args.get('first_name')
    last_name = args.get('last_name')
    username = args.get('username')
    photo_url = args.get('photo_url')
    user = User.query.filter_by(telegram_id=telegram_id).first()
    if not user:
        user = User(
            telegram_id=telegram_id,
            first_name=first_name,
            last_name=last_name,
            username=username,
            photo_url=photo_url,
        )
        db.session.add(user)
    else:
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.photo_url = photo_url

    db.session.commit()
    return user


def create_post(message: telegram.Message) -> Post:
    message_id = str(message.forward_from_message_id)
    post = Post.query.filter_by(message_id=message_id).first()
    if not post:
        post = Post(
            message_id=message_id,
            text=message.text,
            date=message.date,
            telegram_data=message.to_dict(),
        )
        db.session.add(post)
        db.session.commit()
    return post


def get_user(user_id: str) -> Optional[User]:
    return User.query.get(user_id)


def build_open_comments_button(post: Post):
    bot_username = app.config['TELEGRAM_BOT_USERNAME']
    domain = app.config['DOMAIN']
    login_url = LoginUrl(
        url=f'{domain}/api/auth/telegram?next_url=/posts/{post.id}',
        bot_username=bot_username,
    )
    return InlineKeyboardButton("Open comments", login_url=login_url)


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


def redirect():
    pass
