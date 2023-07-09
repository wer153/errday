from datetime import date

from django.shortcuts import get_object_or_404

from calenders.dtos import PostListOut, PostDetailOut, PostDetailIn
from calenders.models import Post


def get_post_list(request, start_date: date | None = None, end_date: date | None = None):
    date_filter = {}
    if start_date:
        date_filter |= {'post_date__gte': start_date}
    if end_date:
        date_filter |= {'post_date__lt': end_date}
    posts = Post.objects.filter(
        user=request.user,
        **date_filter,
    )
    return [
        PostListOut(
            id=post.id,
            thumbnail=post.thumbnail,
            post_date=post.post_date,
            emoji=post.emoji,
        )
        for post in posts
    ]


def get_post_detail(request, post_date: date):
    post: Post = get_object_or_404(Post, post_date=post_date, user=request.user)
    return PostDetailOut(
        id=post.id,
        image=post.image,
        post_date=post.post_date,
        emoji=post.emoji,
    )


def put_post_detail(request, post_date: date, payload: PostDetailIn):
    post, created = Post.objects.update_or_create(
        post_date=post_date,
        user=request.user,
        defaults=payload.dict(),
    )
    status_code = 201 if created else 200
    return status_code, PostDetailOut(
        id=post.id,
        image=post.image,
        post_date=post.post_date,
        emoji=post.emoji,
    )
