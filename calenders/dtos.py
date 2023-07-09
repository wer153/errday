from datetime import date
from enum import Enum

from ninja import Schema


class Emoji(Enum):
    pass


class PostListOut(Schema):
    id: str
    thumbnail_image: str
    postDate: date
    emoji: Emoji


class PostDetailOut(Schema):
    id: str
    image: str
    postDate: date
    emoji: Emoji
