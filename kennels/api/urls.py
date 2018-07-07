# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include

from kennels.api.views import KennelRUDView, KennelAPIView

app_name = 'kennels'
urlpatterns = [
    path('', KennelAPIView.as_view(), name='kennel_list'),
    path('<str:slug>/', KennelRUDView.as_view(), name='kennel_rud'),

]