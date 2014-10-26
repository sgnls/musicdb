from django.shortcuts import render

from musicdb.utils.decorators import superuser_required

@superuser_required
def view(request):
    return render(request, 'superuser/view.html', {
    })
