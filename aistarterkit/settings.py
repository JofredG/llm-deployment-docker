"""
Django settings for aistarterkit project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
ENV = os.getenv("ENVIRONMENT", 'development')

website_hostname = os.getenv('WEBSITE_HOSTNAME')

if ENV == 'development' or ENV == 'test':
    DEBUG = True
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
else:
    DEBUG = True
    ALLOWED_HOSTS = []
    if website_hostname:
        CSRF_TRUSTED_ORIGINS = ['https://' + website_hostname]
        ALLOWED_HOSTS.append(website_hostname)
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SAMESITE = 'None'
    CSRF_COOKIE_SAMESITE = 'None'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chat'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'aistarterkit.urls'
LOGIN_REDIRECT_URL = 'thread_list'  # or 'thread_list' or any other view you want to redirect to
LOGOUT_REDIRECT_URL = 'login'  # Assuming 'login' is the name of your login URL pattern

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'chat.context_processors.thread_list',  # Add this line
            ],
        },
    },
]

WSGI_APPLICATION = 'aistarterkit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# Get the SQLite storage path from the environment variable
sqlite_storage_path = os.getenv('SQLITE3_STORAGE_PATH')

if sqlite_storage_path:
    # If SQLITE3_STORAGE_PATH is set, use it as the directory
    db_path = Path(sqlite_storage_path) / 'db.sqlite3'
    # Create the directory if it doesn't exist
    os.makedirs(sqlite_storage_path, exist_ok=True)
else:
    # Otherwise, use BASE_DIR as the directory
    db_path = BASE_DIR / 'db.sqlite3'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(db_path),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(os.getenv('DJANGO_STATIC_ROOT', BASE_DIR), 'staticfiles')

os.makedirs(STATIC_ROOT, exist_ok=True)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'

DEFAULT_OPENAI_API_BASE = "https://api.openai.com/v1"

ENV_OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")

OPENAI_API_BASE = ENV_OPENAI_API_BASE if ENV_OPENAI_API_BASE else DEFAULT_OPENAI_API_BASE 

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)

AUTH_USER_MODEL = 'chat.CustomUser'

DEFAULT_ADMIN_USERNAME=os.getenv("DEFAULT_ADMIN_USERNAME")

DEFAULT_ADMIN_EMAIL=os.getenv("DEFAULT_ADMIN_EMAIL")

DEFAULT_ADMIN_PASSWORD=os.getenv("DEFAULT_ADMIN_PASSWORD")