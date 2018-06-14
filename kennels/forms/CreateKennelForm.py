# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from kennels.KennelsHandler import KennelsHandler


class CreateKennelForm(forms.Form):
    title = forms.CharField(required=True, label=_(u'Title'))
    type = forms.CharField(required=True, widget=forms.Select, initial="dogs")
#
    def __init__(self, *args, **kwargs):
        super(CreateKennelForm, self).__init__(*args, **kwargs)
        kennel_handler = KennelsHandler()
        self.fields['title'].widget.attrs['placeholder'] = _(u'title')
        self.fields['type'].widget.choices = kennel_handler.model_instance.TYPE_CHOICES
