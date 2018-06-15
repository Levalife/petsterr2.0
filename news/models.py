from django.contrib.auth.models import User
from django.db import models

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
    body = models.CharField(max_length=5120, blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        db_table = 'base_news'
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return '{}, {}, {}'.format(self.source_id, self.type, self.author)