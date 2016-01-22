import djcelery

from os.path import abspath, dirname, join

from apps import *
from setup_warnings import *

djcelery.setup_loader()

BASE_DIR = '/usr/share/python/musicdb'

# Fallback to relative location
if not __file__.startswith(BASE_DIR):
    BASE_DIR = dirname(dirname(dirname(dirname(abspath(__file__)))))

DEBUG = False

ADMINS = (
    ('Chris Lamb', 'chris@chris-lamb.co.uk'),
)
MANAGERS = ADMINS

INTERNAL_IPS = ('127.0.0.1',)
ALLOWED_HOSTS = ('*',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'musicdb',
        'USER': 'musicdb',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
    }
}

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

STATIC_URL = '/static/'
STATIC_ROOT = join(BASE_DIR, 'static')
STATICFILES_DIRS = (join(BASE_DIR, 'media'),)
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATICFILES_FINDERS = (
    'staticfiles_dotd.finders.DotDFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        join(BASE_DIR, 'templates'),
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'musicdb.utils.context_processors.settings_context',
        ],
        'builtins': [
            'django.contrib.staticfiles.templatetags.staticfiles',
            'django_autologin.templatetags.django_autologin',
            'musicdb.utils.templatetags.bootstrap',
            'musicdb.utils.templatetags.fonts',
            'musicdb.utils.templatetags.pagination',
            'musicdb.utils.templatetags.signing',
        ],
    },
}]

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'musicdb.utils.middleware.ShowForSuperusersMiddleware',
    'django_autologin.middleware.AutomaticLoginMiddleware',
)

ROOT_URLCONF = 'musicdb.urls'

SECRET_KEY = 'private'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_DEFAULT_ACL = 'private'
AWS_ACCESS_KEY_ID = 'private'
AWS_SECRET_ACCESS_KEY = 'private'
AWS_QUERYSTRING_EXPIRE = 86400 * 7 * 12
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

SITE_URL = 'overriden-in-productoin'

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/albums' # albums:view

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptPasswordHasher',
)

SERVER_EMAIL = 'overriden-in-production'
DEFAULT_FROM_EMAIL = SERVER_EMAIL

SOUTH_TESTS_MIGRATE = False

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

FONTS_ENABLED = True

BROKER_URL = 'redis://localhost:6379/0'

CELERYBEAT_SCHEDULE = {
}
