from setup_warnings import *

from os.path import abspath, dirname, join

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Chris Lamb', 'chris@chris-lamb.co.uk'),
)
MANAGERS = ADMINS

INTERNAL_IPS = ('127.0.0.1',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'musicdb',
        'USER': 'musicdb',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '6432',
    }
}

MUSICDB_BASE_PATH = dirname(dirname(dirname(dirname(abspath(__file__)))))

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = ''

STATIC_MEDIA_URL = '/media/%(hash).6s/%(path)s'
STATIC_MEDIA_ROOT = join(MUSICDB_BASE_PATH, 'media')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'musicdb.auth.middleware.RequireLoginMiddleware',
    'musicdb.profile.middleware.ProfileMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'musicdb.debug.middleware.ShowForSuperusersMiddleware',
)

ROOT_URLCONF = 'musicdb.urls'

TEMPLATE_DIRS = (
    join(MUSICDB_BASE_PATH, 'templates'),
)

DEBUG_TOOLBAR_CONFIG = {
    'HIDE_DJANGO_SQL': True,
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': False,
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',

    'debug_toolbar',
    'django_extensions',
    'django_yadt',
    'treebeard',
    'storages',
    'south',

    'musicdb.auth',
    'musicdb.db',
    'musicdb.books',
    'musicdb.common',
    'musicdb.classical',
    'musicdb.debug',
    'musicdb.nonclassical',
    'musicdb.profile',
    'musicdb.static',
    'musicdb.unfiled',
    'musicdb.utils',
)

SECRET_KEY = 'EWf30GO9FL7rdgBpdUNuJF1RPx8mtmpFYOvcdNwMzhcyGk4Jxb'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_DEFAULT_ACL = 'private'
AWS_ACCESS_KEY_ID = 'AKIAJ2MH6KAU3WOSKPCQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'lamby-musicdb'

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

SESSION_COOKIE_AGE = 86400 * 365 * 10

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'musicdb',
    }
}

SITE_URL = 'https://musicdb.chris-lamb.co.uk/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'musicdb.utils.context_processors.settings_context',
)

LOGIN_URL = '/login'

DATABASE_ENGINE = 'dummy_for_debug_toolbar'

UNFILED_MEDIA_LOCATION  = '/srv/unfiled.chris-lamb.co.uk/unfiled_classical_music'

SECRET_HTTP_SUFFIX = '0BCidVG6'

UNFILED_MEDIA_LOCATION_HTTP = 'http://musicdb.chris-lamb.co.uk/unfiled/_%s' % SECRET_HTTP_SUFFIX

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptPasswordHasher',
)

SERVER_EMAIL = 'noreply@musicdb.chris-lamb.co.uk'
DEFAULT_FROM_EMAIL = SERVER_EMAIL

SOUTH_TESTS_MIGRATE = False

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
