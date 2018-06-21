from django.contrib import admin

from base.models import BaseModel
from .models import Kennel

class KennelAdmin(admin.ModelAdmin):
    #fields = ['title', 'type']
    list_display = ('id', 'title', 'type')
    list_filter = ['type']
    search_fields = ['title']

admin.site.register(Kennel, KennelAdmin)
