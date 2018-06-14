# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from base.BaseHandler import BaseHandler
from breeds.models import Breed


class BreedsHandler(BaseHandler):
    model_instance = Breed

    def create(self, data):
        breed = self.model_instance(**data)
        breed.save()
        return breed