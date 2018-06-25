# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django import  forms

class CreateLitterForm(forms.Form):
    litter = forms.CharField(required=True)
    kennel = forms.CharField(required=False)