import uuid

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Calender(models.Model):
    MAX_COUNT = 1

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(to=User, related_name='calenders', on_delete=models.PROTECT)
    joined_date = models.DateField()


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_date = models.DateField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    thumbnail = models.ImageField(upload_to='thumbnails/%Y/%m/%d/')
    emoji = models.CharField(blank=True, max_length=10)
    user = models.ForeignKey(to=User, related_name='posts', on_delete=models.PROTECT)
    calender = models.ForeignKey(
        to=Calender,
        related_name='posts',
        on_delete=models.PROTECT,
        unique_for_date='post_date',
    )
