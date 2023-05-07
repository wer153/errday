from rest_framework.fields import EmailField, CharField, ImageField
from rest_framework.serializers import Serializer


class UserSignUpSerializer(Serializer):
    email = EmailField()
    image = ImageField(required=False, default=None)
    nick_name = CharField(required=False, default=None)
