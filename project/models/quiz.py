from sqlalchemy.sql.expression import func

from project import db
# from project.models.users import User
from project.models.utils import get_or_create


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(256), nullable=False)
    answer = db.Column(db.String(256), nullable=False)

    def check_answer(self, answer):
        return answer.lower() == self.answer.lower()

    @classmethod
    def fetch_quiz(cls, limit=10):
        return cls.query.order_by(func.random()).limit(limit).all()

    @classmethod
    def check_answers(cls, key_name, answers, current_user):
        score = 0
        # answered questions
        questions = []
        for key, value in answers.items():
            q_id = key.strip(key_name)
            question = cls.query.get(int(q_id))
            if question.check_answer(value):
                score += 1
            questions.append(question)

        Score.save_record(current_user.id, score)

        return questions, score

    def __repr__(self):
        return f'<Question: {self.question}'

    def __init__(self, **kwargs):
        self.question = kwargs['question']
        self.answer = kwargs['answer']


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('score', uselist=False),
                           lazy='joined')
    score = db.Column(db.Integer, default=0)

    @classmethod
    def save_record(cls, user_id, scored):
        score, created = get_or_create(db.session, cls, user_id=user_id)
        # update score if person has scored higher than before.
        if created:
            score.score = scored
        elif score.score < scored:
            score.score = scored
        db.session.commit()

    def __repr__(self):
        return f'{self.user} {self.score}'

    def __init__(self, **kwargs):
        self.user_id = kwargs['user_id']
        self.score = kwargs.get('score', 0)
