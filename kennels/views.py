from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View

from animals.AnimalsHandler import AnimalsHandler
from animals.forms.CreateAnimalForm import CreateAnimalForm
from animals.forms.EditAnimalForm import EditAnimalForm
from kennels.KennelsHandler import KennelsHandler
from kennels.forms.EditKennelForm import EditKennelForm
from kennels.forms.CreateKennelForm import CreateKennelForm
from news.forms.CreateNewsForm import CreateNewsForm


class KennelView(View):
    handler = KennelsHandler()
    animals_handler = AnimalsHandler()
    form_class = EditKennelForm

    def get(self, request, *args, **kwargs):
        kennel = self.handler.get_by_slug(kwargs.get('slug'))
        if kennel:
            temporary_form = CreateAnimalForm
            from animals.AnimalsHandler import AnimalsHandler
            animals_handler = AnimalsHandler()
            animal = animals_handler.get_by_slug('Dog_Test_1_Male')
            temporary_form_2 = EditAnimalForm(animals_handler.humanize_animal(animal), type='dogs')
            news_form = CreateNewsForm
            context = {'kennel': kennel, 'animal_form': temporary_form, 'aform': temporary_form_2,
                       'news_form': news_form,
                       'form': self.form_class(self.handler.dump(kennel), kennel_id=kennel.id)}
            return render(request, 'kennels/kennel.html', context)
        else:
            raise Http404('Kennel does not exist')

    def post(self, request, *args, **kwargs):
        kennel = self.handler.get_by_slug(kwargs.get('slug'))
        form = self.form_class(request.POST, kennel_id=kennel.id)
        if form.is_valid():
            kennel = self.handler.update_kennel(kennel, form.cleaned_data)
            kennel_data = self.handler.dump(kennel)
            kennel_data = self.animals_handler.dump_animals(kennel_data, kennel)
            return JsonResponse(dict(result=True, kennel=kennel_data))
        return JsonResponse(dict(result=False, form=form))

    def delete(self, request, *args, **kwargs):
        slug = kwargs['slug']
        try:
            self.handler.delete(slug)
            return JsonResponse(dict(result=True))
        except Exception as e:
            return JsonResponse(dict(result=False, error_message=e))



class KennelsView(View):
    handler = KennelsHandler()
    form_class = CreateKennelForm

    def get(self, request, *args, **kwargs):
        kennels_list = self.handler.get_all()
        context = {'kennels_list': kennels_list, 'form': self.form_class}
        return render(request, 'kennels/kennels.html', context)


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            kennel = self.handler.create(request.user, form.cleaned_data)
            return HttpResponseRedirect(reverse('kennels:kennel_page', args=(kennel.slug,)))
        kennels_list = self.handler.get_all()
        context = {'kennels_list': kennels_list, 'form': form}
        return render(request, 'kennels/kennels.html', context)
