# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _


class CreateAnimalForm(forms.Form):
    full_name = forms.CharField(required=True)
    kennel_live = forms.CharField(required=False)
    gender = forms.CharField(required=False)
    type = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(CreateAnimalForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['placeholder'] = _(u'Enter full name')