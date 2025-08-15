from django.contrib.auth.models import AbstractUser
from django.db import models

class UserAccount(AbstractUser):
    email = models.EmailField(unique=True, max_length=11)
    phone_number = models.CharField(max_length=11, unique=True)
# Create your models here.
