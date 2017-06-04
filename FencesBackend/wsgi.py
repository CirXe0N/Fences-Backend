from django.core.wsgi import get_wsgi_application
from .utilities.settings_loader import load_settings

load_settings()
application = get_wsgi_application()
