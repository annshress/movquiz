from project import create_app, db
from project.models import User
from project.utils import delete_code_file


class BaseTestMixin:
    def setUp(self):
        app = create_app('flask_test.cfg')
        # testing client
        self.client = app.test_client()

        context = app.app_context()
        context.push()
        db.create_all()
        self.assertEqual(app.debug, False)

    def tearDown(self):
        db.drop_all()
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
