from django.db import models
from django.contrib.auth.models import AbstractUser
AUTH_USER_MODEL = 'users.CustomUser'
AUTH_USER_MODEL = 'users.CustomUser'


# Create your models here.
class CustomUser(AbstractUser):
    pass
