from django.db import models

from base.models import BaseModel


class EmailTemplates(BaseModel):

    template = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=1000, null=True, blank=True)
    content = models.CharField(max_length=10000, null=True, blank=True)

    class Meta:
        db_table = 'email_templates'

    def __str__(self):
        return u'Subject [%s] | Template [%s] | ID [%s]' % (self.subject, self.template, self.id)


class Email(BaseModel):

    email_to = models.EmailField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=1000, null=True, blank=True)
    content = models.CharField(max_length=10000, null=True, blank=True)
    sent = models.BooleanField(default=False)

    class Meta:
        db_table = 'emails'

    def __str__(self):
        return u'Subject [%s] | Template [%s] | ID [%s]' % (self.subject, self.email_to, self.id)