# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from base.BaseHandler import BaseHandler
from countries.models import Country


class CountriesHandler(BaseHandler):
    model_instance = Country

    def create(self, data):
        country = self.model_instance(**data)
        country.save()
        return country

    def get_by_title(self, title):
        return self.model_instance.objects.get(title=title)