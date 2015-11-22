from django.core.management.base import CommandError

from musicdb.utils.commands import AddMusicFilesCommand

from ...models import Author

class Command(AddMusicFilesCommand):
    def handle_files(self, files):
        self.show_filenames(files)

        if not files:
            raise CommandError("Must specify at least one filename")

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

        title = self.prompt_string(
            "Title",
            author.books.all(),
            'title',
            '',
        )

        print " Author: %s" % author.long_name()
        print "  Title: %s" % title
        print

        if raw_input("Accept? [Yn] ").upper() not in ('', 'Y'):
            raise CommandError("Cancelling")

        audiobook = author.books.create(title=title)

        self.copy_and_tag(
            files,
            'audiobooks/%d' % audiobook.pk,
            'audiobook_track',
            audiobook.tracks,
            tag=False,
        )
