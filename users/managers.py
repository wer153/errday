from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create(self, email, password, date_of_birth=None, is_staff=False, is_superuser=False):
        self.normalize_email(email)
        return super().create(
            email=email,
            password=make_password(password),
            date_of_birth=date_of_birth,
            is_staff=is_staff,
            is_superuser=is_superuser,
        )
