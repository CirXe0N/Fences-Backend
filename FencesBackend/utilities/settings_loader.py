import os
from environ import environ

# Load Environment Variables
env = environ.Env()
environ.Env.read_env('.env')
project_name = os.path.basename(os.path.dirname(os.path.dirname(__file__)))


def load_settings():
    environment = env('ENVIRONMENT').lower()
    os.environ['DJANGO_SETTINGS_MODULE'] = '%s.settings.%s' % (project_name, environment)
