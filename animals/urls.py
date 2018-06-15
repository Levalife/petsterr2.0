from django.urls import path

from animals.views import AnimalsView, AnimalView
from . import views

app_name = 'animals'

urlpatterns = [
    path('', AnimalsView.as_view(), name='animals_page'),
    path('<str:slug>/', AnimalView.as_view(), name='animal_page'),
]