from django.conf import settings
from django.shortcuts import render, redirect

def landing(request):
    if request.user.is_authenticated():
        return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, 'static/landing.html', {
    })
