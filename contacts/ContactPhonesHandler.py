# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from base.BaseHandler import BaseHandler
from contacts.models import ContactPhone


class ContactPhonesHandler(BaseHandler):
    model_instance = ContactPhone

    def get_all_by_contact(self, contact, order_by='created_at'):
        return self.model_instance.objects.filter(contact=contact, is_deleted=False).order_by(order_by)

    def delete(self, id):
        phone = self.get_by_id(id)
        phone.is_deleted = True
        phone.save()