import flask
from flask import jsonify, request
from flask_login import login_user, current_user, login_required
from werkzeug.exceptions import abort

from app import utils
from app.utils import (
    get_update_from_request, validate_telegram_auth, create_user,
    is_safe_url, get_post_comments, group_comments, comments_to_json
)
from . import app, dispatcher


@app.route('/api/posts/<post_id>', methods=['GET'])
def get_post(post_id):
    post = utils.get_post(post_id)
    return jsonify({
        'id': post.id,
        'text': post.text,
        'date': post.date,
    })


@app.route('/api/posts/<post_id>/comments', methods=['GET'])
def get_comments(post_id):
    comments = get_post_comments(post_id)
    grouped = group_comments(comments)
    data = comments_to_json(grouped)
    return jsonify(data)


@app.route('/api/posts/<post_id>/comments', methods=['POST'])
@login_required
def add_comment(post_id):
    data = request.json
    comment = utils.create_comment({**data, 'post_id': post_id})
    return utils.comment_to_json(comment)


@app.route('/api/bot', methods=['GET', 'POST'])
def bot_handler():
    update = get_update_from_request()
    dispatcher.process_update(update)
    return 'OK'


@app.route('/api/index')
def index():
    return f'HELLO {current_user}'


@app.route('/api/auth/telegram', methods=['GET'])
def auth_telegram():
    args, next_url = validate_telegram_auth()
    user = create_user(args)
    login_user(user, remember=True)

    if not is_safe_url(next_url):
        return abort(400)
    return flask.redirect(next_url)
