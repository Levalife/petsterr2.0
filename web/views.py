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
        if request.user.is_authenticated:
            context = dict(kennels_list=self.kennels_handler.get_all())
            return render(request, 'web/feed.html', context=context)
        return render(request, 'web/index.html')