# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _


# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from animals.AnimalsHandler import AnimalsHandler
from breeds.BreedsHandler import BreedsHandler
from kennels.KennelsHandler import KennelsHandler


class EditAnimalForm(forms.Form):
    handler = AnimalsHandler()
    kennels_handler = KennelsHandler()
    breeds_handler = BreedsHandler()

    id = forms.IntegerField(required=False)
    home_name = forms.CharField(required=False)
    full_name = forms.CharField(required=False)
    birthday = forms.CharField(required=False)
    deathday = forms.CharField(required=False, label=_(u'Date of death'))
    kennel_of_birth_slug = forms.CharField(required=False, widget=forms.HiddenInput)
    kennel_of_birth_title = forms.CharField(required=False
                                      # , widget=forms.Select
                                      )
    kennel_live_slug = forms.CharField(required=False, widget=forms.HiddenInput)
    kennel_live_title = forms.CharField(required=False,
                                  # widget=forms.Select
                                  )
    mother = forms.CharField(required=False
                             # , widget=forms.Select
                             )
    mother_slug = forms.CharField(required=False, widget=forms.HiddenInput)
    father = forms.CharField(required=False
                             # , widget=forms.Select
                             )
    father_slug = forms.CharField(required=False, widget=forms.HiddenInput)

    breed = forms.CharField(required=False, widget=forms.Select)
    color = forms.CharField(required=False)
    height = forms.CharField(required=False)
    pedigree = forms.URLField(required=False)
    registry = forms.CharField(required=False, label=_(u'Registry №'))
    entitlements = forms.CharField(required=False)
    gender = forms.ChoiceField(required=False, choices=handler.model_instance.GENDER_CHOICES, widget=forms.Select)
    achievements = forms.CharField(required=False)
    elbow_ed = forms.CharField(required=False)
    hip_hd = forms.CharField(required=False)
    tattoo = forms.CharField(required=False)
    dna_data = forms.CharField(required=False, label=_(u'DNA data'))
    microchip = forms.CharField(required=False)
    photo = forms.IntegerField(required=False)
    about = forms.CharField(required=False, widget=forms.Textarea)
    slug = forms.CharField(required=False, label=_(u'Page address'))
    is_owner = forms.BooleanField(required=False, label=_(u'I am owner'))
    type = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        type = kwargs.pop('type', None)
        super(EditAnimalForm, self).__init__(*args, **kwargs)
        kennels = [('', '')]
        params = dict(type=type)
        for kennel in self.kennels_handler.get_all_by_params(params, order_by='title'):
            kennels.append((kennel.slug, kennel.title))
        females = [('', '')]
        params = dict(gender=self.handler.model_instance.GENDER_FEMALE)
        for animal in self.handler.get_all_by_params(params, order_by='full_name'):
            females.append((animal.slug, animal.full_name if animal.full_name else animal.home_name))

        males = [('', '')]
        params = dict(gender=self.handler.model_instance.GENDER_MALE)
        for animal in self.handler.get_all_by_params(params=params, order_by='full_name'):
            males.append((animal.slug, animal.full_name if animal.full_name else animal.home_name))

        breeds = [('', '')]
        breeds.extend(list(self.breeds_handler.get_breeds_choices_by_type(type)))
        self.fields['kennel_of_birth_title'].widget.choices = kennels
        self.fields['kennel_live_title'].widget.choices = kennels
        self.fields['mother'].widget.choices = females
        self.fields['father'].widget.choices = males
        self.fields['breed'].widget.choices = breeds
        self.fields['pedigree'].widget.attrs['placeholder'] = _(u'link to pedigree')
        self.fields['mother'].widget.attrs['class'] = 'select-input-field'
        self.fields['mother'].widget.attrs['data-gender'] = 'female'
        self.fields['mother'].widget.attrs['data-type'] = 'animal'
        self.fields['mother'].widget.attrs['data-animal-type'] = type
        self.fields['mother'].widget.attrs['autocomplete'] = 'off'
        self.fields['father'].widget.attrs['class'] = 'select-input-field'
        self.fields['father'].widget.attrs['data-gender'] = 'male'
        self.fields['father'].widget.attrs['data-type'] = 'animal'
        self.fields['father'].widget.attrs['data-animal-type'] = type
        self.fields['father'].widget.attrs['autocomplete'] = 'off'
        # self.fields['kennel_live'].widget.attrs['class'] = 'select-input-field'
        # self.fields['kennel_live'].widget.attrs['data-type'] = 'kennel'
        # self.fields['kennel_live'].widget.attrs['data-animal-type'] = type
        # self.fields['kennel_live'].widget.attrs['autocomplete'] = 'off'
        # self.fields['kennel_of_birth'].widget.attrs['class'] = 'select-input-field'
        # self.fields['kennel_of_birth'].widget.attrs['data-type'] = 'kennel'
        # self.fields['kennel_of_birth'].widget.attrs['data-animal-type'] = type
        # self.fields['kennel_of_birth'].widget.attrs['autocomplete'] = 'off'

    def clean_slug(self):

        cleaned_data = super(EditAnimalForm, self).clean()
        slug = cleaned_data.get('slug')
        slug = slug.replace(' ', '_')

        params = dict(slug=slug)
        animals = self.handler.get_all_by_params(params=params, order_by='created_at')
        if animals and animals[0].id != cleaned_data.get('id'):
            raise ValueError(_(u'This page address is already in use. Try another one'))
        return slug
