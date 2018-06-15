from django.http import JsonResponse
from django.views.generic.base import View

from animals.AnimalsHandler import AnimalsHandler
from animals.forms.CreateAnimalForm import CreateAnimalForm
from animals.forms.EditAnimalForm import EditAnimalForm
from animals.forms.GetAnimalsForm import GetAnimalsForm


class AnimalsView(View):
    handler = AnimalsHandler()
    form_class = CreateAnimalForm
    get_form = GetAnimalsForm

    def get(self, request, *args, **kwargs):
        form = self.get_form(request.GET)
        if form.is_valid():
            return JsonResponse(dict(result=True, animals=self.handler.get_all_by_params_json(form.cleaned_data)))
        return JsonResponse(dict(result=False, error_message='Not enough params for performing request'))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            animal = self.handler.create_from_kennel(form.cleaned_data, request.user)
            return JsonResponse(dict(result=True, animal=self.handler.humanize_animal(animal)))
        return JsonResponse(dict(result=False, form=form))


class AnimalView(View):
    handler = AnimalsHandler()
    form_class = EditAnimalForm

    def get(self, request, *args, **kwargs):
        animal = self.handler.get_by_slug(kwargs.get('slug'))
        if animal:
            return JsonResponse(dict(result=True, animals=self.handler.humanize_animal(animal)))
        return JsonResponse(dict(result=False, error_message='Page not found'))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        animal = self.handler.get_by_slug(kwargs.get('slug'))
        if form.is_valid():
            animal = self.handler.edit_animal(animal, form.cleaned_data, request.user)
            return JsonResponse(dict(result=True, animal=self.handler.humanize_animal(animal)))
        return JsonResponse(dict(result=False, form=form))