from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer


@api_view(["POST"])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=serializer.data["username"])
        user.set_password(serializer.data["password"])
        user.save()

        token = Token.objects.create(user=user)
        return Response(
            data={"token": token.key},
            status=status.HTTP_201_CREATED,
        )
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    if not "username" in request.data or not "password" in request.data:
        return Response(
            data={"error": _("Please enter both username and password.")},
            status=status.HTTP_400_BAD_REQUEST,
        )

    user = get_object_or_404(User, username=request.data["username"])

    if not user.check_password(request.data["password"]):
        return Response(
            data={"error": _("You have entered the wrong password.")},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    token, created = Token.objects.get_or_create(user=user)

    return Response(data={"token": token.key}, status=status.HTTP_200_OK)
