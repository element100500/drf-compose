from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampedModel(models.Model):
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)

    class Meta:
        abstract = True


class ActivatableModel(models.Model):
    is_active = models.BooleanField(_('active'), default=True)

    class Meta:
        abstract = True

    def activate(self):
        self.is_active = True
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()
