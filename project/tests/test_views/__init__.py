from flask import url_for

from project.tests import BaseTestMixin


class TestViewsMixin(BaseTestMixin):

    ########################
    #    helper methods    #
    ########################

    def register(self, username):
        return self.client.post(
            url_for('users.register'),
            data=dict(username=username),
            follow_redirects=True
        )

    def activate(self, code, password, re_password):
        return self.client.post(
            url_for('users.activate'),
            data=dict(code=code,
                      password=password,
                      re_password=re_password),
            follow_redirects=True
        )

    def login(self, username, password):
        return self.client.post(
            url_for('users.login'),
            data=dict(username=username, password=password),
            follow_redirects=True
        )

    def logout_user(self):
        return self.client.get(
            url_for('users.logout'),
            follow_redirects=True
        )

    def get_quiz_home(self):
        return self.client.get(
            url_for('users.home'),
            follow_redirects=True
        )

    def get_quiz(self):
        return self.client.get(
            url_for('quiz.home'),
            follow_redirects=True
        )
