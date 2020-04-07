import json

from flask_login import UserMixin

from project import db
from project.utils import get_codes, FILENAME


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(30))

    @staticmethod
    def encrypt_password(password):
        # dummy encryption
        return password+'encrypted'

    @classmethod
    def get_by_username(cls, username):
        return User.query.filter_by(username=username).first()

    def check_password(self, password):
        if self.password == self.encrypt_password(password):
            return True

    def generate_code(self):
        # dummy code generation
        return 'code' + self.username

    def generate_key(self):
        new_code = {self.generate_code(): self.username}
        data = get_codes()
        data.update(new_code)

        with open(FILENAME, 'w') as f:
            json.dump(data, f)

    @classmethod
    def create_user(cls, username):
        user = cls(username=username)
        user.generate_key()
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def activate(cls, code, password):
        data = get_codes()
        username = data.get(code, None)
        if not username:
            return

        user = User.query.filter_by(username=username).first()
        user.password = cls.encrypt_password(password)
        db.session.add(user)
        db.session.commit()

        # remove the activated code
        data.pop(code)
        with open(FILENAME, 'w') as f:
            json.dump(data, f)
        # end remove
        return user

    # -------------- FLASK-LOGIN --------------- #

    @property
    def is_active(self):
        return self.password is not None

    # -------------- END FLASK-LOGIN --------- #

    def __repr__(self):
        return '<User %r>' % self.username
