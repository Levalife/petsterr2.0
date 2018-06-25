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

    def get_breeds_choices_by_type(self, type):
        breeds = self.model_instance.objects.filter(type=type, is_deleted=False).order_by('title')
        return ((breed.slug, breed.humanize_title()) for breed in breeds)

    def get_breeds_by_params(self, params, order_by='title'):
        breeds = self.model_instance.objects.filter(is_deleted=False, **params).order_by(order_by)
        return breeds

    def get_by_slug(self, slug):
        return self.model_instance.objects.get(slug=slug)