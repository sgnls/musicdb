from django.core.management.base import CommandError

from musicdb.utils.commands import AddFilesCommand

from musicdb.books.models import Author
from musicdb.common.models import File

class Command(AddFilesCommand):
    def handle_filenames(self, filenames):
        if len(filenames) != 1:
            raise CommandError("Must specify one file")

        filename = filenames[0]

        if not filename.lower().endswith('.mobi'):
            raise CommandError("Only .mobi files are supported.")

        last_name = self.prompt_string(
            'Author',
            Author.objects.all(),
            'last_name',
        )

        qs = Author.objects.filter(last_name=last_name)

        try:
            default = qs[0].first_names
        except IndexError:
            default = ''

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

        title = self.prompt_string(
            'Title',
            author.books.all(),
            'title',
            '',
        )

        book = author.books.create(title=title)

        File.objects.create_from_path(
            filenames[0],
            'books/%d/%d.mobi' % (book.pk, book.pk),
        )

        print "I: Added %s by %s %s" % (
            book.title,
            book.author.first_names,
            book.author.last_name,
        )
