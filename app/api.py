from . import flask_app

@flask_app.route('/', methods=["GET", "POST"])
def index():
    return "Hello world", 200


