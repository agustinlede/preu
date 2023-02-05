from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255, verbose_name="email address")
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.email