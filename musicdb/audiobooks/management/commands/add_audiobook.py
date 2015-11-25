import os
import shutil
import tempfile
import subprocess

from django.core.management.base import CommandError

from musicdb.utils.commands import AddMusicFilesCommand

from ...models import Author

class Command(AddMusicFilesCommand):
    def handle_prompt(self, files):
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

        self.audiobook = author.books.create(title=title)

    def handle_filenames(self, files):
        tempdir = tempfile.mkdtemp(prefix='musicdb-add_audiobook-')
        result = []
        for idx, val in enumerate(files, 1):
            if os.path.isfile(val):
                result.append(val)
                continue

            subprocess.check_call((
                'youtube-dl',
                val,
                '--extract-audio',
                '--audio-format', 'mp3',
                '--audio-quality', '4',
                '--output',
                '%s/%d.%%(ext)s' % (tempdir, idx),
            ))

            result.append('%s/%d.mp3' % (tempdir, idx))

        try:
            super(Command, self).handle_filenames(result)
        finally:
            shutil.rmtree(tempdir, ignore_errors=True)

    def handle_files(self, files):
        self.copy_and_tag(
            files,
            'audiobooks/%d' % self.audiobook.pk,
            'audiobook_track',
            self.audiobook.tracks,
            tag=False,
        )

