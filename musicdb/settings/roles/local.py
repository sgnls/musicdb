DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'musicdb',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

SITE_URL = 'http://127.0.0.1:8000'
STATIC_MEDIA_URL = '/media/%(path)s'
