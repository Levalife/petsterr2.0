from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from base.models import BaseModel


class Contact(BaseModel):
    TYPE_KENNEL = 'kennel'
    TYPE_USER = 'user'
    TYPE_PLACE = 'place'

    TYPE_CHOICES = (
        (TYPE_KENNEL, TYPE_KENNEL),
        (TYPE_USER, TYPE_USER),
        (TYPE_PLACE, TYPE_PLACE),
    )

    source_id = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True, blank=True)

    def __unicode__(self):
        return u'id {}, type {}, source id {}'.format(self.id, self.type, self.source_id)

    class Meta:
        db_table = 'contacts'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class ContactEmail(BaseModel):
    contact = models.ForeignKey('Contact', blank=True, null=True, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)

    def __unicode__(self):
        return u'id {}, contact {}, email {}'.format(self.id, self.contact, self.email)

    class Meta:
        db_table = 'contact_emails'
        verbose_name = 'Contact email'
        verbose_name_plural = 'Contact emails'


class ContactPhone(BaseModel):
    contact = models.ForeignKey('Contact', blank=True, null=True, on_delete=models.CASCADE)
    phone = PhoneNumberField()
    name = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return u'id {}, contact {}, name {}'.format(self.id, self.contact, self.name)

    class Meta:
        db_table = 'contact_phones'
        verbose_name = 'Contact phone'
        verbose_name_plural = 'Contact phones'