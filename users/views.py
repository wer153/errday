from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSignUpSerializer
from users.services import signup


class UserSignUpView(APIView):
    permission_classes = AllowAny,

    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        signup(**serializer.validated_data)
        return Response(serializer.data)
