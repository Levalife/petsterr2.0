# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _


class GetAnimalsForm(forms.Form):
    kennel_live = forms.CharField(required=True)
    gender = forms.CharField(required=False)
    type = forms.CharField(required=False)
