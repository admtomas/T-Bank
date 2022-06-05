from django.contrib import admin

#* ---- CRATE CUSTOM USER/ACCOUNT, step 3
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CreateCustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CreateCustomUser
    list_display = ["email", "username",]

admin.site.register(CreateCustomUser, CustomUserAdmin)
