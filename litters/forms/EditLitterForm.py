# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from breeds.BreedsHandler import BreedsHandler
from kennels.KennelsHandler import KennelsHandler
from litters.LittersHandler import LittersHandler


class EditLitterForm(forms.Form):
    handler = LittersHandler()
    kennels_handler = KennelsHandler()
    breeds_handler = BreedsHandler()

    id = forms.IntegerField(required=False)
    litter = forms.CharField(required=False)
    birthday = forms.CharField(required=False)
    kennel = forms.CharField(required=False, widget=forms.Select)
    dam = forms.CharField(required=False
                             # , widget=forms.Select
                             )

    dam_slug = forms.CharField(required=False, widget=forms.HiddenInput)
    sire = forms.CharField(required=False
                             # , widget=forms.Select
                             )
    sire_slug = forms.CharField(required=False, widget=forms.HiddenInput)
    breed = forms.CharField(required=False, widget=forms.Select)
    pedigree = forms.URLField(required=False)
    males = forms.IntegerField(required=False)
    females = forms.IntegerField(required=False)
    photo = forms.IntegerField(required=False)
    about = forms.CharField(required=False, widget=forms.Textarea)
    slug = forms.CharField(required=False, label=_(u'Page address'))
    type = forms.CharField(required=False)


    def __init__(self, *args, **kwargs):
        type = kwargs.pop('type', None)


        super(EditLitterForm, self).__init__(*args, **kwargs)
        kennels = [('', '')]
        for kennel in self.kennels_handler.get_all_by_params(dict(type=type), order_by="title"):
            kennels.append((kennel.slug, kennel.title))

        breeds = [('', '')]
        breeds.extend(list(self.breeds_handler.get_breeds_choices_by_type(type)))
        self.fields['kennel'].widget.choices = kennels
        self.fields['breed'].widget.choices = breeds

    def clean_slug(self):
        cleaned_data = super(EditLitterForm, self).clean()
        slug = cleaned_data.get('slug')
        slug = slug.replace(' ', '_')

        params = dict(slug=slug)
        litters = self.handler.get_all_by_params(params)
        if litters and litters[0].id != cleaned_data.get('id'):
            raise ValueError(_(u'This page address is already in use. Try another one'))
        return slug