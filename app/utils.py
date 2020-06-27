import hashlib
import hmac
from http import HTTPStatus
from typing import Dict, Optional, List, Any
from urllib.parse import urlparse, urljoin

import flask
import telegram
from flask import request, abort, Response
from telegram import LoginUrl, InlineKeyboardButton

from app import dispatcher, app, db
from app.models import User, Post, Comment
from app.types import GroupedComment


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


def get_post(post_id: str) -> Optional[Post]:
    return Post.query.get(post_id)


def user_to_json(user: User) -> Dict[str, str]:
    return {
        'id': user.id,
        'name': user.first_name,
        'photoURL': user.photo_url,
    }


def comment_to_json(comment: Comment) -> Dict[str, Any]:
    return {
        'id': comment.id,
        'text': comment.text,
        'date': comment.date_created,
        'author': user_to_json(comment.author)
    }


def comments_to_json(comments: List[GroupedComment]) -> List[Dict[str, Any]]:
    return [
        {
            **comment_to_json(comment.parent),
            'children': comments_to_json(comment.children),
        }
        for comment in comments
    ]


def create_comment(data: Dict[str, str], user: User) -> Comment:
    comment = Comment(
        text=data['text'],
        post_id=data['post_id'],
        parent_id=data.get('parent_id'),
        author=user,
    )
    db.session.add(comment)
    db.session.commit()
    return comment


def get_post_comments(post_id: str) -> List[Comment]:
    return Comment.query.filter_by(post_id=post_id).all()


def group_comments(comments: List[Comment], parent_id: Optional[str] = None) -> List[GroupedComment]:
    children = (c for c in comments if c.parent_id == parent_id)
    return [
        GroupedComment(
            parent=child,
            children=group_comments(comments, child.id),
        )
        for child in children
    ]


def reverse_parent(comments: List[GroupedComment]) -> List[GroupedComment]:
    return list(reversed(comments))


def build_open_comments_button(post: Post):
    bot_username = app.config['TELEGRAM_BOT_USERNAME']
    domain = app.config['TELEGRAM_WEBHOOK_DOMAIN']
    login_url = LoginUrl(
        url=f'{domain}/api/auth/telegram?next_url=/posts/{post.id}',
        bot_username=bot_username,
    )
    return InlineKeyboardButton("Open comments", login_url=login_url)


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


def redirect(target: str):
    return flask.redirect(target)

