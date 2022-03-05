from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Site, SiteCheckResult, Proxy


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'user')
    autocomplete_fields = ('user',)


@admin.register(SiteCheckResult)
class SiteCheckResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'site', 'country', 'status', 'date_updated')


@admin.register(Proxy)
class ProxyAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'http_port', 'country', 'status', 'get_speed', 'date_updated')
    autocomplete_fields = ('user', 'country')

    def get_speed(self, proxy):
        return proxy.format_speed()
    get_speed.short_description = _('speed')
    get_speed.admin_order_field = 'speed'
