from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Admin

admin.site.unrigester(Group)


@admin.register(Admin)
class AdminModel(admin.ModelAdmin):
    list_display = ["user", "admin"]
