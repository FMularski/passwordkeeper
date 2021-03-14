from django.db import models
from authmanager.models import ExtendedUser


class Account(models.Model):
    title = models.CharField(max_length=32, null=False)
    login = models.CharField(max_length=64, null=False)
    email = models.EmailField(max_length=64, null=False)
    password = models.CharField(max_length=256, null=False)
    owner = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE, null=True)