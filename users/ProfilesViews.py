# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View

from users.UserProfilesHandler import UserProfilesHandler
from users.UsersHandler import UsersHandler


class ProfilesView(View):
    handler = UsersHandler()
    profile_handler = UserProfilesHandler()

    def get(self, request, *arg, **kwargs):
        context = dict()
        return render(request, 'users/profile_page.html', context=context)
