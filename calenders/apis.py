from datetime import date

from django.utils import timezone

from calenders.dtos import PostListOut
from calenders.models import Post


def get_post_list(request, start_date: date | None = None, end_date: date | None = None):
    date_filter = {}
    if start_date:
        date_filter |= {'post_datetime__date__gte': start_date}
    if end_date:
        date_filter |= {'post_datetime__date__lt': end_date}
    posts = Post.objects.filter(
        user=request.user,
        **date_filter,
    )
    return [
        PostListOut(
            id=post.id,
            thumbnail=post.thumbnail,
            post_date=timezone.localdate(post.post_datetime),
            emoji=post.emoji,
        )
        for post in posts
    ]
