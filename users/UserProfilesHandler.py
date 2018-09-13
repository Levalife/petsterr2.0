# -*- coding: utf-8 -*-
from users.models import UserProfile


class UserProfilesHandler:
    model_instance= UserProfile

    def create_profile(self, user):
        profile = self.model_instance(user=user)
        profile.save()
        return profile

    def get_by_user(self, user):
        return self.model_instance.objects.get(user=user)