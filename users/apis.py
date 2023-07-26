from django.contrib.auth import get_user_model, login
from django.shortcuts import get_object_or_404
from ninja import Router

from users.services import signup


User = get_user_model()

router = Router()


@router.post('/signup')
def user_signup(request, email: str, nick_name: str):
    user = signup(email=email, nick_name='', image=None)
    login(request=request, user=user)
    return email


@router.get('/signin')
def user_signin(request, email: str):
    user = get_object_or_404(
        User,
        email=email,
    )
    login(request=request, user=user)
    return None
