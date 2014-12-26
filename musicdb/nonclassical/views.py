# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect

from musicdb.utils.iter import chunk
from musicdb.utils.http import render_playlist

from .models import Artist, Album, CD

def index(request, letter=None):
    if letter is None:
        return redirect('nonclassical:letter', 'a')

    artists = Artist.objects.filter(name_first=letter)

    return render(request, 'nonclassical/index.html', {
        'letter': letter,
        'letters': Artist.objects.letters(),
        'artists': artists,
    })

def artist(request, slug):
    artist = get_object_or_404(Artist, slug=slug)

    return render(request, 'nonclassical/artist.html', {
        'artist': artist,
        'albums': chunk(artist.albums.all(), 4),
    })

def album(request, artist_slug, slug):
    artist = get_object_or_404(Artist, slug=artist_slug)
    album = get_object_or_404(artist.albums, slug=slug)

    return render(request, 'nonclassical/album.html', {
        'album': album,
        'artist': artist,
    })

def play_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    return render_playlist(request, album.get_tracks())

def play_cd(request, album_id, cd_id):
    album = get_object_or_404(Album, pk=album_id)
    cd = get_object_or_404(album.cds.all(), pk=cd_id)

    return render_playlist(request, cd.get_tracks())
