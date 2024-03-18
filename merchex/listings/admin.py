from django.contrib import admin

from .models import Band, Listing


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')


admin.site.register(Band, BandAdmin)


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'band')


admin.site.register(Listing, ListingAdmin)