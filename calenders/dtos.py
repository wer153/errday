from datetime import date
from enum import Enum

from ninja import Schema


class Emoji(Enum):
    ANGRY: str = 'ANGRY'
    SICK: str = 'SICK'
    SAD: str = 'SAD
    LOADING: str = 'LOADING'
    HAPPY: str = 'HAPPY'
    PEACEFUL: str = 'PEACFUL'

class CalenderListOut(Schema):
    id: str


class CreateCalenderOut(Schema):
    id: str


class PostListOut(Schema):
    id: str
    thumbnail: str
    post_date: date
    emoji: str


class PostDetailOut(Schema):
    id: str
    image: str
    post_date: date
    emoji: str
