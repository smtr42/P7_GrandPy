#!/usr/bin/python3
""" Main module to run the the app."""

from app import flask_app


def run():
    """ Run the flask app."""

    flask_app.run(debug=True)


if __name__ == "__main__":
    run()
