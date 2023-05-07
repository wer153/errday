from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from users.models import User as AuthUser, Profile
from users.operations import generate_nick_name

User: AuthUser = get_user_model()


def signup(
    email: str,
    image: str,
    nick_name: str,
) -> AuthUser:
    if not nick_name:
        nick_name = generate_nick_name()
    with atomic():
        user = User.objects.create(email=email, image=image)
        Profile.objects.create(user=user, nick_name=nick_name)
    return user
