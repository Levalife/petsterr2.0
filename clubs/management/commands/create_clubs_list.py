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
        with open(os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), 'clubs_list'), 'w') as f:
            page = urllib2.urlopen('https://en.wikipedia.org/wiki/List_of_kennel_clubs#cite_note-2').read()
            soup = BeautifulSoup(page)
            soup.prettify()
            for tr in soup.findAll('tr'):
                td_list = tr.findAll("td")
                if td_list:
                    country = td_list[0].text
                    title = str(td_list[1].text)
                    fci = td_list[2].text
                    wku = td_list[3].text
                    url = td_list[1].a.get('href') if td_list[1].a and 'http' in td_list[1].a else ''
                    f.write("{0},{1},{2},{3}\n".format(country, title, fci, wku, url))
