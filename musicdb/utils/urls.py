import urllib

from django.conf import settings

from musicdb.settings.hashes import HASHES

def google_search(terms):
    q = terms.encode('utf8') # urlencode doesn't like unicode strings
    return 'http://www.google.co.uk/search?%s' % urllib.urlencode({'q': q})

def google_image_search(terms):
    q = terms.encode('utf8') # urlencode doesn't like unicode strings
    return 'http://images.google.co.uk/images?%s' % urllib.urlencode({'q': q})

def static_media_url(path):
    return settings.STATIC_MEDIA_URL % {
        'path': path,
        'hash': HASHES.get(path, '-'),
    }
