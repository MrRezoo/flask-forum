from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import app.exceptions as app_exception
from app.posts.routes import blueprint as posts_blueprint
from app.users.routes import blueprint as users_blueprint


def register_blueprint(flask_app):
    app.register_blueprint(flask_app)
    app.register_blueprint(flask_app)


def register_error_handlers(flask_app):
    app.register_error_handler(404, app_exception.page_not_found)
    app.register_error_handler(500, app_exception.server_error)


app = Flask(__name__)
register_blueprint(app)
register_error_handlers(app)
app.config.from_object('config.DevConfig')

db = SQLAlchemy(app)
db.create_all()
