# -*- coding: utf-8 -*-
from users.models import UserProfile


class UserProfilesHandler:
    model_instance= UserProfile

    def create_profile(self, user):
        profile = self.model_instance(user=user)
        return profile