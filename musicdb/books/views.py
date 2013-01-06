from django.shortcuts import render

from .models import Book

def index(request):
    books = Book.objects.select_related('author')

    return render(request, 'books/index.html', {
        'books': books,
    })
