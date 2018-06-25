# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.views.generic.base import View


class BaseView(View):

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass

    @staticmethod
    def make_form_error_message(form):
        errors = []
        for k, v in form.errors.items():
            errors.append('{}: {}'.format(k, v))
        return errors