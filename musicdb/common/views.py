from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from musicdb.utils.http import render_playlist

from .models import MusicFile

@login_required
def play_music_file(request, music_file_id):
    music_file = get_object_or_404(MusicFile, pk=music_file_id)

    return render_playlist(request, [music_file])
