from . import app


@app.route('/index', methods=['GET'])
def index():
    return 'HELLo'
