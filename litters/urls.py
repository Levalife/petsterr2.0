# -*- coding: utf-8 -*-
from django.urls import path
from django.utils.translation import ugettext_lazy as _

from litters.views import LittersView, LitterView

app_name = 'litters'

urlpatterns = [
    path('', LittersView.as_view(), name='litters_page'),
    path('<str:slug>/', LitterView.as_view(), name='litter_page'),
]