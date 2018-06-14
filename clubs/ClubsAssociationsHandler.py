# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from base.BaseHandler import BaseHandler
from clubs.models import ClubsAssociation


class ClubsAssociationsHandler(BaseHandler):
    model_instance = ClubsAssociation

    def create(self, data):
        club_as = self.model_instance(**data)
        club_as.save()
        return club_as

    def get_by_abbreviation(self, abbreviation):
        return self.model_instance.objects.filter(abbreviation=abbreviation).order_by("created_at").first()