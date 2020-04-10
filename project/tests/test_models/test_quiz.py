from unittest.case import TestCase

from project.models.quiz import Question, Score
from project.tests import BaseTestMixin


class TestQuestion(BaseTestMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.questions = super().populate_questions(10)
        self.username, self.password = 'user', 'password'
        self.user = self.add_user(self.username, self.password)

    def test_fetch_quiz_should_be_random(self):
        sample1 = Question.fetch_quiz(3)
        sample2 = Question.fetch_quiz(3)

        self.assertNotEqual(sample1, sample2)

    def test_check_answers(self):
        # user has no score yet
        self.assertIsNone(self.user.score)

        key = 'answer'
        answers = {
            key+str(question.id): question.answer
            for question in self.questions[:10]
        }
        questions, score = Question.check_answers(key, answers, self.user)
        self.assertEqual(score, 10)

        # check score table has been populated
        self.assertEqual(self.user.score.score, 10)

    def test_best_score_is_preserved(self):
        # this makes total score of 10
        self.test_check_answers()

        key = 'answer'
        answers = {
            key + str(question.id): 'wrong-answer'
            for question in self.questions[:10]
        }
        questions, score = Question.check_answers(key, answers, self.user)
        self.assertEqual(score, 0)

        # however the old score (higher) is preserved
        self.assertEqual(self.user.score.score, 10)
