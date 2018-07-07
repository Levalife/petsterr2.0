# -*- coding: utf-8 -*-
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
    email2 = serializers.EmailField(label=_('Confirm email'))

    class Meta:
        model = User
        fields = [
            # 'username',
            'password',
            'email',
            'email2'
        ]

        extra_kwargs = {"password":
                            {'write_only': True}}

    def validate(self, data):
        # email = data.get('email')
        # users_qs = self.user_handler.get_by_params(dict(email=email))
        # if users_qs.exists():
        #     raise ValidationError(_("This user has already been registered."))
        data['username'] = data['email']
        return data

    def validate_email(self, value):
        data = self.get_initial()
        email1 = value
        email2 = data.get("email2")
        if email1 != email2:
            raise ValidationError(_("Emails must match."))

        users_qs = self.user_handler.get_by_params(dict(email=email1))
        if users_qs.exists():
            raise ValidationError(_("This user has already been registered."))

        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value
        if email1 != email2:
            raise ValidationError(_("Emails must match."))
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

        extra_kwargs = {"password":
                            {'write_only': True}}

    def validate(self, data):
        user_obj = None
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

        # data["token"] = "SOME RANDOM TOKEN"

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
        print(user.check_password('{}'.format(value)))
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