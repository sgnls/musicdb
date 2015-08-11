import json
import urllib

def get_wikipedia_image(q):
    url = 'https://en.wikipedia.org/w/api.php?%s' % urllib.urlencode((
        ('format', 'json'),
        ('action', 'query'),
        ('titles', q.encode('utf-8')),
        ('piprop', 'original'),
        ('prop', 'pageimages'),
    ))

    data = json.loads(urllib.urlopen(url).read())

    try:
        image_url = data['query']['pages'].values()[0]['thumbnail']['original']
    except KeyError:
        return None

    return urllib.urlopen(image_url)
