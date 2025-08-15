from django.contrib.auth.models import User
from django.db import models
from django.db import models

from account.models import UserAccount


# Create your models here.
class Security(UserAccount):
    is_security_guard = models.BooleanField(default=False)