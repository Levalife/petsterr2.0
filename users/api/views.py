# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from kennels.api.errors import AuthenticationError
from users.UsersHandler import UsersHandler
from users.api.serializers import UserCreateSerializer, UserLoginSerializer, UserChangePasswordSerializer

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    user_handler = UsersHandler()

    serializer_class = UserCreateSerializer

    def get_queryset(self):
        return self.user_handler.get_all()


class UserLoginAPIView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    hander = UsersHandler()

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            try:
                token = self.hander.login_user(request, data)
                return Response(dict(token=token.key), status=status.HTTP_200_OK)
            except AuthenticationError:
                return Response({"non_field_errors": ["Login failed"]}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = UserChangePasswordSerializer

    hander = UsersHandler()

    def post(self, request, *args, **kwargs):
        data = request.data
        print(request)
        serializer = self.serializer_class(data=data, context=dict(request=request))
        if serializer.is_valid(raise_exception=True):
            self.hander.set_new_password(request, serializer.data.get('password1'))
            return Response(dict(result=True), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

