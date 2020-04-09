from project.tests import BaseTestMixin


class TestViewsMixin(BaseTestMixin):

    ########################
    #    helper methods    #
    ########################

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
