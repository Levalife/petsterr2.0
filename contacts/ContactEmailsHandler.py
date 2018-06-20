# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from base.BaseHandler import BaseHandler
from contacts.models import ContactEmail


class ContactEmailsHandler(BaseHandler):
    model_instance = ContactEmail

    def get_all_by_contact(self, contact, order_by='created_at'):
        return self.model_instance.objects.filter(contact=contact, is_deleted=False).order_by(order_by)

    def get_by_contact_email(self, data):
        return self.model_instance.objects.get(**data, is_deleted=False)

    def delete(self, id):
        phone = self.get_by_id(id)
        phone.is_deleted = True
        phone.save()
