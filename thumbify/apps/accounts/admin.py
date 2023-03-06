from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import get_user_model
from .models import AccountTier

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    ordering = ["-created_at"]
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ("email", "is_staff", "created_at")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password", "tier")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "tier",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


@admin.register(AccountTier)
class AccountTierAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "thumbnail_sizes",
        "include_original_link",
        "generate_expiring_link",
    )
