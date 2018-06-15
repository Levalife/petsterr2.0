# -*- coding: utf-8 -*-
import random

from kennels.models import Kennel


class KennelsHandler:
    model_instance = Kennel

    def get_all(self):
        return self.model_instance.objects.filter(is_deleted=False).order_by('title')

    def get_by_id(self, id):
        return self.model_instance.objects.get(id=id)

    def get_by_slug(self, slug):
        return self.model_instance.objects.filter(slug=slug).first()

    def get_all_by_params(self, params, order_by='-created_at'):
        params['is_deleted'] = False
        return self.model_instance.objects.filter(**params).order_by(order_by)

    def create(self, user, data):
        try:
            item = self.model_instance(owner=user, **data)
            item.slug = self.make_slug(data.get('title'))
            item.save()
            return item
        except Exception as e:
            print(e)

    def delete(self, slug):
        item = self.get_by_slug(slug)
        item.is_deleted = True
        item.save()

    def make_slug(self, title):
        slug = title.replace(' ', '_').lower()
        while True:
            kennel = self.get_by_slug(slug)
            if kennel:
                slug += str(random.randint(0, 10000))
            else:
                return slug