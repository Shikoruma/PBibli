import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG=True

# Web acces protections
ALLOWED_HOSTS = ['localhost']

CSRF_COOKIE_DOMAIN="localhost"

if DEBUG == False :
    SESSION_COOKIE_SECURE=True
    CSRF_COOKIE_SECURE=True
    USE_X_FORWARDED_HOST=True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

if DEBUG == True:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    STATIC_ROOT = ''
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "./static"),
    ]

