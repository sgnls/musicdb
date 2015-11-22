import os

from lxml import etree

from django.http import HttpResponse
from django.utils import simplejson

def render_playlist(request, tracks):
    return XSPFResponse(tracks, filename=None)

class XSPFResponse(HttpResponse):
    def __init__(self, tracks, filename=None):
        if filename is None:
            filename = 'playlist.xspf'

        NSMAP = {
            None: 'http://xspf.org/ns/0/',
        }

        playlist = etree.Element('playlist', nsmap=NSMAP, attrib={
            'version': '1',
        })

        track_list = etree.SubElement(playlist, 'trackList')

        for track in tracks:
            elem = etree.SubElement(track_list, 'track')

            title = etree.SubElement(elem, 'title')
            title.text = track.get_parent_instance().title

            duration = etree.SubElement(elem, 'duration')
            duration.text = unicode(track.length * 1000)

            location = etree.SubElement(elem, 'location')
            location.text = track.file.url().replace('https:', 'http:')

        super(XSPFResponse, self).__init__(
            etree.tounicode(playlist),
            mimetype='application/xspf+xml',
        )

        self['Content-Disposition'] = 'attachment; filename=%s' % filename
