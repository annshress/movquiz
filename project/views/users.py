from flask import render_template, redirect, flash, Blueprint
from flask import request
from flask.helpers import url_for
from flask_login import login_user, login_required, logout_user

from project.forms import LoginUserForm, RegisterUserForm, ActivateUserForm
from project.models.users import User
from project.views.utils import logout_required

users = Blueprint('users', __name__)


@users.route('/', methods=['GET'])
@login_required
def home():
    return render_template('pages/home.html')


@users.route('/register', methods=['GET', 'POST'])
@logout_required
def register():
    form = RegisterUserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = form.save(form.data)
        flash(f'User {user.username} Registered successfully!')
        return redirect('/')
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
        else:
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
    return redirect('/')
