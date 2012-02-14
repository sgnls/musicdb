import os

from django.conf import settings
from django.utils.hashcompat import sha_constructor
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    require_model_validation = False

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError("build <role>")

        self.generate_hashes()

    def generate_hashes(self):
        print "I: Generating hashes"

        hashes = {}
        static_media = os.walk(settings.STATIC_MEDIA_ROOT)

        for dirpath, _, filenames in static_media:
            commonpath = os.path.commonprefix(
                (dirpath, settings.STATIC_MEDIA_ROOT),
            )

            for filename in filenames:
                fullpath = os.path.join(dirpath, filename)
                common_path = fullpath[len(commonpath) + 1:]

                sha = sha_constructor(open(fullpath, 'rb').read())
                hashes[common_path] = sha.hexdigest()

        target = os.path.join(
            settings.MUSICDB_BASE_PATH, 'musicdb/build/hashes.py',
        )

        open(target, 'wb').write("HASHES = %r" % hashes)
