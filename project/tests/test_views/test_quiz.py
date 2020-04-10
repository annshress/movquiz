from unittest import TestCase

from project.tests.test_views import TestViewsMixin


class TestQuizViews(TestViewsMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.username, self.password = 'admin', 'admin'
        self.user = self.add_user(self.username, self.password)

    def test_random_questions_appear(self):
        # populate questions to table first
        self.populate_questions(10)

        with self.client:
            self.login(self.username, self.password)

            response = self.get_quiz()
            self.assertEqual(response.status_code, 200)

            # render the page again
            response2 = self.get_quiz()
            self.assertEqual(response.status_code, 200)
            self.assertNotEqual(response.data, response2.data)
            # render the page again
            response3 = self.get_quiz()
            self.assertEqual(response.status_code, 200)
            self.assertNotEqual(response2.data, response3.data)

    def test_quiz_home(self):
        # setup some users and scores
        with self.client:
            self.login(self.username, self.password)

            self.add_score(self.user)

            response = self.get_quiz_home()
            # user score should be available in the home page
            self.assertIn(self.user.username.encode(), response.data)
