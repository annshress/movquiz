from functools import wraps

from flask import redirect
from flask.helpers import url_for
from flask_login import current_user


def logout_required(func):
    """decorator: redirects to users.home for views requiring anonymous user"""
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.is_authenticated and current_user.is_active:
            return redirect(url_for('users.home'))
        return func(*args, **kwargs)
    return decorated_view
