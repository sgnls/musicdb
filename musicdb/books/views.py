from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.core.files.storage import default_storage
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import Author, MobiFile

@login_required
def view(request, letter=None):
    if letter is None:
        return redirect('books:view', 'a')

    authors = Author.objects.filter(
        last_name_first=letter,
    )

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

@require_POST
@login_required
def mobi_email(request, mobi_file_id):
    mobi_file = get_object_or_404(MobiFile, pk=mobi_file_id)

    address = request.user.profile.kindle_email_address

    if not address:
        messages.error(
            request,
            "You must first configure your Kindle email address."
        )
        return redirect('profile:view')

    message = EmailMessage(to=(address,))
    message.attach(
        '%d.mobi' % mobi_file.pk,
        default_storage.open(mobi_file.file.location).read(),
    )
    message.send()

    messages.success(request, '"%s" sent to Kindle.' % mobi_file.book.title)

    return redirect(mobi_file.book.authors.all()[0].author)

@login_required
def mobi_download(request, mobi_file_id):
    mobi_file = get_object_or_404(MobiFile, pk=mobi_file_id)

    return redirect(mobi_file.file.url())
