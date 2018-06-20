# -*- coding: utf-8 -*-
import random
import requests
from django.urls import reverse
from easy_thumbnails.files import get_thumbnailer

from clubs.CountryClubsHandler import CountryClubsHandler
from countries.CountriesHandler import CountriesHandler
from kennels.models import Kennel
from petsterr.settings import KENNEL_COVER


class KennelsHandler:
    model_instance = Kennel
    clubs_hanlder = CountryClubsHandler()
    countries_handler = CountriesHandler()

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

    def update_kennel(self, kennel, data):
        if data.get('type') == 'cover':
            if data.get('cover', None):
                # img_io = StringIO.StringIO()
                from PIL import Image
                img = Image.open(data['cover'])
                # image_object = self.image_factory.get_by_id(data['cover'])
                # img = Image.open(image_object.image)

                # x = data['x']
                # y = data['y']
                # w = data['w']
                # h = data['h']

                # img = img.crop((x, y, x + w, y + h))
                # img.save(img_io, format='JPEG', quality=100)
                # img_content = ContentFile(img_io.getvalue(), '%s' % data['cover'])
                kennel.cover = img
            else:
                kennel.cover = None
        else:
            for key, value in data.items():
                if value is not None:
                    if key == 'country_club':
                        # TODO: check __dict__[key] update
                        item = self.clubs_hanlder.get_by_id(value)
                        kennel.country_club = item

                    # elif key == 'address':
                        # TODO: get country from position
                        # kennel.coordinates = 'POINT(%s %s)' % (data.get('longitude'), data.get('latitude'))
                        # kennel.position = "%s,%s" % (data.get('latitude'), data.get('longitude'))
                        # kennel.address = data.get('address', None)
                        # country_title = ''
                        # country_code = ''
                        # city_title = ''
                        # response = requests.get(
                        #     "http://maps.googleapis.com/maps/api/geocode/json?latlng={0},{1}&sensor=true".format(
                        #         data.get('latitude'), data.get('longitude')))
                        # for result in response.json().get('results')[0].get('address_components'):
                        #     if 'country' in result.get('types'):
                        #         country_title = result.get('long_name')
                        #         country_code = result.get('short_name')
                        #     if 'locality' in result.get('types'):
                        #         city_title = result.get('long_name')
                        # timezone
                        # country = self.countries_handler.get_by_code(country_code)
                        # kennel.country = country
                    else:
                        kennel.__dict__[key] = value

                    kennel.save()
            return kennel

    def dump(self, kennel):
        plain_data = dict()
        plain_data['id'] = kennel.id
        plain_data['title'] = kennel.title
        plain_data['slug'] = kennel.slug
        plain_data['about'] = kennel.about
        plain_data['cover'] = kennel.cover.url if kennel.cover else KENNEL_COVER
        options = {'size':(800, 800), 'quality': 99}
        plain_data['mini_cover'] = get_thumbnailer(kennel.cover).get_thumbnail(options).url if kennel.cover else \
            KENNEL_COVER


        # plain_data['litters'] = self.litter_handler.get_dump_litters_by_kennel(kennel, user)

        # plain_data['news'] = self.get_kennel_news(kennel)
        plain_data['facebook'] = kennel.facebook
        plain_data['twitter'] = kennel.twitter
        plain_data['skype'] = kennel.skype
        plain_data['site'] = kennel.site
        plain_data['address'] = kennel.address
        plain_data['kennel_url'] = reverse('kennels:kennel_page', kwargs={'slug': kennel.slug})
        # if kennel.coordinates:
        #     plain_data['longitude'] = float(kennel.coordinates.get_x())
        #     plain_data['latitude'] = float(kennel.coordinates.get_y())
        if kennel.country_club:
            plain_data['country_club'] = kennel.country_club.id
            plain_data['country_club_title'] = kennel.country_club.title
            plain_data['country_club_url'] = kennel.country_club.url
            if kennel.country_club.club_association:
                plain_data['club_as'] = kennel.country_club.club_association.title

        # plain_data['contacts'] = self.contact_handler.dump_get_contact_by_type_source(
        #     self.contact_handler.factory.mapping.model_class.TYPE_KENNEL, kennel.id)
        return plain_data

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