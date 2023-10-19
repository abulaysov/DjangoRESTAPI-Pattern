from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users import models as user_models


@admin.register(user_models.User)
class AdminUser(UserAdmin):
    fieldsets = (
        (
            None,
            {"fields": ("username", "password")},
        ),
        (
            "Advanced options",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    list_display = [
        "id",
        "username",
    ]
