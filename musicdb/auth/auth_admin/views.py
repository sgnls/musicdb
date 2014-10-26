from django.shortcuts import render
from django.contrib.auth.models import User

from musicdb.utils.paginator import AutoPaginator
from musicdb.utils.decorators import superuser_required

@superuser_required
def view(request):
    page = AutoPaginator(request, User.objects.all(), 10).current_page()

    return render(request, 'auth/admin/view.html', {
        'page': page,
    })
