import uuid

# Import for Google Maps API
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    Group,
    Permission,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

import requests
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.core.models import Gender, TimeStampedUUIDModel

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    pkid = models.BigAutoField(primary_key=True, editable=False)
    username = models.CharField(verbose_name=_("Username"), max_length=250)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=250)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=250)
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = CustomUserManager()

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True,
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        indexes = [
            models.Index(fields=["email"]),
        ]

    def __str__(self) -> str:
        return f"{self.username} - {self.email}"

    def get_fullname(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    def get_short_name(self):
        return self.username

    def membership_duration(self):
        """Returns time since account creation in human-readable format"""
        from django.utils.timesince import timesince

        return timesince(self.date_joined)

    def last_active(self):
        """Returns time since last login in human-readable format"""
        from django.utils.timesince import timesince

        return timesince(self.last_login) if self.last_login else "Never"


class Profile(TimeStampedUUIDModel):

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    bio = models.TextField(
        verbose_name=_("About me"), default="", blank=True, null=True
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"),
        default="profiles/default_profile.png",
        upload_to="profiles/",
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20,
    )
    country = CountryField(
        verbose_name=_("Country"), default="CMR", blank=False, null=False
    )
    city = models.CharField(
        verbose_name=_("City"),
        max_length=180,
        default="Bamenda",
        blank=False,
        null=False,
    )
    address = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        default="Address",
        verbose_name=_("Address"),
    )
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=30, default="+237660181440"
    )

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        indexes = [
            models.Index(fields=["phone_number"]),
        ]

    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        """
        Override save method to alter the behavior if needed.
        """
        # Call the parent save method
        super().save(*args, **kwargs)


class DataDeletionRequest(models.Model):
    """
    Google PlayStore Requirements
    This is need if the api is to be used with an app that will be hosted on the Play Store and AppStore.
    https://support.google.com/googleplay/android-developer/answer/104713?hl=en
    """

    REQUEST_TYPES = (
        ("account", "Account Deletion"),
        ("data", "Data Deletion Only"),
    )

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("completed", "Completed"),
        ("rejected", "Rejected"),
    )

    # User info
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="deletion_requests",
        null=True,
        blank=True,
    )
    email = models.EmailField()
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)

    # Verification
    verification_token = models.UUIDField(default=uuid.uuid4, editable=False)

    # Status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    # What to delete (for data deletion)
    delete_profile = models.BooleanField(default=False)
    delete_appointments = models.BooleanField(default=False)
    delete_services = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    processed_at = models.DateTimeField(null=True, blank=True)

    # Notes
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.email} - {self.get_request_type_display()} - {self.status}"

    class Meta:
        ordering = ["-created_at"]
