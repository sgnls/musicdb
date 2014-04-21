import os

from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import default_storage

PREFIX = 'unfiled/classical'

def view(request, path=None):
    if path is None:
        path = ''

    try:
        dirnames, filenames = default_storage.listdir(
            os.path.join(PREFIX, path),
        )
    except Exception, exc:
        return HttpResponse("Exception when listing dir: %r" % exc)

    dirnames = [{
        'name': x,
        'path': '%s/' % os.path.join(path, x),
    } for x in dirnames]

    filenames = [{
        'url': default_storage.url(os.path.join(PREFIX, path, x)),
        'name': x,
    } for x in filenames]

    return render(request, 'unfiled/view.html', {
        'path': path,
        'dirnames': dirnames,
        'filenames': filenames,
    })
