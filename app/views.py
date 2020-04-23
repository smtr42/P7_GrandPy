"""Main views for the flask app."""
from app import flask_app, render_template, jsonify, request
from app.models.core import Core


@flask_app.route('/')
@flask_app.route('/index')
def index():
    return render_template("index.html")


@flask_app.route('/ajax', methods=["POST"])
def get_content():
    text_input = request.form["message-content"]
    core = Core()
    payload = core.process(text_input)
    return jsonify(payload)

# Bonjour GrandPy, où se trouve la tour Eiffel, s'il te plaît ?