import json

from app import db
from config import FILENAME
from utils import get_codes


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(30))

    @staticmethod
    def encrypt_password(password):
        return hash(password)

    def check_password(self, password):
        return self.password == self.encrypt_password(password)

    def generate_key(self):
        new_code = {'code' + self.username: self.username}
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
        return user

    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, **kwargs):
        self.username = kwargs['username']
        if 'password' in kwargs:
            self.password = self.encrypt_password(kwargs['password'])


db.create_all()
