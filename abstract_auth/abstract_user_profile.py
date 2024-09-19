from django.conf import settings
from django.db import models


class AbstractAuthProfile(models.Model):
    class Meta:
        abstract = True

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="auth_profile"
    )
    display_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    photo_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uid = models.CharField(max_length=255, blank=True, null=True)
