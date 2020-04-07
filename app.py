from flask import Flask, render_template, redirect, flash
from flask import request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def home():
    return render_template('pages/home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    from forms import RegisterUserForm

    form = RegisterUserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = form.save(form.data)
        flash(f'User {user.username} Registered successfully!')
        return redirect('/')
    return render_template('forms/register.html', form=form)


@app.route('/activate', methods=['GET', 'POST'])
def activate():
    from forms import ActivateUserForm

    form = ActivateUserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = form.save(form.data)
        flash(f'User {user.username} created successfully! Please login!')
        return redirect('/')
    return render_template('forms/activate.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # todo if request.user, return HOME
    if request.method == 'GET':
        return 'Login Form'
    # todo handle login
    return 'Login'


if __name__ == "__main__":
    app.run(debug=True)
