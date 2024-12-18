"""
Django settings for math_learning project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

import environ
from kombu import Queue

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", False)

RUN_TEST = env.bool("RUN_TEST", False)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", [])


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "js_routes",
    "inertia",
    "webpack_loader",
    "django_countries",
    "django_user_agents",
    "django_celery_beat",
    "django_extensions",
    "apps.core",
    "apps.accounts",
    "apps.management",
    "apps.learning",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_user_agents.middleware.UserAgentMiddleware",
    "inertia.middleware.InertiaMiddleware",
    "apps.accounts.middleware.AuthPropsMiddleware",
    "apps.core.middleware.CorePropsMiddleware",
    "apps.core.middleware.SessionIdleTimeout",
]

ROOT_URLCONF = "math_learning.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "apps/core/templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "math_learning.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": env.str("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": env.str("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": env.str("SQL_USER", "user"),
        "PASSWORD": env.str("SQL_PASSWORD", "password"),
        "HOST": env.str("SQL_HOST", "localhost"),
        "PORT": env.str("SQL_PORT", "5432"),
    }
}

# Wrap all requests funtions with transaction.atomic
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 8,
        },
        "IDENTIFIER": "minimum",
    },
    {
        "NAME": "apps.accounts.validators.AtLeastOneDigitValidator",
        "IDENTIFIER": "number",
    },
    {
        "NAME": "apps.accounts.validators.AtLeastOneUpperLetterValidator",
        "IDENTIFIER": "uppercase",
    },
    {
        "NAME": "apps.accounts.validators.AtLeastOneLowerLetterValidator",
        "IDENTIFIER": "lowercase",
    },
    {
        "NAME": "apps.accounts.validators.AtLeastOneSpecialCharacterValidator",
        "IDENTIFIER": "special",
    },
]

AUTH_USER_MODEL = "core.CustomUser"

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

LANGUAGES = [
    ("es", "Spanish"),
    ("en-us", "English"),
]

JS_INFO_DICT = {
    "packages": (
        "apps.core",
        "apps.accounts",
        "apps.management",
        "apps.learning",
    )
}

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# ------------------------------------------------------------------------------
# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"
# ------------------------------------------------------------------------------

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


JS_ROUTES_INCLUSION_LIST = ["core", "accounts", "management", "learning"]

# CSRF_HEADER_NAME="HTTP_X_CSRFTOKEN"
VERSION = 2
CSRF_COOKIE_NAME = "XSRF-TOKEN"
CSRF_HEADER_NAME = "HTTP_X_XSRF_TOKEN"
INERTIA_SHARE = False
INERTIA_LAYOUT = "base.html"

WEBPACK_LOADER = {
    "DEFAULT": {
        # 'CACHE': not DEBUG,
        "BUNDLE_DIR_NAME": "static/dist/",
        "STATS_FILE": os.path.join(BASE_DIR, "webpack-stats.json"),
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
    }
}

# Email Settings
EMAIL_BACKEND = env.str(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)
# EMAIL CONFIG
EMAIL_FROM_ADDR = env.str("EMAIL_FROM_ADDR", "admin@math_learning.com")
EMAIL_HOST = env.str("EMAIL_HOST", "localhost")
EMAIL_PORT = env.int("EMAIL_PORT", 1025)
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=False)
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", "")
EMAIL_VERIFICATION = "none"

# CORE
MAX_SIZE_FILE = 10

# CELERY
CELERY_TASK_DEFAULT_QUEUE = "default"

# Force all queues to be explicitly listed in `CELERY_TASK_QUEUES` to help prevent typos
CELERY_TASK_CREATE_MISSING_QUEUES = False

CELERY_TASK_QUEUES = (
    # need to define default queue here or exception would be raised
    Queue("default"),
    Queue("high_priority"),
    Queue("low_priority"),
)

CELERY_BROKER_URL = env.str("CELERY_BROKER", "redis://127.0.0.1:6379/0")
CELERY_RESULT_BACKEND = env.str("CELERY_BACKEND", "redis://127.0.0.1:6379/0")


# Dynamic task routing for celery
def route_task(name, args, kwargs, options, task=None, **kw):
    if ":" in name:
        queue, _ = name.split(":")
        return {"queue": queue}
    return {"queue": "default"}


CELERY_TASK_ROUTES = (route_task,)
