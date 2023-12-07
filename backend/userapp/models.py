from django.db import models
from django.contrib.auth.models import AbstractUser


# создать класс юзера и унаследовать от abstract user
class MyUser(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=10, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    is_seller = models.BooleanField(default=False)
    fio = models.CharField(max_length=255, null=True, blank=True)
    is_confirmed = models.BooleanField(default=False)
    confirm_token = models.CharField(max_length=255, null=True, blank=True)
