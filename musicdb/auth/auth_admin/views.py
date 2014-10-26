from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from musicdb.utils.paginator import AutoPaginator
from musicdb.utils.decorators import superuser_required

from .forms import UserForm

@superuser_required
def view(request):
    page = AutoPaginator(request, User.objects.all(), 10).current_page()

    return render(request, 'auth/admin/view.html', {
        'page': page,
    })

@superuser_required
def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, "User saved.")

            return redirect('auth:admin:user', user.pk)
    else:
        form = UserForm(instance=user)

    return render(request, 'auth/admin/user.html', {
        'user': user,
        'form': form,
    })
