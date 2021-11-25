from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    country = models.ForeignKey('location.Country', on_delete=models.SET_NULL, null=True, blank=True)
