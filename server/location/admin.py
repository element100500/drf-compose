from django.contrib import admin

from .models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'code')
