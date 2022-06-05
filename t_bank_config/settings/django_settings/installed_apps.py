# ---- APPS ----
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps

DJANGO_APPS = [
    # -- Default django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    # -- third party
    'rest_framework',
]

LOCAL_APPS = [
    # -- Your projects

    # ---- ACCOUNTS, CUSTOM USER
    'accounts',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS