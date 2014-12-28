import os
import urllib

from django.core.files import File as DjangoFile

def set_artwork_from_url(album, url):
    tempfile, _ = urllib.urlretrieve(url)
    try:
        album.image.save(DjangoFile(open(tempfile)))
        album.save()
    except:
        album.cover.delete()
        raise
    finally:
        try:
            os.unlink(tempfile)
        except:
            pass
