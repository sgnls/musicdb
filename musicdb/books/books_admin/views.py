from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from musicdb.utils.decorators import superuser_required

from ..models import Author, Book

from .forms import AuthorForm, AuthorMergeForm, BookForm

@superuser_required
def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)

        if form.is_valid():
            form.save()

            messages.success(request, "Author saved.")

            return redirect('books:admin:author', author.pk)
    else:
        form = AuthorForm(instance=author)

    return render(request, 'books/admin/author.html', {
        'form': form,
        'author': author,
    })

@superuser_required
def author_merge(request, author_id):
    author = get_object_or_404(Author, pk=author_id)

    if request.method == 'POST':
        form = AuthorMergeForm(author, request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Author merged.")

            return redirect('books:admin:author', author.pk)
    else:
        form = AuthorMergeForm(author)

    return render(request, 'books/admin/author_merge.html', {
        'form': form,
        'author': author,
    })

@superuser_required
def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()

            messages.success(request, "Book saved.")

            return redirect('books:admin:book', book.pk)

    else:
        form = BookForm(instance=book)

    return render(request, 'books/admin/book.html', {
        'book': book,
        'form': form,
    })
