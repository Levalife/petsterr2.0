from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import BaseModel


class Litter(BaseModel):

    litter = models.CharField(max_length=256, blank=True, null=True)
    birthday = models.CharField(max_length=100, blank=True, null=True)
    kennel = models.ForeignKey('kennels.Kennel', null=True, blank=True, related_name='kennel_of_birth', on_delete=models.CASCADE)
    dam = models.ForeignKey('animals.BaseAnimal', null=True, blank=True, related_name='dam_animal', on_delete=models.SET_NULL)
    sir = models.ForeignKey('animals.BaseAnimal', null=True, blank=True, related_name='sir_animal', on_delete=models.SET_NULL)
    breed = models.ForeignKey('breeds.Breed', null=True, blank=True, on_delete=models.SET_NULL)

    pedigree = models.URLField(max_length=2048, null=True, blank=True)
    males = models.IntegerField(null=True, blank=True)
    females = models.IntegerField(null=True, blank=True)

    photo = models.ImageField(upload_to='images/photo/%Y/%m/%d', blank=True, null=True)

    about = models.CharField(max_length=10000, blank=True, null=True)
    slug = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'kennel_litter'
        verbose_name = _('Litter')
        verbose_name_plural = _('Litters')

    def __unicode__(self):
        return u'%s, %s' % (self.kennel.title, self.litter)