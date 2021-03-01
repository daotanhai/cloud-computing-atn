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
        'NAME': 'ddt0a6dcqdl63h',
        'USER': 'gsvliwarukkkzq',
        'PASSWORD': '8a4c148d0a2f926fc025b5f336ad832107ad71fe682c687a24de67914cc36eff',
        'HOST': 'ec2-54-155-87-214.eu-west-1.compute.amazonaws.com',
        'PORT': '5432'
    }
}


STRIPE_PUBLIC_KEY = 'your-live-public-key'
STRIPE_SECRET_KEY = 'your-live-secret-key'

