from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$voqhisg+qe6a1uvdjn%qpqq=5o)fe901lk#36l-sm^q3s4!c@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'django_celery_results',
    'django_celery_beat'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'client.urls'

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

WSGI_APPLICATION = 'client.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password valdjango_celery_resultsidation
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

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


"""Celery settings 
Celery Configuration Options

Use this if you want to use redis for results
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0

Make sure redis is installed 
Check with this command from you terminal  "❯ redis-cli > 127.0.0.1:6379>"""
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'

"""OR this if you want to use django-admin panel for results"""
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TIMEZONE = "Asia/Kolkata"
 
"""Enable extended task result atributes (name, args, worker, 
    retries, queue, delhivery-info to be written to back end (basicaly to check from admin panel))"""
CELERY_RESULT_EXTENDED  = True


# Beat conf
# https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html
# Methode 1 if want to use this comment from celery.py
"""'args': ("hey im still runing", ) why ',' this 
is because we have only one argument """

# if this is commented here check celery.py
# CELERY_BEAT_SCHEDULE = {
#     'every-10-second': {
#         'task': 'app.tasks.every_10_second',
#         'schedule': 10,
#         'args': ("why are you runnig", )
#     }
# }



CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
