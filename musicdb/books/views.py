from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.core.files.storage import default_storage

from .models import Author, Book

def index(request, letter=None):
    if letter is None:
        return redirect('books:index', 'a')

    authors = Author.objects.filter(last_name_first=letter)

    return render(request, 'books/index.html', {
        'letter': letter,
        'authors': authors,
        'letters': Author.objects.letters(),
    })

def author(request, slug):
    author = get_object_or_404(Author, slug=slug)

    return render(request, 'books/author.html', {
        'author': author,
    })

def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    address = request.user.profile.kindle_email_address

    if not address:
        return redirect(book.file.url())

    message = EmailMessage(to=(address,))
    message.attach(
        '%d.mobi' % book.pk,
        default_storage.open(book.file.location).read(),
    )
    message.send()

    messages.success(request, '"%s" sent to Kindle.' % book.title)

    return redirect(book.authors.all()[0].author)
