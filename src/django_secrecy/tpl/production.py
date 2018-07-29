from django_secrecy.utils import get_secret

from .base import BASE_DIR, PROJ_NAME


DEBUG = False
# CHANGE '*' - on your domain names
ALLOWED_HOSTS = ['*']

# Default MySql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_secret('NAME', BASE_DIR, PROJ_NAME),
        'USER': get_secret('USER', BASE_DIR, PROJ_NAME),
        'PASSWORD': get_secret('PASSWORD', BASE_DIR, PROJ_NAME),
        'HOST': '',
        'PORT': '',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_unicode_ci'
        }
    }
}
