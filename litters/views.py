from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import View

from base.BaseView import BaseView
from kennels.KennelsHandler import KennelsHandler
from litters.LittersHandler import LittersHandler
from litters.forms.CreateLitterForm import CreateLitterForm
from litters.forms.EditLitterForm import EditLitterForm
from litters.forms.GetLitterForm import GetLitterForm


class LittersView(View):
    handler = LittersHandler()
    form_class = CreateLitterForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            litter = self.handler.create_litter(form.cleaned_data)
            return JsonResponse(dict(result=True, litter=self.handler.dump(litter)))
        return JsonResponse(dict(result=False, form=form))

    def get(self, request, *args, **kwargs):
        # kennel slug
        litters = self.handler.get_all_by_kennel_slug(request.GET.get('slug'))
        paginator = Paginator(litters, 15)  # Show 15 contacts per page
        page = request.GET.get('page')
        litters_object = paginator.get_page(page)
        dump_litters = [self.handler.dump(litter) for litter in litters_object.object_list]
        return JsonResponse(dict(result=True, litters=dump_litters, page_number=litters_object.number,
                                 num_pages=litters_object.paginator.num_pages))


class LitterView(BaseView):
    handler = LittersHandler()
    edit_form_class = EditLitterForm
    get_form_class = GetLitterForm

    def post(self, request, *args, **kwargs):
        form = self.edit_form_class(request.POST)
        if form.is_valid():
            litter = self.handler.get_by_slug(kwargs.get('slug'))
            litter = self.handler.update(litter, form.cleaned_data)
            return JsonResponse(dict(result=True, litter=self.handler.dump(litter)))
        return JsonResponse(dict(result=False, form=form))

    def get(self, request, *args, **kwargs):
        litter = self.handler.get_by_slug(kwargs['slug'])
        return JsonResponse(dict(result=True, litter=self.handler.dump(litter)))

    def delete(self, request, *args, **kwargs):
        form = self.get_form_class(kwargs)
        if not form.is_valid():
            return JsonResponse(dict(result=False, form_errors=self.make_form_error_message(form)))
        self.handler.delete(form.cleaned_data.get('slug'))
        return JsonResponse(dict(result=True))
