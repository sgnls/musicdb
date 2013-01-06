from django.core.management.base import CommandError, make_option

from musicdb.utils.commands import AddFilesCommand

from musicdb.books.models import Author
from musicdb.common.models import File

class Command(AddFilesCommand):
    option_list = AddFilesCommand.option_list + (
        make_option('-f', '--author-first-names', dest='first_names', default='',
            action='store', help="Author first names (optional)"),
        make_option('-l', '--author-last-name', dest='last_name', default='',
            action='store', help="Author last name (optional)"),
        make_option('-t', '--title', dest='title', default='',
            action='store', help="Title (optional)"),
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
                'Author',
                Author.objects.all(),
                'last_name',
            )

        qs = Author.objects.filter(last_name=last_name)

        try:
            default = qs[0].first_names
        except IndexError:
            default = ''

        first_names = self.options['first_names']

        if not first_names:
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

        book = author.books.create(title=title)

        book.file = File.objects.create_from_path(
            filenames[0],
            'books/%d/%d.mobi' % (book.pk, book.pk),
        )

        book.save()

        print "I: Added %s by %s %s" % (
            book.title,
            book.author.first_names,
            book.author.last_name,
        )
