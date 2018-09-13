from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import BaseModel


class BaseNews(BaseModel):
    TYPE_KENNEL = 'kennel'
    TYPE_ANIMAL = 'animal'
    TYPE_LITTER = 'litter'

    TYPE_CHOICES = (
        (TYPE_KENNEL, 'kennel'),
        (TYPE_ANIMAL, 'animal'),
        (TYPE_LITTER, 'litter'),
    )

    source_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, null=True, blank=True)
    content = models.CharField(max_length=5120, blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'base_news'
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return '{}, {}, {}'.format(self.source_id, self.type, self.author)


class FavoriteItem(BaseModel):
    TYPE_KENNEL = 'kennel'
    TYPE_ANIMAL = 'animal'
    TYPE_LITTER = 'litter'

    TYPE_CHOICES = (
        (TYPE_KENNEL, 'kennel'),
        (TYPE_ANIMAL, 'animal'),
        (TYPE_LITTER, 'litter'),
    )

    source_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, null=True, blank=True)
    follower = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'favorite_item'
        verbose_name = _('Favorite Items')
        verbose_name_plural = _('Favorite Item')

    def __str__(self):
        return '{}, {}, {}'.format(self.source_id, self.type, self.follower)