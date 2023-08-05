from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    telegram = models.CharField(max_length=150, verbose_name='Telegram')
    REQUIRED_FIELDS = ["email", "telegram"]
