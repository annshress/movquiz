import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SECRET_KEY = 'some-random-key'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')

FILENAME = 'codes.json'
