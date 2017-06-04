from .base import *

DEBUG = True
ADMIN_ENABLED = False

INSTALLED_APPS += []

# Cache Configurations

CACHES = {
    'default': env.cache()
}
