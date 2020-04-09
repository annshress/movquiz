from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login.login_manager import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# DETACHED EXTENSIONS
db = SQLAlchemy()
# Authentication manager and System setup
login_manager = LoginManager()
login_manager.login_view = 'users.login'
# password encryption
bcrypt = Bcrypt()


def create_app(config_file=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_file)
    initialize_extensions(app)
    register_blueprints(app)

    return app


def initialize_extensions(app):
    # bind extensions to the flask app
    db.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # to fetch logged in user based on session user id
    from project.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app):
    # register flask blueprints
    from project.views.users import users
    from project.views.quiz import quiz

    app.register_blueprint(users)
    app.register_blueprint(quiz)
