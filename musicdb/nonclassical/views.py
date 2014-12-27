# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from musicdb.utils.iter import chunk
from musicdb.utils.http import render_playlist

from .models import Artist, Album

@login_required
def view(request, letter=None):
    if letter is None:
        return redirect('nonclassical:view', 'a')

    artists = Artist.objects.filter(name_first=letter)

    return render(request, 'nonclassical/view.html', {
        'letter': letter,
        'letters': Artist.objects.letters(),
        'artists': artists,
    })

@login_required
def artist(request, slug):
    artist = get_object_or_404(Artist, slug=slug)

    return render(request, 'nonclassical/artist.html', {
        'artist': artist,
        'albums': chunk(artist.albums.all(), 4),
    })

@login_required
def album(request, artist_slug, slug):
    artist = get_object_or_404(Artist, slug=artist_slug)
    album = get_object_or_404(artist.albums, slug=slug)

    return render(request, 'nonclassical/album.html', {
        'album': album,
        'artist': artist,
    })

@login_required
def play_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    return render_playlist(request, album.get_tracks())

@login_required
def play_cd(request, album_id, cd_id):
    album = get_object_or_404(Album, pk=album_id)
    cd = get_object_or_404(album.cds.all(), pk=cd_id)

    return render_playlist(request, cd.get_tracks())
