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
    'treebeard',
    'south',

    'musicdb.auth',
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

# Make this unique, and don't share it with anybody.
try:
    with open('/var/lib/musicdb/key', 'r') as f:
        SECRET_KEY = f.read().strip()
except IOError:
    SECRET_KEY = 'gh*w7@sdfj4%i=xyjatf_@!wx^d#tam^&5q6(f=z6io-302iwu'

MEDIA_ROOT = 'site_media'
MEDIA_URL = '/site_media/'

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

MEDIA_LOCATION = '/srv/musicdb.chris-lamb.co.uk'
UNFILED_MEDIA_LOCATION  = '/srv/files.chris-lamb.co.uk/unfiled_classical_music'

try:
    with open('/var/lib/musicdb/http_suffix', 'r') as f:
        SECRET_HTTP_SUFFIX = f.read().strip()
except IOError:
    SECRET_HTTP_SUFFIX = 'z7DukHiMKH'

MEDIA_LOCATION_HTTP = 'http://musicdb.chris-lamb.co.uk/_%s' % SECRET_HTTP_SUFFIX
UNFILED_MEDIA_LOCATION_HTTP = 'http://musicdb.chris-lamb.co.uk/unfiled/_%s' % SECRET_HTTP_SUFFIX

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptPasswordHasher',
)

SERVER_EMAIL = 'noreply@musicdb.chris-lamb.co.uk'

SOUTH_TESTS_MIGRATE = False

GOOGLE_MUSIC_EMAIL = 'chris@chris-lamb.co.uk'

try:
    with open('/var/lib/musicdb/google_music', 'r') as f:
        GOOGLE_MUSIC_PASSWORD = f.read().strip()
except IOError:
    GOOGLE_MUSIC_PASSWORD = None
