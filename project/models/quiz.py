from project import db
# from project.models.users import User


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(256), nullable=False)
    answer = db.Column(db.String(256), nullable=False)

    def check_answer(self, answer):
        return answer.lower() == self.answer.lower()

    def __init__(self, **kwargs):
        self.question = kwargs['question']
        self.answer = kwargs['answer']


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('score', uselist=False),
                           lazy='joined')
    score = db.Column(db.Integer, default=0)
