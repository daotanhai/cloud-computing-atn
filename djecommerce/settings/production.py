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
        'NAME': 'd5192ojbjnl1u6',
        'USER': 'lfxyemofsfzdla',
        'PASSWORD': 'b426a6564603fc407bf5335b3cccd9bee7b17a76c9c2555bb3299c54409a182c',
        'HOST': 'ec2-34-230-167-186.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}


STRIPE_PUBLIC_KEY = 'your-live-public-key'
STRIPE_SECRET_KEY = 'your-live-secret-key'

