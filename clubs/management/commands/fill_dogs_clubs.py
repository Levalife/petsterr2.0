# -*- coding: utf-8 -*-
import inspect

import os
from django.core.management import BaseCommand
from django.utils.translation import ugettext_lazy as _

from clubs.ClubsAssociationsHandler import ClubsAssociationsHandler
from clubs.CountryClubsHandler import CountryClubsHandler
from countries.CountriesHandler import CountriesHandler


class Command(BaseCommand):
    handler = CountryClubsHandler()
    clubas_handler = ClubsAssociationsHandler()
    countries_handler = CountriesHandler()

    def handle(self, *args, **options):
        self.fill_clubs_association()
        self.fill_country_clubs()

    def fill_clubs_association(self):
        plain_data = dict(title="Fédération Cynologique Internationale", abbreviation="FCI", type="dogs")
        self.clubas_handler.create(plain_data)
        plain_data = dict(title="World Kennel Union", abbreviation="WKU", type="dogs")
        self.clubas_handler.create(plain_data)

    def fill_country_clubs(self, *args, **kwargs):
        with open(os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), 'clubs_list'), 'r') as f:
            for row in f.readlines():
                row_list = row.rstrip().split(',')
                country = self.countries_handler.get_by_title(title=row_list[0].replace(' ', '_').lower())
                fci = self.clubas_handler.get_by_abbreviation('FCI')
                wku = self.clubas_handler.get_by_abbreviation('WKU')
                if row_list[2] == "Yes":
                    plain_data = dict(title=row_list[1], country=country, url=row_list[3] if len(row_list) > 3 else None,
                                      club_association=fci)
                elif row_list[3] == "Yes":
                    plain_data = dict(title=row_list[1], country=country,
                                      url=row_list[3] if len(row_list) > 3 else None,
                                      club_association=wku)
                else:
                    plain_data = dict(title=row_list[1], country=country,
                                      url=row_list[3] if len(row_list) > 3 else None)
                self.handler.create(plain_data)
