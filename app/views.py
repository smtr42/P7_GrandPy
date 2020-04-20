"""Main views for the flask app."""
from app import flask_app, render_template, jsonify, request
from app.models.parser import Parser

parser = Parser()


@flask_app.route('/')
@flask_app.route('/index')
def index():
    return render_template("index.html")


@flask_app.route('/ajax', methods=["POST"])
def get_content():
    user_text = request.form["message-content"]
    clean_text = parser.process(user_text)
    clean_text = {"response": clean_text}
    print(jsonify(clean_text))
    return jsonify(clean_text)

# Bonjour GrandPy, où se strouve la tour Eiffel, s'il te plaît ?