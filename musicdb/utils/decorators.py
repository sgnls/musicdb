import functools

from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

superuser_required = user_passes_test(lambda u: (u.is_authenticated() and u.is_superuser))

def logout_required(fn):
    @functools.wraps(fn)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(settings.LOGIN_REDIRECT_URL)
        return fn(request, *args, **kwargs)
    return wrapper
