import factory

from project.models import Question
from project import db


class QuestionFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Question
        sqlalchemy_session = db.session   # the SQLAlchemy session object

    id = factory.Sequence(lambda n: n)
    question = factory.Sequence(lambda n: u'Question %d' % n)
    answer = factory.Sequence(lambda n: u'Answer %d' % n)
