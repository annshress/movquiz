import unittest

from project.models import User
from project.tests.test_views import TestViewsMixin


class TestUserViews(TestViewsMixin, unittest.TestCase):

    def test_main_page(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please log in to access this page', response.data)

    def test_valid_login(self):
        username, password = 'user', 'password'
        # create user and login again
        self.add_user(username, password)
        response = self.login(username, password)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

    def test_invalid_login(self):
        # user does not exist yet
        username, password = 'admin', 'admin'
        response = self.login(username, password)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username or Password does not match', response.data)

    def test_valid_user_registration(self):
        username = 'user'
        response = self.register(username)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registered successfully', response.data)

        # try logging in, it should fail
        response = self.login(username, 'random pass')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username or Password does not match', response.data)

        return username

    def test_invalid_user_registration_duplicate_username(self):
        # register user
        username = 'user'
        response = self.register(username)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registered successfully', response.data)

        # RE-register user
        response = self.register(username)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Already exists', response.data)

    def test_valid_activation(self):
        username = 'user'
        response = self.register(username)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registered successfully', response.data)

        # use the saved code to activate
        password = 'pass'
        response = self.activate(code=User.generate_code(username), password=password, re_password=password)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'created successfully', response.data)

    def test_invalid_re_activation(self):
        username = 'user'
        response = self.register(username)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registered successfully', response.data)

        # use the saved code to activate
        password = 'pass'
        response = self.activate(code=User.generate_code(username), password=password, re_password=password)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'created successfully', response.data)

        # resubmit
        response = self.activate(code=User.generate_code(username), password=password, re_password=password)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Could not find the code', response.data)

    def test_invalid_code_activation(self):
        # resubmit
        response = self.activate(code=User.generate_code('random'), password='random', re_password='random')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Could not find the code', response.data)
