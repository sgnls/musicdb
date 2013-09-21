from django.shortcuts import render, redirect, get_object_or_404

from .models import Author

def index(request, letter=None):
    if letter is None:
        return redirect('books:index', 'a')

    authors = Author.objects.filter(last_name_first=letter)

    return render(request, 'books/index.html', {
        'authors': authors,
        'letters': Author.objects.letters(),
    })

def author(request, slug):
    author = get_object_or_404(Author, slug=slug)

    return render(request, 'books/author.html', {
        'author': author,
    })
