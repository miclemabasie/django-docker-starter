from pathlib import Path
import environ
import logging
from datetime import timedelta
import logging.config
from django.utils.log import DEFAULT_LOGGING
from django.utils.translation import gettext_lazy as _

from pathlib import Path

env = environ.Env(DEBUG=(bool, False))
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
environ.Env.read_env(BASE_DIR / ".env")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-t+4t*bp23a(n1o8##%7fqki&^+rf!4o031e4@cjt^(xgb&__31"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# ----------------------------
# Django core applications
# ----------------------------
DJANGO_APPS = [
    "django.contrib.admin",  # Django admin interface for managing data
    "django.contrib.auth",  # Authentication system (users, permissions, passwords)
    "django.contrib.contenttypes",  # Generic relations and permission framework backbone
    "django.contrib.sessions",  # Session management (server-side sessions)
    "django.contrib.messages",  # Flash messages framework (success, error, info)
    "django.contrib.staticfiles",  # Static file handling (CSS, JS, images)
]

# ----------------------------
# Local project applications
# ----------------------------
LOCAL_APPS = [
    "apps.users.apps.UsersConfig",  # Custom user app (auth extensions, profiles, roles)
    "apps.core.apps.CoreConfig",  # Core/shared logic (utils, base models, constants)
]

# ----------------------------
# Third-party applications
# ----------------------------
THIRD_PARTY_APPS = [
    # "modeltranslation",              # Multilingual model fields (i18n at database level)
    # "autoslug",                      # Automatic, SEO-friendly slug generation
    # "django_extensions",             # Developer utilities (shell_plus, graph_models, etc.)
    # "django_elasticsearch_dsl",      # Elasticsearch integration via Django ORM signals
    # "allauth",                       # Complete authentication framework
    # "allauth.socialaccount",         # Social login support (OAuth plumbing)
    # "allauth.socialaccount.providers.google",  # Google OAuth provider
    # "allauth.account",               # Email-based auth, registration, verification
    # "corsheaders",                   # Cross-Origin Resource Sharing (API access from browsers)
    # "rest_framework",                # Django REST Framework (APIs, serializers, views)
    # "rest_framework_simplejwt",      # JWT authentication for DRF (stateless auth)
    # "djoser",                        # REST endpoints for auth (login, register, reset password)
    # "formtools",                     # Advanced form workflows (wizards, multi-step forms)
    # "djcelery_email",                # Async email sending via Celery
    # "drf_spectacular",               # OpenAPI 3 schema generation (Swagger / Redoc)
]

# ----------------------------
# Final installed apps
# ----------------------------
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS


AUTH_USER_MODEL = "users.User"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "djangostarter.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "djangostarter.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
