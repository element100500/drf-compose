from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    code = models.CharField(_('code'), max_length=2, unique=True, help_text=_('ISO 3166'))

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        ordering = ('name',)

    def __str__(self):
        return self.name
