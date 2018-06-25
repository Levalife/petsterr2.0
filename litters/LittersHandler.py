# -*- coding: utf-8 -*-
import random
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from animals.AnimalsHandler import AnimalsHandler
from base.BaseHandler import BaseHandler
from breeds.BreedsHandler import BreedsHandler
from kennels.KennelsHandler import KennelsHandler
from litters.models import Litter
from news.NewsHandler import NewsHandler


class LittersHandler(BaseHandler):
    model_instance = Litter
    kennels_handler = KennelsHandler()
    news_handler = NewsHandler()
    animals_handler = AnimalsHandler()
    breeds_handler = BreedsHandler()

    def create_litter(self, data):
        kennel = self.kennels_handler.get_by_slug(data.get('kennel'))
        litter = self.model_instance(litter=data.get('litter'), kennel=kennel,
                                     slug=self.make_slug(data.get('litter', is_deleted=False), kennel.title))
        litter.save()
        return litter

    def get_by_slug(self, slug):
        return self.model_instance.objects.filter(slug=slug, is_deleted=False).order_by('-created_at').first()

    def get_all_by_kennel_slug(self, kennel_slug, order_by='-created_at'):
        kennel = self.kennels_handler.get_by_slug(kennel_slug)
        return self.model_instance.objects.filter(kennel=kennel, is_deleted=False).order_by(order_by)

    def get_all_by_params(self, params, order_by='-created_at'):
        return self.model_instance.objects.filter(**params).order_by(order_by)

    def get_all_by_kennel(self, kennel, order_by='-created_at'):
        return self.model_instance.objects.filter(kennel=kennel, is_deleted=False).order_by(order_by)

    def delete(self, slug):
        litter = self.get_by_slug(slug)
        try:
            litter.is_deleted = True
            litter.save()
        except self.model_instance.DoesNotExist:
            pass

    def make_slug(self, title, kennel_title):
        slug = '{}_{}'.format(kennel_title.replace(' ', '_'), title).lower()
        while True:
            litter = self.get_by_slug(slug)
            if not litter:
                return slug
            slug = '{}_{}'.format(slug, random.randint(1, 1000))

    def update(self, litter, data):
        if data.get('type') == 'photo':
            if data.get('photo', None):
                pass
                # image_object = self.image_handler.get_by_id(data['photo'])
                # item_data.photo = image_object.image
            else:
                litter.photo = None
        else:
            for key, value in data.items():
                if value is not None and value != '':
                    if key == 'dam_slug' or key == 'sir_slug':
                        # TODO: check if works Foreign Key update

                        value = self.animals_handler.get_by_slug(value)
                    elif key == 'breed':
                        value = self.breeds_handler.get_by_slug(value)
                    elif key == 'kennel':
                        value = self.kennels_handler.get_by_slug(value)

                    setattr(litter, key, value)
        litter.save()
        return litter

    def dump(self, item):

        plain_data = dict()
        plain_data['id'] = item.id
        plain_data['litter'] = item.litter
        plain_data['slug'] = item.slug
        plain_data['photo'] = item.photo.url if item.photo else None
        plain_data['is_photo'] = True if item.photo else False

        plain_data['pedigree'] = item.pedigree
        plain_data['birthday'] = item.birthday
        plain_data['males'] = item.males
        plain_data['females'] = item.females
        plain_data['about'] = item.about

        if item.kennel:
            plain_data['kennel'] = item.kennel.slug
            plain_data['kennel_title'] = item.kennel.title
            plain_data['kennel_url'] = reverse('kennels:kennel_page',
                                               kwargs={'slug': item.kennel.slug})

        if item.breed:
            plain_data['breed'] = item.breed.title

        if item.dam:
            plain_data['dam'] = self.animals_handler.humanize_animal(item.dam)

        if item.sir:
            plain_data['sire'] = self.animals_handler.humanize_animal(item.sir)
        plain_data['news'] = self.news_handler.get_dump_news_by_params(dict(type='litter', source_id=item.id))
        # plain_data['album'] = self.gallery_handler.get_dump_album('litter', item.id) if \
        #     self.gallery_handler.get_album('litter', item.id) else dict(images=[], images_preview=[])
        # plain_data['album'].get('images').insert(0, dict(id='', url=plain_data['photo']))
        return plain_data
