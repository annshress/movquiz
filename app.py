from flask import Flask
from flask_login.login_manager import LoginManager
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
# Authentication manager and System setup
login_manager = LoginManager()
login_manager.login_view = 'users.login'

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))


if __name__ == '__main__':
    from views.users import users

    app.register_blueprint(users)
    app.run(debug=True)
