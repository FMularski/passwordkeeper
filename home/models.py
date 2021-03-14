from django.db import models
from authmanager.models import ExtendedUser


class Account(models.Model):
    title = models.CharField(max_length=32)
    login = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField(max_length=64, null=True, blank=True)
    password = models.CharField(max_length=256)
    owner = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE, null=True)