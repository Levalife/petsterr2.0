from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.base import View

from kennels.KennelsHandler import KennelsHandler


class IndexView(View):
    template_name = 'web/index.html'
    context_object_name = 'items_list'
    kennels_handler = KennelsHandler()

    def get(self, request, *args, **kwargs):
        registered_user = False
        if request.user.is_authenticated:
            registered_user = True
        context = dict(registered_user=registered_user)

        return render(request, 'web/index.html', context=context)