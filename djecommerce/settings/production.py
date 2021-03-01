from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd6p1d4oqvdjsl9',
        'USER': 'lgflanahjtlltc',
        'PASSWORD': 'b6ede30437b8a21b2f9702e90dddc5738adfd7ea0c6070d59454c23adbabc0ab',
        'HOST': 'ec2-54-146-73-98.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}


STRIPE_PUBLIC_KEY = 'your-live-public-key'
STRIPE_SECRET_KEY = 'your-live-secret-key'

