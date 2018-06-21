# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _


class CreateNewsForm(forms.Form):
    # id = forms.IntegerField(required=False)
    source_id = forms.IntegerField(required=False)
    type = forms.CharField(required=False)
    content = forms.CharField(required=False)