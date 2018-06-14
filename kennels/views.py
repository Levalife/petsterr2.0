from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View

from kennels.KennelsHandler import KennelsHandler
from kennels.forms.CreateKennelForm import CreateKennelForm


class KennelView(View):
    handler = KennelsHandler()

    def get(self, request, *args, **kwargs):
        kennel = self.handler.get_by_slug(kwargs.get('slug'))
        if kennel:
            context = {'kennel': kennel}
            return render(request, 'kennels/kennel.html', context)
        else:
            raise Http404('Kennel does not exist')

    def post(self, request, *args, **kwargs):
        pass

    def delete(self, request):
        pass


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
