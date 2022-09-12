from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-gbbhs345-3nvdmq-)l39*fw8342t%nc(@x(-i4y6)nd^)pb-d2#^6g9+@gy'

DEBUG = False

ALLOWED_HOSTS = ['mikhaillazarev.pythonanywhere.com', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'catalog/static',
]

STATIC_ROOT = BASE_DIR / 'assets'
