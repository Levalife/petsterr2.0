# -*- coding: utf-8 -*-
import inspect

import os
from django.core.management import BaseCommand
from django.utils.translation import ugettext_lazy as _


from countries.CountriesHandler import CountriesHandler


class Command(BaseCommand):
    handler = CountriesHandler()

    def handle(self, *args, **options):
        self.fill_countries()

    def fill_countries(self):
        with open(os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), 'list_of_countries'), 'r') as f:
            for row in f.readlines():
                row_list = row.split(',')
                name = row_list[0].replace(" ", "_").replace("'", "").lower()
                print(name)
                plain_data = dict(code=row_list[-1], title=name)
                self.handler.create(plain_data)

