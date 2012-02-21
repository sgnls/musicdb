from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from .decorators import login_not_required

@login_not_required
def login(request):
    if request.user.is_authenticated():
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)

            return redirect(request.path)
    else:
        form = AuthenticationForm()

    request.session.set_test_cookie()

    return render(request, 'auth/login.html', {
        'form': form,
    })

@login_not_required
def logout(request):
    auth.logout(request)

    messages.success(request, "You were succesfully logged out")

    return redirect('home')
