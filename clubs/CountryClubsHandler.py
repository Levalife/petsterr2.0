# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from base.BaseHandler import BaseHandler
from clubs.models import CountryClub


class CountryClubsHandler(BaseHandler):
    model_instance = CountryClub

    def create(self, data):
        club = self.model_instance(**data)
        club.save()
        return club

    def get_all_by_type(self, type):
        return self.model_instance.objects.filter(type=type, is_deleted=False).order_by('title')

    def get_club_choices_by_type(self, type):
        clubs = self.get_all_by_type(type)
        return [(club.id, club.title) for club in clubs]

