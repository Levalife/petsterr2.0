# -*- coding: utf-8 -*-
import urllib.request as urllib2

from bs4 import BeautifulSoup
from django.utils.translation import ugettext_lazy as _

# -*- coding: utf-8 -*-
import inspect

import os
from django.core.management import BaseCommand
from django.utils.translation import ugettext_lazy as _


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.create_clubs_list()

    def create_clubs_list(self):
        with open(os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), 'dogs_breeds_list'), 'w') as f:
            page = urllib2.urlopen('https://en.wikipedia.org/wiki/List_of_dog_breeds_recognized_by_the_FCI').read()
            soup = BeautifulSoup(page)
            soup.prettify()
            for tr in soup.findAll('tr'):
                td_list = tr.findAll("td")
                if td_list and len(td_list)>=3:
                    breed = td_list[3].text.split('\n')[0]
                    f.write('{}\n'.format(breed.replace(' ', '_').replace(',', ')').lower()))
                    # f.write('("{0}",_("{1}")),\n'.format(breed.replace(' ', '_').replace(',', ')').lower(), breed))
