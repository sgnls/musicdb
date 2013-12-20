import os
import urllib

from lxml import etree

from django.db import connection
from django.core.files import File as DjangoFile
from django.core.management.base import CommandError, make_option

from musicdb.utils.commands import AddFilesCommand

from musicdb.common.models import File

from ...models import Author, Book

class Command(AddFilesCommand):
    option_list = AddFilesCommand.option_list + (
        make_option('-f', '--author-first-names', dest='first_names', default=None,
            action='store', help="Author first names (optional)"),
        make_option('-l', '--author-last-name', dest='last_name', default='',
            action='store', help="Author last name (optional)"),
        make_option('-t', '--title', dest='title', default='',
            action='store', help="Title (optional)"),
        make_option('-c', '--cover', dest='cover_url', default=None,
            action='store', help="Cover URL (optional)"),
    )

    def handle_filenames(self, filenames):
        if len(filenames) != 1:
            raise CommandError("Must specify one file")

        filename = filenames[0]

        if not filename.lower().endswith('.mobi'):
            raise CommandError("Only .mobi files are supported.")

        data = guess_book_details(filename)

        if not data:
            raise CommandError("Could not guess book details")

        self.options.update(data)

        last_name = self.options['last_name']
        if not last_name:
            last_name = self.prompt_string(
                "Author last name",
                Author.objects.all(),
                'last_name',
            )

        qs = Author.objects.filter(last_name=last_name)

        try:
            default = qs[0].first_names
        except IndexError:
            default = ''

        first_names = self.options['first_names']
        if not self.options['first_names']:
            first_names = self.prompt_string(
                'Author forenames',
                qs,
                'first_names',
                default,
            )

        author, _ = Author.objects.get_or_create(
            last_name=last_name,
            first_names=first_names,
        )

        title = self.options['title']

        if not title:
            title = self.prompt_string(
                'Title',
                author.books.all(),
                'title',
                '',
            )

        print " Author: %s" % author.long_name()
        print "  Title: %s" % title
        print "  Cover: %s" % self.options['cover_url']
        print

        if raw_input("Accept? [Yn] ").upper() not in ('', 'Y'):
            raise CommandError("Cancelling")

        cursor = connection.cursor()
        cursor.execute("SELECT NEXTVAL('books_book_id_seq')")
        book_pk = cursor.fetchone()[0]

        # Store the file
        file_ = File.objects.create_from_path(
            filenames[0],
            'books/%d.mobi' % book_pk,
        )

        book = Book.objects.create(
            pk=book_pk,
            title=title,
            file=file_,
        )

        book.authors.create(num=1, author=author)

        if self.options['cover_url']:
            tempfile, _ = urllib.urlretrieve(self.options['cover_url'])

            try:
                book.image.save(DjangoFile(open(tempfile)))
                book.save()
            finally:
                try:
                    os.unlink(tempfile)
                except:
                    pass

        print "I: Added."

def guess_book_details(val):
    val = os.path.basename(val)
    val = os.path.splitext(val)[0]

    url = 'http://www.amazon.co.uk/s/?%s' % urllib.urlencode((
        ('url', 'search-alias=stripbooks'),
        ('field-keywords', val),
    ))

    print "I: Performing search: %s" % url
    root = etree.HTML(urllib.urlopen(url).read())
    url = root.xpath(
        '//div[contains(@class, "result")]//div[@class="productTitle"]/a',
    )[0].attrib['href']

    print "I: Downloading details: %s" % url
    root = etree.HTML(urllib.urlopen(url).read())

    title = root.xpath('//span[@id="btAsinTitle"]/span/text()')[0].strip()
    title = title.replace(' (Vintage Classics)', '')
    title = title.replace(' (Modern Classics)', '')
    title = title.replace(' (Penguin Modern Classics)', '')
    title = title.strip()

    authors = []
    for x in root.xpath(
        '//div[@class="buying"][h1[@class="parseasinTitle"]]/a'
    ):
        authors.append((x.text, x.getnext().text))

    if len(authors) > 1:
        authors = [(x, y) for x, y in authors if y == "(Author)"]

    if len(authors) != 1:
        return

    first_names, last_name = authors[0][0].split(' ', 1)

    cover_url = root.xpath('//img[@id="main-image-nonjs"]')[0].attrib['src']
    cover_url = cover_url.split('._BO2')[0] + '.jpg'

    return {
        'title': title,
        'first_names': first_names,
        'last_name': last_name,
        'cover_url': cover_url,
    }

