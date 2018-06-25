# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _


class GetLitterForm(forms.Form):
    slug = forms.CharField(required=True)