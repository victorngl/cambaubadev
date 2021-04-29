'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''
import os

from decouple import config
from dj_database_url import parse as dburl
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = [
    'localhost',
    'cambauba.herokuapp.com',
    'cambauba.dokku.outboxsistemas.com',
    'intranet.cambauba.org.br',
    'intranet.cambauba.com.br',
    'novo.cambauba.com.br',
]

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrapform',
    'djrichtextfield',
    'avatar',
    'core',
    'home',
    'emails',
    'atividades',
    'enquetes',
    'escolas',
    'informativos',
    'atividades_escolares',
    'materiais_didaticos',
    'calendario',
    'django_bleach',
    'django_quill',
    'colorfield',
    'import_export',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'crum.CurrentRequestUserMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cambauba.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cambauba.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

PRODUCAO = config('PRODUCAO', default=True, cast=bool)
default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

if PRODUCAO:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'intranet_cambauba',
            'USER': 'intranet_cambauba_user',
            'PASSWORD': 'D@t@C@rt3sC@mb@ub@',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join('/var/www/html/static')

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join('/var/www/html/media')
else:
    DATABASES = {
        'default': config(
            'DATABASE_URL',
            default=default_dburl,
            cast=dburl
        ),
    }

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DJRICHTEXTFIELD_CONFIG = {
    'js': ['//cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js'],
    'init_template': 'djrichtextfield/init/tinymce.js',
    'settings': {
        'menubar': False,
        'plugins': 'link image',
        'toolbar': 'bold italic | link image | removeformat',
        'width': 700
    }
}