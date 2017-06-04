from .base import *

DEBUG = True
ADMIN_ENABLED = True

INSTALLED_APPS += []

# CORS Configurations

CORS_ORIGIN_ALLOW_ALL = True

# Cache Configurations

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache'
    }
}

# Logging Configurations

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': env('DJANGO_LOG_LEVEL', default='INFO'),
        },
    },
}

# Maximum Data Upload Configurations

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000
