import os
import stat
import mimetypes

from django_yadt.utils import get_variant_from_path

from django.http import Http404
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotModified
from django.utils.http import http_date
from django.views.static import was_modified_since, serve

def media(request, path):
    fullpath = os.path.join(settings.STATIC_MEDIA_ROOT, path)

    if not os.path.isdir('%s.d' % fullpath):
        return serve(
            request,
            path,
            document_root=settings.STATIC_MEDIA_ROOT,
            show_indexes=True,
        )

    latest = -1
    filenames = []

    for root, _, files in os.walk('%s.d' % fullpath, followlinks=True):
        for filename in [os.path.join(root, x) for x in files]:
            if filename.endswith('~'):
                continue
            filenames.append(filename)
            latest = max(latest, os.stat(filename)[stat.ST_MTIME])

    mimetype = mimetypes.guess_type(fullpath)[0] or 'application/octet-stream'

    if not was_modified_since(
        request.META.get('HTTP_IF_MODIFIED_SINCE'),
        latest,
    ):
        return HttpResponseNotModified(mimetype=mimetype)

    contents = ""
    for filename in sorted(filenames):
        with open(filename) as f:
            contents += f.read()

    response = HttpResponse(contents, mimetype=mimetype)
    response['Last-Modified'] = http_date(latest)
    response['Content-Length'] = len(contents)

    return response

def storage(request, path):
    try:
        return serve(
            request,
            path,
            show_indexes=True,
            document_root=settings.MEDIA_ROOT,
        )
    except Http404:
        variant = get_variant_from_path(path)

        if variant is None or not variant.fallback:
            raise

        return media(request, os.path.join(
            'img',
            'yadt_fallbacks',
            variant.fallback_filename(),
        ))
