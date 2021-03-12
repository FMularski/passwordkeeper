from django.db import models
from django.contrib.auth.models import AbstractUser


class ExtendedUser(AbstractUser):
    pin = models.CharField(max_length=255, null=False, default='0000')

