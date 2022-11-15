from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Admin
from .forms import UserCreationForm, UserChangeForm

User = get_user_model()
admin.site.unregister(Group)


@admin.register(Admin)
class AdminModel(admin.ModelAdmin):
    list_display = ["user", "admin"]


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["email", "full_name", "admin"]
    list_filter = ("is_admin",)

    fieldsets = (
        ("Authentication", {"fields": ("email",)}),
        ("Personal Info", {"fields": ("full_name",)}),
        ("Permissions", {"fields": ("is_admin",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "full_name", "password1", "password2"),
            },
        ),
    )

    search_fields = (
        "email",
        "full_name",
    )
    ordering = ("email",)
    filter_horizontal = ()
