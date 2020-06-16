"""
Здесь собираеться приложение которое импортируеться в run.py для запуска.
"""

from flask import Flask
from models import create_tables
from config import config
from flask_cors import CORS

def create_app(env):
    app = Flask(__name__)
    create_tables()
    app.config.from_object(config[env])
    CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
    CORS(app, resources={r"/parser/*": {"origins": "*"}})

    from freelance_api.api import api
    app.register_blueprint(api, url_prefix="/api/v1")

    from site_parser.main import parser
    app.register_blueprint(parser, url_prefix="/parser")

    return app