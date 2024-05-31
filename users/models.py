from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # 追加のフィールドをここに定義することもできます
    pass


