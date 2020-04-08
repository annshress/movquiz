import os
import unittest

from project.tests.test_views import TestViewsMixin


class TestUserViews(TestViewsMixin, unittest.TestCase):

    def test_main_page(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please log in to access this page', response.data)

    def test_valid_login(self):
        # user does not exist yet
        username, password = 'admin', 'admin'
        response = self.login(username, password)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username or Password does not match', response.data)

        # create user and login again
        self.add_user(username, password)
        response = self.login(username, password)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

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
