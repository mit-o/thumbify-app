from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.contrib.auth.base_user import BaseUserManager


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


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(("The Email must be set."))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(("SuperUser must be assigned to staff role"))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(("Super User must be assigned to super user role"))

        return self.create_user(email, password, **extra_fields)


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
