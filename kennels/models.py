from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import BaseModel


class Kennel(BaseModel):
    TYPE_DOGS = 'dogs'
    TYPE_CATS = 'cats'

    TYPE_CHOICES = (
        (TYPE_DOGS, _(u'dogs')),
        (TYPE_CATS, _(u'cats')),
    )

    title = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True, choices=TYPE_CHOICES, default='dogs')
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    reg_number = models.CharField(max_length=50, null=True, blank=True)
    about = models.CharField(max_length=10000, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    cover = models.ImageField(upload_to='kennels/covers/%Y/%m/%d', blank=True, null=True)
    slug = models.CharField(max_length=256, blank=True, null=True)

    country_club = models.ForeignKey('clubs.CountryClub', null=True, blank=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=1024, blank=True, null=True)
    skype = models.CharField(blank=True, null=True, max_length=255)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    site = models.URLField(blank=True, null=True)

    def __str__(self):
        return 'Kennel: {}'.format(self.title)
