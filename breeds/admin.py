from django.contrib import admin

from breeds.models import Breed

class BreedAdmin(admin.ModelAdmin):
    #fields = ['title', 'type']
    list_display = ('title', 'type')
    list_filter = ['type']
    search_fields = ['title']

admin.site.register(Breed, BreedAdmin)