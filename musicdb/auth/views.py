from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

from .decorators import login_not_required

@login_not_required
def login(request):
    if request.user.is_authenticated():
        return redirect('static:home')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)

            return redirect(request.GET.get('next', request.path))

        messages.error(
            request,
            "There was an error logging you in, please check your details.",
        )

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

    return redirect('static:home')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your password was changed successfully")
        else:
            messages.error(request, "There was an error changing your password")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'auth/change_password.html', {
        'form': form,
    })

