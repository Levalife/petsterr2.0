# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User

from base.BaseHandler import BaseHandler
from users.UserProfilesHandler import UserProfilesHandler


class UsersHandler(BaseHandler):
    model_instance = User
    profile_handler = UserProfilesHandler()

    def get_user_by_email(self, email):
        return self.model_instance.objects.get(email=email)

    def create_user(self, data):
        # data consist of email and password
        user = User.objects.create_user(**data)
        profile = self.profile_handler.create_profile(user)
        return user

    def update(self, data):
        # data consist of any of User model fields
        #TODO check data
        user = self.get_by_id(data.get(id))
        for key, value in data:
            user.__dict__[key] = value
        user.save()
        return user

    def change_password(self, request,data):
        # data consost of user id and password
        #TODO check data
        user = self.get_by_id(data.get('id'))
        user.set_password(data.get('password'))
        user.save()
        update_session_auth_hash(request, user)
        return user

    def login_user(self, request, data):
        # data consist of username and password
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
        else:
            # No backend authenticated the credentials
            pass

    def logout_user(self, request):
        logout(request)

