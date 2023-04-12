SECRET_KEY = "django-insecure-u41#mntxg5r1gsypybca_v!l%t!u&^01((d9w#-0h^u##dlh3a"
DEBUG = True
AUTH_USER_MODEL = 'cv_generator.User'

ALLOWED_HOSTS = []
ROOT_URLCONF = "portfolio.urls"
WSGI_APPLICATION = "portfolio.wsgi.application"
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"