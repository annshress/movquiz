import pytest

from project import create_app, db
from project.models.users import User


@pytest.fixture(scope='module')
def test_client():
    app = create_app('flask_test.cfg')

    testing_client = app.test_client()
    context = app.app_context()
    context.push()

    yield testing_client

    context.pop()


@pytest.fixture(scope='module')
def init_database():
    # create database
    db.create_all()

    # initialize db
    user = User(username='foo')
    user.password = user.encrypt_password('admin')
    db.session.add(user)
    db.session.commit()

    yield db

    db.drop_all()


@pytest.fixture(scope='module')
def new_user():
    user = User(username='foo')
    return user
