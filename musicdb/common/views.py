from django.db import models
from django.shortcuts import get_object_or_404, render

from musicdb.utils.http import render_playlist

from .models import MusicFile

def play_music_file(request, music_file_id):
    music_file = get_object_or_404(MusicFile, id=music_file_id)

    return render_playlist(request, [music_file])

def stats(request):
    total_duration = MusicFile.objects.aggregate(
        x=models.Sum('length'),
    )['x'] or 0

    return render(request, 'common/stats.html', {
        'total_duration': total_duration,
        'music_file_count': MusicFile.objects.count(),
    })
