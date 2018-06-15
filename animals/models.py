from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.db import models

from base.models import BaseModel
from kennels.models import Kennel


class BaseAnimal(BaseModel):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'

    GENDER_CHOICES = (
        (GENDER_MALE, 'male'),
        (GENDER_FEMALE, 'female'),
    )

    # ANIMAL_CHOICES = (
    #     ('dogs', 'dogs'),
    #     ('cats', 'cats'),
    # )

    type = models.CharField(max_length=100, choices=Kennel.TYPE_CHOICES, null=True, blank=True)
    full_name = models.CharField(max_length=256, blank=True, null=True)
    home_name = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    deathday = models.DateField(blank=True, null=True)
    kennel_of_birth = models.ForeignKey('kennels.Kennel', null=True, blank=True, related_name='kennel_birth',
                                        on_delete=models.SET_NULL)
    kennel_live = models.ForeignKey('kennels.Kennel', null=True, blank=True, related_name='kennel_live',
                                        on_delete=models.SET_NULL)
    owner = models.ForeignKey(User, blank=True, null=True,
                                        on_delete=models.CASCADE)
    mother = models.ForeignKey('self', null=True, blank=True, related_name='mother_dog',
                                        on_delete=models.SET_NULL)
    father = models.ForeignKey('self', null=True, blank=True, related_name='father_dog',
                                        on_delete=models.SET_NULL)
    breed = models.ForeignKey('breeds.Breed', null=True, blank=True,
                                        on_delete=models.SET_NULL)
    color = models.CharField(max_length=50, null=True, blank=True)
    height = models.CharField(max_length=50, blank=True, null=True)
    registry = models.CharField(max_length=50, null=True, blank=True)
    pedigree = models.URLField(null=True, blank=True)

    entitlements = models.CharField(max_length=2048, null=True, blank=True)

    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True, blank=True)

    achievements = models.CharField(max_length=2048, null=True, blank=True)

    elbow_ed = models.CharField(max_length=2048, null=True, blank=True)
    hip_hd = models.CharField(max_length=2048, null=True, blank=True)
    tattoo = models.CharField(max_length=50, null=True, blank=True)

    dna_data = models.CharField(max_length=2048, null=True, blank=True)

    microchip = models.CharField(max_length=50, null=True, blank=True)

    photo = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)

    about = models.CharField(max_length=10000, blank=True, null=True)
    slug = models.CharField(max_length=256, blank=True, null=True)
    is_owner = models.BooleanField(default=False)

    class Meta:
        db_table = 'kennel_animal'
        verbose_name = _('Animal')
        verbose_name_plural = _('Animals')

    def humanize_type(self):
        return dict(Kennel.TYPE_CHOICES).get(self.type)

    def humanize_gender(self):
        return dict(self.GENDER_CHOICES).get(self.gender)

    def __str__(self):
        return u'%s' % (self.full_name)