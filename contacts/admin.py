from django.contrib import admin

from contacts.models import Contact, ContactPhone, ContactEmail

admin.site.register(Contact)
admin.site.register(ContactEmail)
admin.site.register(ContactPhone)