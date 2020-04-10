import random

from project import create_app, db
from project.models import User, Score
from project.tests.factory import QuestionFactory
from project.utils import delete_code_file


class BaseTestMixin:
    def setUp(self):
        app = create_app('flask_test.cfg')
        self.app = app
        # testing client
        self.client = app.test_client()

        context = app.app_context()
        context.push()
        print('dropping')
        db.drop_all()
        print('creating')
        db.create_all()
        self.assertEqual(app.debug, False)

    def tearDown(self):
        # remove the codes file created during tests
        delete_code_file()

    ########################
    #    helper methods    #
    ########################

    @staticmethod
    def add_user(username, password):
        user = User(username=username)
        user.password=User._hash_password(password)
        db.session.add(user)
        db.session.commit()
        return user

    def populate_questions(self, size=3):
        questions = QuestionFactory.create_batch(size)
        for question in questions:
            db.session.add(question)
        db.session.commit()

    @staticmethod
    def add_score(user):
        Score.save_record(user.id, random.randint(1, 10))
