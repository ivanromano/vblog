
from pathlib import Path
from corsheaders.defaults import default_headers
import os 
import environ
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env()

SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS_DEV')


# Application definition

LIBRERIAS = [ 
    'rest_framework', 
    'rest_framework.authtoken',
    # para mejores textos en el blog
    'ckeditor',
    'ckeditor_uploader',
    # para documentacion
    'drf_spectacular',
    'users',
    'vblog',
    'dist',
    'corsheaders',
]
 
CKEDITOR_CONFIG = {
    "default": {
        "toolbar": 'full',
        "autoParagraph": False

    }
}

CKEDITOR_UPLOAD_PATH = "/media/"

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + LIBRERIAS

JAZZMIN_SETTINGS = {
    "site_title": "Republic",
    "site_header": "Home",
    "site_brand": "Home",
    "copyright": "Republica Victinera",
    "welcome_sign": "Welcome Admin",
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'http://localhost:3001',

    'http://127.0.0.1:8000',
    'http://localhost:8000',

    'http://127.0.0.1:8001',
    'http://localhost:8001',

    'http://localhost:5173',
    'http://127.0.0.1:5173',

    'http://localhost:5174',
    'http://127.0.0.1:5174'
)

ROOT_URLCONF = 'core.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'dist/assets')
# ]


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

if not DEBUG:
    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS_DEPLOY')  
    # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'