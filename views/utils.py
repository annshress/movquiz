from functools import wraps

from flask import redirect
from flask_login import current_user


def logout_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect('/')
        return func(*args, **kwargs)
    return decorated_view
