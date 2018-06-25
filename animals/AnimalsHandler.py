# -*- coding: utf-8 -*-
import datetime

import random
from django.utils.translation import ugettext_lazy as _

from animals.models import BaseAnimal
from base.BaseHandler import BaseHandler
from breeds.BreedsHandler import BreedsHandler
from kennels.KennelsHandler import KennelsHandler


class AnimalsHandler(BaseHandler):
    model_instance = BaseAnimal
    kennels_handler = KennelsHandler()
    breeds_handler = BreedsHandler()

    def create_from_kennel(self, data, user):
        kennel_live = self.kennels_handler.get_by_slug(data.get('kennel_live'))
        data['kennel_live'] = kennel_live
        data['is_owner'] = True
        data['owner'] = user
        data['slug'] = self.make_slug(data.get('full_name'))
        animal = self.model_instance(**data)
        animal.save()
        return animal

    def get_by_slug(self, slug):
        return self.model_instance.objects.filter(slug=slug, is_deleted=False).order_by('-created_at').first()

    def get_all_by_params(self, params, order_by='-created_at'):
        # params['is_deleted'] = False
        return self.model_instance.objects.filter(**params, is_deleted=False).order_by(order_by)

    def get_all_by_params_json(self, params, order_by='-created_at'):
        if params.get('kennel_live', None):
            params['kennel_live'] = self.kennels_handler.get_by_slug(params.get('kennel_live'))
        if params.get('kennel_of_birth', None):
            params['kennel_of_birth'] = self.kennels_handler.get_by_slug(params.get('kennel_of_birth'))
        animals = self.get_all_by_params(params, order_by)
        return [self.humanize_animal(animal) for animal in animals]

    def humanize_animal(self, animal):
        animal_data = dict()
        animal_data['id'] = animal.id
        animal_data['full_name'] = animal.full_name
        animal_data['home_name'] = animal.home_name
        animal_data['type'] = animal.humanize_type()
        animal_data['gender'] = animal.humanize_gender()
        if animal.birthday:
            animal_data['birthday'] = animal.birthday.strftime("%d.%m.%Y")
        if animal.deathday:
            animal_data['deathday'] = animal.deathday.strftime("%d.%m.%Y")
        if animal.mother:
            animal_data['mother_slug'] = animal.mother.slug
            animal_data['mother'] = animal.mother.full_name

        if animal.father:
            animal_data['father_slug'] = animal.father.slug
            animal_data['father'] = animal.father.full_name

        if animal.breed:
            animal_data['breed'] = animal.breed.title

        if animal.kennel_of_birth:
            animal_data['kennel_of_birth_slug'] = animal.kennel_of_birth.slug
            animal_data['kennel_of_birth_title'] = animal.kennel_of_birth.title

        if animal.kennel_live:
            animal_data['kennel_live_slug'] = animal.kennel_live.slug
            animal_data['kennel_live_title'] = animal.kennel_live.title

        animal_data['color'] = animal.color
        animal_data['height'] = animal.height
        animal_data['registry'] = animal.registry
        animal_data['pedigree'] = animal.pedigree
        animal_data['entitlements'] = animal.entitlements
        animal_data['achievements'] = animal.achievements
        animal_data['elbow_ed'] = animal.elbow_ed
        animal_data['hip_hd'] = animal.hip_hd
        animal_data['tattoo'] = animal.tattoo
        animal_data['dna_data'] = animal.dna_data
        animal_data['microchip'] = animal.microchip
        animal_data['about'] = animal.about
        animal_data['slug'] = animal.slug
        animal_data['is_owner'] = animal.is_owner
        if animal.photo:
            animal_data['photo'] = animal.photo.url

        return animal_data

    def edit_animal(self, animal, data, user):
        for key, value in data.items():
            if value is not None:
                if key == 'birthday' or key == 'deathday':
                    if value != '':
                        animal.__dict__[key] = datetime.datetime.strptime(value, '%d.%m.%Y')
                elif key == 'mother_slug' or key == 'father_slug':
                    # TODO: check if works Foreign Key update
                    item = self.get_by_slug(value)
                    animal.__dict__[key] = item

                elif key == 'breed':
                    item = self.breeds_handler.get_by_slug(value)
                    animal.breed = item

                elif key == 'is_owner':
                    animal.__dict__[key] = value
                    animal.__dict__['owner'] = user

                elif key == 'kennel_of_birth_slug' or key == 'kennel_live_slug':
                    kennel = self.kennels_handler.get_by_slug(value)
                    animal.__dict__[key] = kennel

                else:
                    animal.__dict__[key] = value

        animal.save()
        return animal

    def make_slug(self, full_name):
        slug = full_name.replace(' ', '_')

        while True:
            animal = self.get_by_slug(slug)
            if animal:
                slug += str(random.randint(0, 10000))
            else:
                return slug

    def dump_animals(self, kennel_data, kennel):
        animals = self.get_all_by_params(dict(kennel_live=kennel,
                                              deathday=None,
                                              gender=self.model_instance.GENDER_MALE, is_deleted=False))
        kennel_data['male'] = self.dump_items(animals)

        animals = self.get_all_by_params(dict(kennel_live=kennel,
                                              deathday=None,
                                              gender=self.model_instance.GENDER_FEMALE, is_deleted=False))
        kennel_data['female'] = self.dump_items(animals)

        animals = self.get_all_by_params(dict(kennel_of_birth=kennel))
        kennel_data['offsprings'] = self.dump_items(animals)

        breeds = []
        animals = kennel_data['male'] + kennel_data['female']
        for animal in animals:
            if animal.get('breed') not in animals and animal.get('breed'):
                breeds.append(animal.get('breed'))
        kennel_data['breeds'] = ', '.join(breeds)

        return kennel_data

    def dump_items(self, animals):
        return [self.humanize_animal(animal) for animal in animals]
