from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.gis.geoip2 import GeoIP2

from core.models import ActivatableModel, TimestampedModel
from location.models import Country

User = get_user_model()


class Site(ActivatableModel, TimestampedModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('user'),
                             related_name='sites')
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = _('Site')
        verbose_name_plural = _('Sites')
        ordering = ('-date_created',)

    def __str__(self):
        return self.url


class SiteCheckResult(TimestampedModel):
    site = models.ForeignKey(to=Site, on_delete=models.CASCADE, verbose_name=_('site'), related_name='check_results')
    country = models.ForeignKey(to='location.Country', on_delete=models.CASCADE, verbose_name=_('country'))
    status = models.BooleanField(_('status'))
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)

    class Meta:
        verbose_name = _('Site check result')
        verbose_name_plural = _('Site check results')
        ordering = ('-date_created',)
        unique_together = ('site', 'country')


class Proxy(ActivatableModel, TimestampedModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('user'),
                             related_name='proxies')
    ip = models.GenericIPAddressField(_('ip'))
    http_port = models.PositiveIntegerField(_('http port'))
    https_port = models.PositiveIntegerField(_('https port'), blank=True, null=True)
    socks_port = models.PositiveIntegerField(_('socks port'), blank=True, null=True)
    username = models.CharField(_('username'), max_length=255, blank=True)
    password = models.CharField(_('password'), max_length=255, blank=True)
    status = models.CharField(_('status'), max_length=255, blank=True)
    speed = models.FloatField(_('speed'), null=True, blank=True)
    country = models.ForeignKey(to='location.Country', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name=_('country'), related_name='proxies')

    __original_ip = None

    class Meta:
        verbose_name = _('Proxy')
        verbose_name_plural = _('Proxies')
        unique_together = ('ip', 'http_port')
        ordering = ('-date_created',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_ip = self.ip

    def save(self, *args, **kwargs):
        if self.ip != self.__original_ip:
            self.update_country()

        super().save(*args, **kwargs)
        self.__original_ip = self.ip

    def __str__(self):
        result = self.host

        if self.username and self.password:
            result += f'{self.username}:{self.password}'

        return result

    def as_dict(self):
        return {
            'https': f'http://{self.username}:{self.password}@{self.ip}:{self.http_port}',
        }

    def update_country(self):
        g = GeoIP2()
        geo_data = g.country(self.ip)

        country, _ = Country.objects.get_or_create(code=geo_data['country_code'], defaults={
            'name': geo_data['country_name'],
        })
        self.country = country

    def format_speed(self):
        if self.speed:
            return f'{round(self.speed * 1e3)} ms'

    @property
    def host(self):
        # https://developer.mozilla.org/en-US/docs/Web/API/URL/host
        return f'{self.ip}:{self.http_port}'

    @property
    def url(self):
        return 'http://' + self.host
