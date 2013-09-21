from django.shortcuts import render

from .models import Author

def index(request):
    authors = Author.objects.all()

    return render(request, 'books/index.html', {
        'authors': authors,
    })
