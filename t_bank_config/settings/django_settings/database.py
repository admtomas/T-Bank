# ---- POSTGRES SETUP ----
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# ---- DJANGO ENVIRON ----
import environ
import os
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'postgres',
        'NAME': 'T_BANK',
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': 5432,
        },
    }
