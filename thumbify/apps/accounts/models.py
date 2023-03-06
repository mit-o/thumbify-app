from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)

from .managers import UserManager


class AccountTier(models.Model):
    name = models.CharField(max_length=64, unique=True)
    thumbnail_sizes = models.CharField(
        max_length=64,
        default="200",
        help_text="Comma-separated list of thumbnail sizes",
    )
    include_original_link = models.BooleanField(default=False)
    generate_expiring_link = models.BooleanField(default=False)
    thumbnail_sizes_list = property(lambda self: self.thumbnail_sizes.split(","))

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=64, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    tier = models.ForeignKey(
        AccountTier,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
    )

    USERNAME_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        return self.email
