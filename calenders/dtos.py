from datetime import date
from enum import Enum

from ninja import Schema


class Emoji(Enum):
    pass


class CalenderListOut(Schema):
    id: str


class CreateCalenderOut(Schema):
    id: str


class PostListOut(Schema):
    id: str
    thumbnail: str
    post_date: date
    emoji: Emoji


class PostDetailOut(Schema):
    id: str
    image: str
    post_date: date
    emoji: Emoji


class PostDetailIn(Schema):
    image: str
    emoji: Emoji
