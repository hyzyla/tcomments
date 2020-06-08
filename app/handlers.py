from flask_login import login_user
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

from app.utils import (
    get_update_from_request, validate_telegram_auth, create_user,
    is_safe_url
)
from . import app, dispatcher


@app.route('/api/comments', methods=['GET'])
def get_comments():
    return 'HELL0'


@app.route('/api/comments/events', methods=['GET'])
def get_comments_events():
    return 'HELLO'


@app.route('/api/comments', methods=['POST'])
def add_comment():
    return 'HELLO'


@app.route('/api/bot', methods=['GET', 'POST'])
def bot_handler():
    update = get_update_from_request()
    dispatcher.process_update(update)
    return 'OK'


@app.route('/api/auth/telegram', methods=['GET'])
def auth_telegram():
    args, next_url = validate_telegram_auth()
    user = create_user(args)
    login_user(user)

    if not is_safe_url(next_url):
        return abort(400)

    return redirect(next_url)
