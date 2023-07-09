from datetime import date

from django.shortcuts import get_object_or_404
from ninja import Router

from calenders.dtos import PostListOut, PostDetailOut, PostDetailIn, Emoji
from calenders.models import Post


router = Router()

@router.get('/{calender_id}/posts')
def get_post_list(request, calender_id: str, start_date: date | None = None, end_date: date | None = None):
    date_filter = {}
    if start_date:
        date_filter |= {'post_date__gte': start_date}
    if end_date:
        date_filter |= {'post_date__lt': end_date}
    posts = Post.objects.filter(
        calender=calender_id,
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


@router.get('/{calender_id}/posts/{post_date}')
def get_post_detail(request, calender_id: str, post_date: date):
    post: Post = get_object_or_404(
        Post,
        post_date=post_date,
        user=request.user,
        calender=calender_id,
    )
    return PostDetailOut(
        id=post.id,
        image=post.image,
        post_date=post.post_date,
        emoji=post.emoji,
    )


@router.put('/{calender_id}/posts/{post_date}')
def put_post_detail(request, calender_id: str, post_date: date, payload: PostDetailIn):
    post, created = Post.objects.update_or_create(
        calender=calender_id,
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


@router.delete('/{calender_id}/posts/{post_date}')
def delete_post_detail(request, calender_id: str, post_date: date):
    Post.objects.filter(
        calender=calender_id,
        user=request.user,
        post_date=post_date,
    ).delete()
    return None
