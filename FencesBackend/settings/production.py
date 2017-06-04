from .base import *

DEBUG = False
ADMIN_ENABLED = False

INSTALLED_APPS += []

# Cache Configurations

CACHES = {
    'default': env.cache()
}
