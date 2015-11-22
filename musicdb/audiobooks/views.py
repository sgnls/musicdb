from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from musicdb.utils.http import render_playlist

from .models import Author, AudioBook

@login_required
def view(request, letter=None):
    if letter is None:
        return redirect('audiobooks:view', 'a')

    authors = Author.objects.filter(
        last_name_first=letter,
    )

    return render(request, 'audiobooks/view.html', {
        'letter': letter,
        'authors': authors,
        'letters': Author.objects.letters(),
    })

@login_required
def author(request, slug):
    author = get_object_or_404(Author, slug=slug)

    return render(request, 'audiobooks/author.html', {
        'author': author,
    })

@login_required
def play(request, audiobook_id):
    audiobook = get_object_or_404(AudioBook, pk=audiobook_id)

    return render_playlist(request, audiobook.get_tracks())
