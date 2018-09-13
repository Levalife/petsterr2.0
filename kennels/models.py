from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
# from geoposition.fields import GeopositionField
# from django.contrib.gis.db import models as geo_models

from base.models import BaseModel

from rest_framework.reverse import reverse as api_reverse


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
    # contacts = models.ForeignKey(Contact, blank=True, null=True)
    # coordinates = geo_models.PointField(blank=True, null=True)
    # position = GeopositionField(blank=True, null=True)
    country = ForeignKey('countries.Country', blank=True, null=True, on_delete=models.SET_NULL)
    timezone = models.CharField(blank=True, null=True, max_length=255)
    skype = models.CharField(blank=True, null=True, max_length=255)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    site = models.URLField(blank=True, null=True)
    # menu_color = models.CharField(max_length=64, blank=True, null=True, default="rgba(234, 99, 54, 0.2)")
    # link_color = models.CharField(max_length=64, blank=True, null=True, default="rgba(234, 99, 54, 1)")
    # text_color = models.CharField(max_length=64, blank=True, null=True, default="#5d6369")


    class Meta:
        db_table = 'kennels'

    # def save(self, *args, **kwargs):
    #     if self.position and not self.coordinates:
    #         self.coordinates = 'POINT(%s %s)' % (self.position.longitude, self.position.latitude)
    #     return super(Kennel, self).save(*args, **kwargs)

    def __str__(self):
        return u'Title [%s] | Owner [%s] | ID [%s]' % (self.title, self.owner, self.id)

    def get_api_url(self, request=None):
        return api_reverse('kennels:kennel_rud', kwargs={'slug': self.slug}, request=request)