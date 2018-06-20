# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from clubs.CountryClubsHandler import CountryClubsHandler
from kennels.KennelsHandler import KennelsHandler


class EditKennelForm(forms.Form):
    kennels_handler = KennelsHandler()
    country_club_handler = CountryClubsHandler()


    about = forms.CharField(max_length=11000, required=False)
    title = forms.CharField(max_length=512, required=False, label=_('Kennel title'))
    slug = forms.CharField(max_length=512, required=False, label=_('Kennel page address'))
    address = forms.CharField(max_length=512, required=False)
    latitude = forms.FloatField(widget=forms.HiddenInput, required=False)
    longitude = forms.FloatField(widget=forms.HiddenInput, required=False)
    reg_number = forms.CharField(max_length=256, required=False)
    email_0 = forms.EmailField(max_length=128, required=False, label=_(u'Email'))
    skype = forms.CharField(max_length=128, required=False)
    twitter = forms.URLField(required=False)
    facebook = forms.URLField(required=False)
    site = forms.URLField(required=False)
    name_0 = forms.CharField(required=False, label=_(u'Name'))
    phone_0 = forms.RegexField(required=False, regex=r'^\+?1?\d{9,15}$',
                               error_messages={'format': (
                                   u"Phone number must be entered in the format '+99999999999'. Up to 15 digits allowed.")},
                               label=_(u'Phone'))
    country_club = forms.CharField(required=False, widget=forms.Select)

    def __init__(self, *args, **kwargs):
        phones_number = kwargs.pop('phones_number', None)
        emails_number = kwargs.pop('emails_number', None)
        self.kennel_id = kwargs.pop('kennel_id', None)
        super(EditKennelForm, self).__init__(*args, **kwargs)
        self.fields['about'].widget.attrs['placeholder'] = _(u'Tell something about your kennel')
        self.fields['phone_0'].widget.attrs['class'] = 'phone-item-block'
        self.fields['email_0'].widget.attrs['class'] = 'email-item-block'
        self.fields['phone_0'].widget.attrs['placeholder'] = '+99999999999'
        if phones_number:
            for number in range(1, int(phones_number)):
                self.fields['name_%s' % number] = forms.CharField(required=False, label=_(u'Name'))
                self.fields['phone_%s' % number] = forms.RegexField(required=False, regex=r'^\+?1?\d{9,15}$',
                               error_message=_(
                                   u"Phone number must be entered in the format '+99999999999'. Up to 15 digits allowed."),
                               label=_(u'Phone'))
                self.fields['phone_%s' % number].widget.attrs['class'] = 'phone-item-block'
        if emails_number:
            for number in range(1, int(emails_number)):
                self.fields['email_%s' % number] = forms.EmailField(max_length=128, required=False, label=_(u'Email'))
                self.fields['email_%s' % number].widget.attrs['class'] = 'email-item-block'
        if self.kennel_id:
            kennel = self.kennels_handler.get_by_id(int(self.kennel_id))
            self.fields['country_club'].widget.choices = [('','')] + self.country_club_handler.get_club_choices_by_type(kennel.type)

    def clean_slug(self):
        cleaned_data = super(EditKennelForm, self).clean()
        slug = cleaned_data.get('slug')
        slug = slug.replace(' ', '_')
        #
        kennels = self.kennels_handler.get_by_slug(slug)
        if kennels and kennels.id != int(self.kennel_id):
            raise ValueError(_(u'This page address is already in use. Try another one'))
        return slug