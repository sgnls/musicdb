import os
import urllib

from lxml import etree

BASE_URL = 'http://www.amazon.co.uk/s/'

def guess_book_details(val):
    val = os.path.basename(val)
    val = os.path.splitext(val)[0]

    url = '%s?%s' % (BASE_URL, urllib.urlencode((
        ('url', 'search-alias=stripbooks'),
        ('field-keywords', val),
    )))

    root = etree.HTML(urllib.urlopen(url).read())
    url = root.xpath(
        '//div[contains(@class, "result")]//div[@class="productTitle"]/a',
    )[0].attrib['href']

    root = etree.HTML(urllib.urlopen(url).read())

    title = root.xpath('//span[@id="btAsinTitle"]/span/text()')[0].strip()
    title = title.replace(' (Vintage Classics)', '')
    title = title.strip()

    authors = []
    for x in root.xpath(
        '//div[@class="buying"][h1[@class="parseasinTitle"]]/a'
    ):
        if x.getnext().text == "(Author)":
            authors.append(x.text)

    if len(authors) != 1:
        return

    first_names, last_name = authors[0].split(' ', 1)

    cover_url = root.xpath('//img[@id="main-image-nonjs"]')[0].attrib['src']

    return {
        'title': title,
        'first_names': first_names,
        'last_name': last_name,
        'cover_url': cover_url,
    }
