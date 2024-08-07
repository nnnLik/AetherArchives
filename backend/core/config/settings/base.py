import os.path
import sys
from pathlib import Path

from .constants import application_consts

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DEBUG = application_consts.server.DEBUG
TESTING = "test" in sys.argv

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "djoser",
    "storages",
    "drf_yasg",
    "src.memos",
    "src.core",
    "src.pages",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "config.wsgi.application"
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_LOCATION = "static"
STATICFILES_STORAGE = "src.core.storage.S3StaticStorage"

MEDIA_URL = "/media/"
DEFAULT_FILE_STORAGE = "src.core.storage.S3MediaStorage"

AWS_ACCESS_KEY_ID = application_consts.s3_server.AWS_S3_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = application_consts.s3_server.AWS_S3_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME = application_consts.s3_server.AWS_S3_STORAGE_BUCKET_NAME
AWS_S3_ENDPOINT_URL = application_consts.s3_server.AWS_S3_ENDPOINT_URL
MINIO_ACCESS_URL = application_consts.s3_server.MINIO_ACCESS_URL
AWS_S3_USE_SSL = application_consts.s3_server.AWS_S3_USE_SSL

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "core.AetherUser"

LOGIN_URL = "/auth/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/auth/login"

if DEBUG and not TESTING:
    MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
    INSTALLED_APPS += ("debug_toolbar",)

    DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda _request: DEBUG}
