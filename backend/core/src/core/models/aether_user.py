from datetime import datetime
from typing import Any

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.apps import apps
from django.db import models


class AetherUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
        self,
        username: str,
        email: str,
        password: str,
        **extra_fields: dict[str, Any],
    ) -> "AetherUser":
        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self,
        email: str,
        username: str | None = None,
        password: str | None = None,
        **extra_fields: dict[str, Any],
    ) -> "AetherUser":
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(
        self,
        email: str,
        username: str | None = None,
        password: str | None = None,
        **extra_fields: dict[str, Any],
    ) -> "AetherUser":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


class AetherUser(AbstractBaseUser, PermissionsMixin):
    objects = AetherUserManager()
    username_validator = UnicodeUsernameValidator()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    username = models.CharField(
        _("username"),
        max_length=150,
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = models.EmailField(
        _("email"),
        unique=True,
    )
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    bio = models.CharField(max_length=150, blank=True, null=True)
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    created_at = models.DateTimeField(
        _("created_at"),
        default=datetime.now,
    )
    last_login = models.DateTimeField(_("last login"), blank=True, null=True)
    password = models.CharField(_("password"), max_length=128)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    def __str__(self):
        return f"{self.id} - {self.email}"
