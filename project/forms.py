from wtforms import StringField, validators, PasswordField
from wtforms_alchemy import ModelForm, Form

from project.models.users import User


class RegisterUserForm(ModelForm):
    class Meta:
        model = User
        only = ['username']

    def save(self, cleaned_data):
        return User.create_user(**cleaned_data)


class ActivateUserForm(Form):
    code = StringField('Code', [validators.Length(min=1, max=80)])
    password = PasswordField(
        'Password',
        validators=[
            validators.DataRequired(),
            validators.Length(min=7, max=30),
        ]
    )
    re_password = PasswordField(
        'Password (Again)',
        validators=[
            validators.DataRequired(),
            validators.EqualTo('password', message='Passwords must match')
        ]
    )

    def save(self, cleaned_data):
        return User.activate(
            code=cleaned_data['code'],
            password=cleaned_data['password']
        )


class LoginUserForm(ModelForm):
    password = PasswordField(
        'Password',
        validators=[
            validators.DataRequired(),
            validators.Length(max=255),
        ]
    )

    class Meta:
        model = User
        only = ['username', 'password']
        unique_validator = None

    def validate(self):
        success = super().validate()
        if not success:
            return False
        user = User.get_by_username(self.data['username'])
        if not user:
            self.errors['errors'] = ['User not found.']
            return False
        elif not user.check_password(password=self.data['password']):
            self.password.errors.append('Password does not match')
            return False
        return True
