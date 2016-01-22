from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

from musicdb.utils.paginator import AutoPaginator
from musicdb.utils.decorators import superuser_required

from .forms import NewUserForm, EditUserForm, ResetPasswordForm

@superuser_required
def view(request):
    page = AutoPaginator(request, User.objects.all(), 10).current_page()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, "User invited.")

            return redirect('account:admin:user', user.pk)

        messages.error(request, "There was an error creating this user.")
    else:
        form = NewUserForm()

    return render(request, 'auth/admin/view.html', {
        'form': form,
        'page': page,
    })

@superuser_required
def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, "User saved.")

            return redirect('account:admin:user', user.pk)
    else:
        form = EditUserForm(instance=user)

    return render(request, 'auth/admin/user.html', {
        'user': user,
        'form': form,
    })

@superuser_required
@require_POST
def reset_password(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    new_password = ResetPasswordForm(instance=user).save()

    messages.success(request, "Password reset to '%s'." % new_password)

    return redirect('account:admin:user', user.pk)
