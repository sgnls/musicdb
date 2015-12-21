import os
import urllib

from django.core.files import File as DjangoFile
from django.core.management.base import CommandError, make_option

from musicdb.utils.db import nextval
from musicdb.utils.commands import AddFilesCommand

from musicdb.common.models import File

from ...models import Author, Book, MobiFile

class Command(AddFilesCommand):
    option_list = AddFilesCommand.option_list + (
        make_option('-f', '--author-first-names', dest='first_names', default=None,
            action='store', help="Author first names (optional)"),
        make_option('-l', '--author-last-name', dest='last_name', default='',
            action='store', help="Author last name (optional)"),
        make_option('-t', '--title', dest='title', default='',
            action='store', help="Title (optional)"),
        make_option('-c', '--cover', dest='cover', default=None,
            action='store', help="Cover file/URL (optional)"),
    )

    def handle_filenames(self, filenames):
        if len(filenames) != 1:
            raise CommandError("Must specify one file")

        filename = filenames[0]

        if not filename.lower().endswith('.mobi'):
            raise CommandError("Only .mobi files are supported.")

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
                "Author forenames",
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
                "Title",
                author.books.all(),
                'title',
                '',
            )

        print " Author: %s" % author.long_name()
        print "  Title: %s" % title
        print "  Cover: %s" % self.options['cover']
        print

        if raw_input("Accept? [Yn] ").upper() not in ('', 'Y'):
            raise CommandError("Cancelling")

        # Need to know where to store the book before we create, hence manual
        # cursor manipulation
        book_pk = nextval('books_book_id_seq')

        # Store the file
        file_ = File.objects.create_from_path(
            filenames[0],
            'books/%d.mobi' % book_pk,
        )

        book = Book.objects.create(
            pk=book_pk,
            title=title,
        )

        MobiFile.objects.create(
            book=book,
            file=file_,
        )

        book.authors.create(num=1, author=author)

        if self.options['cover']:
            if 'http' in self.options['cover']:
                tempfile, _ = urllib.urlretrieve(self.options['cover'])

                try:
                    book.image.save(DjangoFile(open(tempfile)))
                    book.save()
                finally:
                    try:
                        os.unlink(tempfile)
                    except:
                        pass
            else:
                book.image.save(DjangoFile(open(self.options['cover'])))
                book.save()
