# ---- DJANGO REST FRAMEWORK SETTINGS ----
#  https://www.django-rest-framework.org/api-guide/settings/
# REST_FRAMEWORK = {
#     "DEFAULT_AUTHENTICATION_CLASSES": (
#         "rest_framework.authentication.SessionAuthentication",
#         "rest_framework.authentication.TokenAuthentication",
#     ),
#     "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
#     "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
# }

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}