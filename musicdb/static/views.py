from django.shortcuts import render

from musicdb.auth.decorators import login_not_required

def index(request):
    return render(request, 'static/index.html')
