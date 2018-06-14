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