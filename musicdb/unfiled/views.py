import os
import re

from django.http import Http404
from django.conf import settings
from django.shortcuts import render

from musicdb.utils.http import XSPFResponse

from .utils import Track

re_show_play = re.compile(r'\.(mp3|flac)$', re.IGNORECASE)

def view(request):
    try:
        rel_path = request.GET['x']
        parent = os.path.dirname(rel_path)
    except KeyError:
        rel_path = ''
        parent = None

    abs_path = os.path.realpath(
        os.path.join(settings.UNFILED_MEDIA_LOCATION, rel_path)
    )

    if not abs_path.startswith(settings.UNFILED_MEDIA_LOCATION):
        raise Http404

    if not os.path.isdir(abs_path):
        raise Http404

    entries = [{
        'name': x,
        'isdir': os.path.isdir(os.path.join(abs_path, x)),
        'abs_path': os.path.join(abs_path, x),
        'rel_path': os.path.join(rel_path, x),
        'show_play': bool(re_show_play.search(x)),
    } for x in os.listdir(abs_path)]

    entries.sort(key=lambda x: (not x['isdir'], x['name']))

    return render(request, 'unfiled/view.html', {
        'parent': parent,
        'entries': entries,
        'rel_path': rel_path,
        'show_parent': parent is not None,
    })

def play(request):
    try:
        rel_path = request.GET['x']
    except KeyError:
        raise Http404

    abs_path = os.path.realpath(
        os.path.join(settings.UNFILED_MEDIA_LOCATION, rel_path)
    )

    if not os.path.exists(abs_path):
        raise Http404

    return XSPFResponse(
        [Track(rel_path)],
        prefix=settings.UNFILED_MEDIA_LOCATION_HTTP,
    )
