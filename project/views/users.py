from flask import render_template, redirect, flash, Blueprint
from flask import request
from flask.globals import current_app
from flask.helpers import url_for
from flask_login import login_user, login_required, logout_user

from project.forms import LoginUserForm, RegisterUserForm, ActivateUserForm
from project.models import Score
from project.models.users import User
from project.views.utils import logout_required

users = Blueprint('users', __name__)


@users.route('/', methods=['GET'])
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    paginated_scores = Score.query.order_by(Score.score.desc()).paginate(
        page, current_app.config.get('PAGE_SIZE', 5), False
    )
    next_url = url_for('users.home', page=paginated_scores.next_num) \
        if paginated_scores.has_next else None
    prev_url = url_for('users.home', page=paginated_scores.prev_num) \
        if paginated_scores.has_prev else None
    context = dict(
        scores=paginated_scores.items,
        prev_url=prev_url,
        next_url=next_url,
        page=page,
    )
    return render_template('pages/home.html', **context)


@users.route('/register', methods=['GET', 'POST'])
@logout_required
def register():
    form = RegisterUserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = form.save(form.data)
        flash(f'User {user.username} Registered successfully!')
        return redirect(url_for('users.home'))
    return render_template('forms/register.html', form=form)


@users.route('/activate', methods=['GET', 'POST'])
@logout_required
def activate():
    form = ActivateUserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = form.save(form.data)
        if not user:
            flash('Could not find the code.')
            return redirect('/activate')
        flash(f'User {user.username} created successfully! Please login!')
        return redirect(url_for('users.login'))
    return render_template('forms/activate.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
@logout_required
def login():
    form = LoginUserForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.data['username']
        login_user(User.get_by_username(username))
        flash(f'Welcome {username}!')
        return redirect('/')
    return render_template('forms/login.html', form=form)


@users.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))


@users.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@users.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404
