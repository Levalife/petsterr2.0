# -*- coding: utf-8 -*-
from django.urls import path
from django.utils.translation import ugettext_lazy as _

from news.views import NewsView

app_name = 'news'

urlpatterns = [
    path('news/', NewsView.as_view(), name='news_page')
]






