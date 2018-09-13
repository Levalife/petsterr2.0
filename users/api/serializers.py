# -*- coding: utf-8 -*-
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from users.UsersHandler import UsersHandler

User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    user_handler = UsersHandler()

    email = serializers.EmailField(label=_('Email address'))

    class Meta:
        model = User
        fields = [
            'password',
            'email',
        ]

        extra_kwargs = {"password":
                            {'write_only': True}}

    def validate(self, data):
        data['username'] = data['email']
        return data

    def validate_email(self, value):
        email1 = value

        users_qs = self.user_handler.get_by_params(dict(email=email1))
        if users_qs.exists():
            raise ValidationError(_("This user has already been registered."))

        return value

    def create(self, validated_data):
        self.user_handler.create_user(validated_data)
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(label=_('Email address'), required=False, allow_blank=True)

    user_handler = UsersHandler()

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'token'
        ]

        # extra_kwargs = {"password":
        #                     {'write_only': True}}

    def validate(self, data):
        email = data.get('email', None)
        username = data.get('username', None)
        password = data.get('password', None)
        if not username and not email:
            raise ValidationError(_("A username or email is required to login."))

        user = self.user_handler.get_by_username_or_email(username, email)
        user.exclude(email__isnull=True).exclude(email__iexact="")
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError(_("This username/email is not valid."))

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError(_("Incorrect credentials, please try again."))

        return data


class UserChangePasswordSerializer(ModelSerializer):
    user_handler = UsersHandler()

    old_password = serializers.CharField(label=_('Old password'))
    password1 = serializers.CharField(label=_('New password'))
    password2 = serializers.CharField(label=_('Confirm password'))

    class Meta:
        model = User
        fields = [
            'old_password',
            'password1',
            'password2',
        ]

        extra_kwargs = {
            "old_password": {'write_only': True},
            "password1": {'write_only': True},
            "password2": {'write_only': True},
                        }

    def validate_old_password(self, value):
        user = self.user_handler.get_by_id(self.context.get('request').user.id)
        if user.check_password('{}'.format(value)):
            return value
        raise ValidationError(_("Wrong password."))

    def validate_password1(self, value):
        data = self.get_initial()
        password1 = value
        password2 = data.get("password2")
        if password1 != password2:
            raise ValidationError(_("Passwords must match."))

        return value

    def validate_password2(self, value):
        data = self.get_initial()
        password1 = data.get("password1")
        password2 = value
        if password1 != password2:
            raise ValidationError(_("Passwords must match."))
        return value


class UserForgotPasswordSerializer(ModelSerializer):

    email = serializers.EmailField(label=_('Email address'))

    class Meta:
        model = User
        fields = [
            'email',
        ]


class UserValidateTokenSerializer(ModelSerializer):
    user_handler = UsersHandler()

    token = serializers.CharField()

    class Meta:
        model = User
        fields = [
            'token',
        ]

    def validate_token(self, value):
        try:
            token_data = jwt.decode(value, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise ValidationError("Signature has expired")
        except jwt.InvalidSignatureError:
            raise ValidationError("Invalid signature token")


class UserResetPasswordSerializer(serializers.Serializer):

    token = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    class Meta:
        fields = [
            "token",
            'new_password',
            'confirm_password',
        ]

    def validate_new_password(self, value):
        data = self.get_initial()
        new_password = value
        confirm_password = data.get("confirm_password")
        if new_password != confirm_password:
            raise ValidationError(_("Passwords must match."))

        return value

    def validate_confirm_password(self, value):
        data = self.get_initial()
        new_password = data.get("new_password")
        confirm_password = value
        if new_password != confirm_password:
            raise ValidationError(_("Passwords must match."))
        return value

    def validate_token(self, value):
        try:
            jwt.decode(value, settings.SECRET_KEY, algorithms=['HS256'])
            return value
        except jwt.ExpiredSignatureError:
            raise ValidationError("Signature has expired")
        except jwt.InvalidSignatureError:
            raise ValidationError("Invalid signature token")