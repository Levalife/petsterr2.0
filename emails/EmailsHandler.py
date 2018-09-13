# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _

from base.BaseHandler import BaseHandler
from emails.models import Email


class EmailsHandler(BaseHandler):
    model_instance = Email

    def create_email(self, data):
        item = self.model_instance.objects.create(**data)
        item.save()
        return item

    @staticmethod
    def send_email(email):
        send_mail(
            email.subject,
            email.content,
            'info@petsterr.com',
            [email.email_to],
            fail_silently=False,
        )
