# ---- EMAIL SETTINGS ----
# ---- DJANGO ENVIRON ----
import environ
import os
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

#?Use mailtrap.io for testing
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.mailtrap.io'
# EMAIL_HOST_USER = env('MAILTRAP_USER')
# EMAIL_HOST_PASSWORD = env('MAILTRAP_PASSWORD')
# EMAIL_PORT = '2525'
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False