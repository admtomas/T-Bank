from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CreateCustomUser

#* ---- CRATE CUSTOM USER/ACCOUNT, step 2
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CreateCustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CreateCustomUser
        fields = ("username", "email")