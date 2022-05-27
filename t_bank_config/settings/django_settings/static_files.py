# STATIC & MEDIA SETTINGS ----
# Static files (CSS, JavaScript, Images)

# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = "/static/"

# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
#STATIC_ROOT = str(ROOT_DIR / "staticfiles")

# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
#STATICFILES_DIRS = [str(APPS_DIR / "static")]

# https://docs.djangoproject.com/en/4.0/ref/contrib/staticfiles/
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# https://docs.djangoproject.com/en/4.0/ref/settings/#media-root
#MEDIA_ROOT = str(APPS_DIR / "media")

MEDIA_URL = "/media/"