from flask import Flask

import app.exceptions as app_exception
from app.extentions import db, migrate, login_manager
from app.posts.routes import blueprint as posts_blueprint
from app.users.routes import blueprint as users_blueprint


def register_blueprint(flask_app):
    flask_app.register_blueprint(users_blueprint)
    flask_app.register_blueprint(posts_blueprint)


def register_error_handlers(flask_app):
    flask_app.register_error_handler(404, app_exception.page_not_found)
    flask_app.register_error_handler(500, app_exception.server_error)


def register_shell_context(flask_app):
    def shell_context():
        return {
            'db': db,
            'User': User,
            'Code': Code,
            'Follow': Follow,
        }

    flask_app.shell_context_processor(shell_context)


app = Flask(__name__)
register_blueprint(app)
register_error_handlers(app)
register_shell_context(app)
app.config.from_object('config.DevConfig')
db.init_app(app)

from app.users.models import User, Code, Follow  # is here due to circular_imports for db.create_all() use

migrate.init_app(app, db)
login_manager.init_app(app)
