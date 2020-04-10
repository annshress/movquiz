from unittest import TestCase

from project.models import User
from project.tests import BaseTestMixin


class TestUserModel(BaseTestMixin, TestCase):
    def test_user_is_active(self):
        username = 'username'
        user = User(username=username)
        self.assertFalse(user.is_active)

    def test_user_password_is_hashed(self):
        username, password = 'username', 'password'
        user = self.add_user(username, password)
        self.assertNotEqual(password, user.password)
