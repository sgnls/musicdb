import os
import errno
import subprocess

from django.conf import settings
from django.core.management.base import NoArgsCommand

TARGET = '%s/yadt/' % settings.MEDIA_ROOT

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        assert settings.DEBUG

        try:
            os.makedirs(TARGET)
        except OSError, e:
            if e.errno != errno.EEXIST:
                raise

        subprocess.check_call((
            's3cmd',
            'sync',
            '--verbose',
            '--delete-removed',
            's3://%s/yadt/' % settings.AWS_STORAGE_BUCKET_NAME,
            TARGET,
        ))
