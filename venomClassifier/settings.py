from pathlib import Path
from os.path import join, dirname, abspath

from django.contrib.messages import constants as error_messages


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'venomClassifierApp',
    'manageUsers',
    'predictionsapp',
    'crispy_forms',
    'django_rename_app',
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

ROOT_URLCONF = 'venomClassifier.urls'

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

WSGI_APPLICATION = 'venomClassifier.wsgi.application'



DATABASES = {
    
}



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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    join(BASE_DIR, 'static'),
]

STATIC_ROOT = join(BASE_DIR, 'staticfiles')

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CRISPY_TEMPLATES_PACK='bootstrap'

MESSAGE_TAGS={
    error_messages.DEBUG: 'debug',
    error_messages.INFO: 'info',
    error_messages.SUCCESS: 'success',
    error_messages.WARNING: 'warning',
    error_messages.ERROR: 'danger',
}

CSRF_TRUSTED_ORIGINS=['https://venom-classifier.herokuapp.com']