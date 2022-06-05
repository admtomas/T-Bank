from django.db import models
from django.contrib.auth.models import AbstractUser

#* ---- CREATE CUSTOM USER/ACCOUNT MODEL, step 1
class CreateCustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
