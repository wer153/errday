from calenders.dtos import PostListOut
from calenders.models import Post


def get_post_list(request):
    posts = Post.objects.all()
    return [
        PostListOut()
        for post in posts
    ]
    return