# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from base.BaseHandler import BaseHandler
from contacts.ContactEmailsHandler import ContactEmailsHandler
from contacts.ContactPhonesHandler import ContactPhonesHandler
from contacts.models import Contact


class ContactsHandler(BaseHandler):
    model_instance = Contact
    emails_handler = ContactEmailsHandler()
    phones_handler = ContactPhonesHandler()

    def create(self, data):
        # data = {source_id, type}
        contact = self.model_instance(**data)
        contact.save()
        return contact

    def get_by_type_source_id(self, data):
        return self.model_instance.objects.filter(**data, is_deleted=False).order_by('-created_at').first()

    def get_full_contact(self, data):
        contact = self.get_by_type_source_id(data)
        emails = self.emails_handler.get_all_by_contact(contact)
        phones = self.phones_handler.get_all_by_contact(contact)
        contact.emails = emails
        contact.phones = phones
        return contact

    def dump_get_contact_by_type_source(self, type, source_id):
        contact = self.get_by_type_source_id(dict(type=type, source_id=source_id))
        emails = self.emails_handler.get_all_by_contact(contact)
        phones = self.phones_handler.get_all_by_contact(contact)
        contact_data = dict(emails=[], phones=[])
        for email in emails:
            contact_data['emails'].append(email.email)

        for phone_contact in phones:
            contact_data['phones'].append(dict(name=phone_contact.name, phone=self.dump_phone_number(phone_contact.phone)))
        return contact_data

    def dump_phone_number(self, phone_number):
        return '+%s%s' % (phone_number.country_code, phone_number.national_number)