# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

# -*- coding: utf-8 -*-
import inspect

import os
from django.core.management import BaseCommand
from django.utils.translation import ugettext_lazy as _

from breeds.BreedsHandler import BreedsHandler
from clubs.ClubsAssociationsHandler import ClubsAssociationsHandler
from clubs.CountryClubsHandler import CountryClubsHandler
from countries.CountriesHandler import CountriesHandler


class Command(BaseCommand):
    handler = BreedsHandler()

    def handle(self, *args, **options):
        self.fill_dogs_fci_breeds()

    def fill_dogs_fci_breeds(self, *args, **kwargs):
        with open(os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), 'dogs_breeds_list'), 'r') as f:
            for row in f.readlines():
                title = row.replace('\n', '')
                plain_data = dict(title=title, type="dogs", slug=title)
                self.handler.create(plain_data)
