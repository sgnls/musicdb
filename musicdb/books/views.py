from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required

from .models import Author, MobiFile

@login_required
def view(request, letter=None):
    if letter is None:
        return redirect('books:view', 'a')

    authors = Author.objects.filter(
        last_name_first=letter,
    ).prefetch_related('books__book')

    return render(request, 'books/view.html', {
        'letter': letter,
        'authors': authors,
        'letters': Author.objects.letters(),
    })

@login_required
def author(request, slug):
    author = get_object_or_404(Author, slug=slug)

    return render(request, 'books/author.html', {
        'author': author,
    })

@login_required
def mobi_file(request, mobi_file_id):
    mobi_file = get_object_or_404(MobiFile, pk=mobi_file_id)

    address = request.user.profile.kindle_email_address

    if not address:
        return redirect(mobi_file.file.url())

    message = EmailMessage(to=(address,))
    message.attach(
        '%d.mobi' % mobi_file.pk,
        default_storage.open(mobi_file.file.location).read(),
    )
    message.send()

    messages.success(request, '"%s" sent to Kindle.' % mobi_file.book.title)

    return redirect(mobi_file.book.authors.all()[0].author)
