from django.urls import path

from kennels.views import KennelView, KennelsView
from . import views

app_name = 'kennels'

urlpatterns = [
    path('', KennelsView.as_view(), name='kennels_page'),
    path('<str:slug>/', KennelView.as_view(), name='kennel_page'),
]