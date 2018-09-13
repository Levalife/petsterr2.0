# -*- coding: utf-8 -*-
import datetime

import jwt
from django.conf import settings
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.authtoken.models import Token

from base.BaseHandler import BaseHandler
from emails.EmailsHandler import EmailsHandler
from users.api.errors import AuthenticationError
from users.UserProfilesHandler import UserProfilesHandler


class UsersHandler(BaseHandler):
    model_instance = User
    profile_handler = UserProfilesHandler()
    emails_handler = EmailsHandler()

    def get_user_by_email(self, email):
        return self.model_instance.objects.get(email=email)

    def get_by_params(self, params):
        return self.model_instance.objects.filter(**params)

    def get_by_username_or_email(self, username=None, email=None):
        return self.model_instance.objects.filter(Q(username=username) | Q(email=email)).distinct()

    def create_user(self, data):
        # data consist of email and password
        user = self.model_instance.objects.create_user(**data)
        return user

    def update(self, data):
        # data consist of any of User model fields
        # TODO check data
        user = self.get_by_id(data.get(id))
        for key, value in data:
            user.__dict__[key] = value
        user.save()
        return user

    def change_password(self, request, data):
        # data consist of user id and password
        # TODO check data
        user = self.get_by_id(data.get('id'))
        user.set_password(data.get('password'))
        user.save()
        update_session_auth_hash(request, user)
        return user

    def set_new_password(self, request, new_password):
        user = self.get_by_id(request.user.id)
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)
        return user

    def reset_password(self, token, new_password):
        token_data = jwt.decode(token.encode('utf-8'), settings.SECRET_KEY, algorithm='HS256')
        user = self.get_by_id(token_data.get("id"))
        if user.profile.reset_token == token:
            user.set_password(new_password)
            user.profile.reset_token = None
            user.save()
            return user
        raise AuthenticationError("This link has already been used.")

    def login_user(self, request, data):
        # data consist of username and password
        user = authenticate(username=data.get('email'), password=data.get('password'))
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)  # with sessions
            token, _ = Token.objects.get_or_create(user=user)  # with token
            return token
        else:
            # No backend authenticated the credentials
            raise AuthenticationError("Invalid username or password.")

    def logout_user(self, request):
        logout(request)

    def send_reset_password_email(self, user, request):
        token = jwt.encode({'id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
                           settings.SECRET_KEY, algorithm='HS256')

        self.update_reset_token(user, token)
        link = 'http://{}/reset_password/{}'.format(request.META['HTTP_HOST'], token.decode("utf-8"))
        email_data = {
            "subject": 'Reset Password',
            "content": 'To reset password follow this link <a href={0}>{0}</a>'.format(link),
            "email_to": user.email
        }
        email = self.emails_handler.create_email(email_data)
        self.emails_handler.send_email(email)

    def update_reset_token(self, user, token):
        user_profile = self.profile_handler.get_by_user(user)
        user_profile.reset_token = token.decode('utf-8')
        user_profile.save()
