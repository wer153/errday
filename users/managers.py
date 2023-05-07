from django.db import models
from django.contrib.auth.hashers import make_password


class UserManager(models.Manager):
    def create(self, email, password, date_of_birth=None, is_staff=False, is_superuser=False):
        self.normalize_email(email)
        return super().create(
            email=email,
            password=make_password(password),
            date_of_birth=date_of_birth,
            is_staff=is_staff,
            is_superuser=is_superuser,
        )

    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the address by lowercasing the domain part of the email
        address.
        """
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = '@'.join([email_name, domain_part.lower()])
        return email

    def get_by_natural_key(self, email):
        return self.get(email=email)
