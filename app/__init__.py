""" Initialization of Flask"""

from flask import Flask

flask_app = Flask(__name__)

# After flask instantiation we import routes
from app import views
