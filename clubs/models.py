from django.utils.translation import ugettext_lazy as _

from django.db import models

from base.models import BaseModel
from kennels.models import Kennel


class ClubsAssociation(BaseModel):
     title = models.CharField(max_length=255, blank=True, null=True)
     abbreviation = models.CharField(max_length=255, blank=True, null=True)
     type = models.CharField(max_length=64, blank=True, null=True, choices=Kennel.TYPE_CHOICES,
                             default=Kennel.TYPE_DOGS)

     class Meta:
         db_table = 'clubs_associations'
         verbose_name = _('Clubs Association')
         verbose_name_plural = _('Clubs Associations')


     def __str__(self):
         return u'{}, {}'.format(self.id, self.title)


class CountryClub(BaseModel):
    title = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey('countries.Country', null=True, blank=True, related_name='country_of_origin', on_delete=models.SET_NULL)
    url = models.URLField(null=True, blank=True)
    # fci = models.BooleanField(default=False)
    club_association = models.ForeignKey('clubs.ClubsAssociation', null=True, blank=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=64, blank=True, null=True, choices=Kennel.TYPE_CHOICES, default=Kennel.TYPE_DOGS)

    class Meta:
        db_table = 'country_clubs'
        verbose_name = _('Country Club')
        verbose_name_plural = _('Country Clubs')

    def __str__(self):
        return u'{}, {}, {}, {}, {}'.format(self.id, self.title, self.type, self.country,
                                            self.club_association.abbreviation if self.club_association else '')
