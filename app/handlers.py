import flask
from flask_login import login_user, login_required, current_user
from flask import jsonify, request, session
from werkzeug.exceptions import abort

from app.utils import (
    get_update_from_request, validate_telegram_auth, create_user,
    is_safe_url, redirect, get_post_comments, group_comments, comments_to_json
)
from app import utils
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
# @login_required
def add_comment(post_id):
    print(dict(session))
    raise
    data = request.json
    comment = utils.create_comment({**data, 'post_id': post_id})
    return utils.comment_to_json(comment)


@app.route('/api/bot', methods=['GET', 'POST'])
def bot_handler():
    update = get_update_from_request()
    dispatcher.process_update(update)
    return 'OK'


@app.route('/index')
def index():
    return f'HELLO {current_user}'


@app.route('/api/auth/telegram', methods=['GET'])
def auth_telegram2():
    args, next_url = validate_telegram_auth()
    user = create_user(args)
    print('Logged', login_user(user, remember=True))
    print(dict(session))
    if not is_safe_url(next_url):
        return abort(400)
    session['hello'] = 'world!'
    print(next_url)
    # return 'ok'
    return flask.redirect(next_url)
    # return redirect(next_url)