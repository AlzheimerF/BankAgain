from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Profile, Info, SecretInfo, Rate

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Profile
    list_display = ['id', 'username', 'email', 'is_staff', 'date_joined', ]

admin.site.register(Profile, CustomUserAdmin)
admin.site.register(Info)
admin.site.register(SecretInfo)
admin.site.register(Rate)
