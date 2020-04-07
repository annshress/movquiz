from wtforms import StringField, validators
from wtforms_alchemy import ModelForm, Form

from models import User


class RegisterUserForm(ModelForm):
    class Meta:
        model = User
        only = ['username']

    def save(self, cleaned_data):
        return User.create_user(**cleaned_data)


class ActivateUserForm(Form):
    code = StringField('Code', [validators.Length(min=1, max=80)])
    password = StringField(
        'Password',
        validators=[
            validators.DataRequired(),
            validators.Length(max=255),
        ]
    )
    re_password = StringField(
        'Password (Again)',
        validators=[
            validators.DataRequired(),
            validators.Length(max=255),
            validators.EqualTo('password', message='Passwords must match')
        ]
    )

    def save(self, cleaned_data):
        return User.activate(
            code=cleaned_data['code'],
            password=cleaned_data['password']
        )


class LoginUserForm(ModelForm):
    class Meta:
        model = User
        only = ['username', 'password']

# RegisterUserForm = model_form(User, only=['username'])
# LoginUserForm = model_form(User, only=['username', 'password'])
