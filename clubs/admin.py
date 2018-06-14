from django.contrib import admin

from clubs.models import ClubsAssociation, CountryClub


class ClubsAssociationAdmin(admin.ModelAdmin):
    #fields = ['title', 'type']
    list_display = ('title', 'type')
    list_filter = ['type']
    search_fields = ['title']


class CountryClubAdmin(admin.ModelAdmin):
    #fields = ['title', 'type']
    list_display = ('title', 'type')
    list_filter = ['type']
    search_fields = ['title']

admin.site.register(ClubsAssociation, ClubsAssociationAdmin)
admin.site.register(CountryClub, CountryClubAdmin)