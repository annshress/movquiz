from flask import render_template, request, Blueprint, url_for
from flask_login.utils import login_required, current_user

from project.models.quiz import Question

quiz = Blueprint('quiz', __name__)


@quiz.route('/quiz', methods=['GET', 'POST'])
@login_required
def home():
    context = dict(
        key_name='answer',
        form={},
        questions=Question.fetch_quiz()
    )
    if request.method == 'POST':
        answered_questions, score = Question.check_answers(key_name=context['key_name'],
                                                           answers=request.form,
                                                           current_user=current_user)
        context.update(dict(
            form=request.form,
            questions=answered_questions,
            show_answer=True,
            score=score
        ))
    return render_template('pages/movies.html', **context)
