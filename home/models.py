from django.db import models

class Account(models.Model):
    title = models.CharField(max_length=32, null=False)
    login = models.CharField(max_length=64, null=False)
    email = models.EmailField(max_length=64, null=False)
    password = models.CharField(max_length=256, null=False)
