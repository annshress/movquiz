from project import create_app, db
from project.models import User
from project.tests import BaseTestMixin


class TestViewsMixin(BaseTestMixin):
    def setUp(self):
        app = create_app('flask_test.cfg')
        # testing client
        self.client = app.test_client()

        context = app.app_context()
        context.push()
        db.create_all()
        self.assertEqual(app.debug, False)

    def tearDown(self):
        super().tearDown()
        db.drop_all()

    ########################
    #    helper methods    #
    ########################

    @staticmethod
    def add_user(username, password):
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    def register(self, username):
        return self.client.post(
            '/register',
            data=dict(username=username),
            follow_redirects=True
        )

    def activate(self, code, password, re_password):
        return self.client.post(
            '/activate',
            data=dict(code=code,
                      password=password,
                      re_password=re_password),
            follow_redirects=True
        )

    def login(self, username, password):
        return self.client.post(
            '/login',
            data=dict(username=username, password=password),
            follow_redirects=True
        )

    def logout_user(self):
        return self.client.get(
            '/logout',
            follow_redirects=True
        )

    def force_login(self, user):
        """sets the flask.current_user to provided user"""
