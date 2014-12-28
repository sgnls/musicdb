import getpass
import optparse
import subprocess

from django.db import models
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import NoArgsCommand, CommandError

def psql(stdin, database=None, sudo=True, stop_on_error=True, gzip=False):
    args = []
    if sudo:
        args = [
            'sudo', 'sudo', '-u', settings.DATABASES['default']['USER'] or 'postgres',
        ]

    args.extend([
        'psql', '-v', 'client_min_messages=warning', '-e',
    ])

    if stop_on_error:
        args.extend(['-v', 'ON_ERROR_STOP=1'])

    host = settings.DATABASES['default'].get('HOST')
    if host:
        args.extend(['-h', host])

    if database:
        args.append(database)

    if isinstance(stdin, basestring):
        print ' '.join(args[1:])
        p = subprocess.Popen(args, stdin=subprocess.PIPE)
        p.communicate(input=stdin)
    else:
        print "%s | %s" % (' '.join(stdin), ' '.join(args))
        p1 = p2 = subprocess.Popen(stdin, stdout=subprocess.PIPE)

        if gzip:
            p2 = subprocess.Popen(
                ['gunzip', '-c'],
                stdin=p1.stdout,
                stdout=subprocess.PIPE,
            )

        p = subprocess.Popen(args, stdin=p2.stdout)
        p1.stdout.close()

    if p.wait() != 0:
        raise CommandError("Command failed")

class Command(NoArgsCommand):
    option_list = NoArgsCommand.option_list + (
        optparse.make_option(
            '--database-name',
            dest='database_name',
            help="Database name. [default: %default]",
            default='musicdb',
        ),
        optparse.make_option(
            '--hostname',
            dest='hostname',
            help="Remote host to sync from [default: %default]",
            default='tallis.chris-lamb.co.uk',
        ),
        optparse.make_option(
            '--no-data',
            dest='no_data',
            action='append',
            help="Model names of tables to not get data for [default: %default]",
            default=[
                'sessions.Session',
            ],
        ),
    )

    def handle_noargs(self, **options):
        assert settings.DEBUG

        psql('DROP DATABASE IF EXISTS %(database_name)s' % options)

        no_data_tables = [
            models.get_model(*model.split('.', 1))._meta.db_table
            for model in options['no_data']
        ]

        # Need to try a few locales because of Mac
        for locale in ('UTF8', 'UTF-8'):
            try:
                psql("""
                    CREATE DATABASE %(database)s WITH
                        TEMPLATE = template0
                        ENCODING = 'UTF-8'
                        LC_COLLATE = 'en_GB.UTF-8'
                        LC_CTYPE = 'en_GB.%(locale)s'
                        OWNER = %(owner)s
                """ % {
                    'owner': getpass.getuser(),
                    'locale': locale,
                    'database': options['database_name'],
                })
            except CommandError:
                # Might be okay
                continue

            # Get tables and data at the same time

            args = ['ssh', options['hostname'], 'sudo', '-u', 'postgres', 'pg_dump',
                '--no-owner', '--compress', '9']

            for table in no_data_tables:
                args.extend(['-T', table])

            psql(
                args + [options['database_name']],
                database=options['database_name'],
                gzip=True,
                sudo=False,
                stop_on_error=False,
            )

            # Create (empty) ignored tables.

            if options['no_data']:
                args = ['ssh', options['hostname'], 'sudo', '-u', 'postgres', 'pg_dump',
                    '--no-owner', '--compress', '9', '--schema-only']

                for table in no_data_tables:
                    args.extend(['-t', table])

                psql(
                    args + [options['database_name']],
                    database=options['database_name'],
                    gzip=True,
                    sudo=False,
                    stop_on_error=False,
                )

            # Create some other (empty) ignored tables
            call_command('syncdb')

            psql('UPDATE books_book SET image_exists = false')
            psql('UPDATE nonclassical_album SET image_exists = false')

            return

        raise CommandError("Could not sync database")
