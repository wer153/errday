import uuid

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_date = models.DateField(unique=True)
    image = models.ImageField()
    thumbnail = models.ImageField(blank=True, null=True)
    emoji = models.CharField(blank=True, max_length=10)
    user = models.ForeignKey(to=User, related_name='posts', on_delete=models.PROTECT)
