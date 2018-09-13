# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.api.errors import AuthenticationError
from users.UsersHandler import UsersHandler
from users.api.serializers import UserCreateSerializer, UserLoginSerializer, UserChangePasswordSerializer, \
    UserValidateTokenSerializer, UserForgotPasswordSerializer, UserResetPasswordSerializer

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    user_handler = UsersHandler()
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            token = self.user_handler.login_user(request, request.data)
            return Response(dict(token=token.key, email=request.user.email, username=request.user.username),
                            status=status.HTTP_201_CREATED)
        return Response(self.user_handler.parse_serializer_errors(serializer.errors),
                        status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    handler = UsersHandler()

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            try:
                token = self.handler.login_user(request, serializer.data)
                return Response(dict(token=token.key, email=request.user.email, username=request.user.username),
                                status=status.HTTP_200_OK)
            except AuthenticationError:
                return Response(["Login failed"], status=status.HTTP_401_UNAUTHORIZED)
        return Response(self.handler.parse_serializer_errors(serializer.errors),
                        status=status.HTTP_400_BAD_REQUEST)


class UserForgotPasswordAPIView(APIView):
    handler = UsersHandler()
    permission_classes = [AllowAny]
    serializer_class = UserForgotPasswordSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            try:
                user = self.handler.get_by_params(dict(email=serializer.data.get('email'))).first()
                if user:
                    self.handler.send_reset_password_email(user, request)
                    return Response(dict(result=True), status=status.HTTP_200_OK)
                return Response(["There is no user with such email."],
                                status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response([str(e)],
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(self.handler.parse_serializer_errors(serializer.errors),
                        status=status.HTTP_400_BAD_REQUEST)


class UserValidateTokenAPIView(APIView):
    handler = UsersHandler()
    permission_classes = [AllowAny]
    serializer_class = UserValidateTokenSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            return Response(status=status.HTTP_200_OK)


class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserChangePasswordSerializer

    handler = UsersHandler()

    def get(self, request, *args, **kwargs):
        self.handler.logout_user(request)
        return Response(dict(result=True), status=status.HTTP_200_OK)


class UserResetPasswordAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserResetPasswordSerializer

    handler = UsersHandler()

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            try:
                user = self.handler.reset_password(serializer.data.get("token"), serializer.data.get('new_password'))
                return Response(dict(email=user.email, username=user.username), status=status.HTTP_200_OK)
            except AuthenticationError as error:
                return Response([str(error)],
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(self.handler.parse_serializer_errors(serializer.errors),
                        status=status.HTTP_400_BAD_REQUEST)