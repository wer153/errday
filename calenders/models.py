import uuid

from django.db import models


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_datetime = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    thumbnail = models.ImageField(blank=True, null=True)
