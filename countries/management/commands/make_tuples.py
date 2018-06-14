# -*- coding: utf-8 -*-
import inspect

import os
from django.utils.translation import ugettext_lazy as _


def make_countries_tuples():
    tuple_string = ''
    with open(os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), 'list_of_countries'), 'r') as f:
        for row in f.readlines():
            title = row.split(',')[0]
            tuple_string += '("' + title.replace(" ", "_").replace('"','').lower() + '", _(u"' + title.replace('"','') + '")),\n'
    print(tuple_string)

make_countries_tuples()
