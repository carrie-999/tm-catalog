from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class NameRegistration(models.Model):
    STATUS_CHOICES = [
        ('free', _('Wolna')),
        ('reserved', _('W trakcie rejestracji')),
        ('taken', _('Zajęta')),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('Użytkownik')
    )
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('Nazwa')
    )
    country = models.CharField(
        max_length=100,
        verbose_name=_('Kraj/Państwo')
    )
    postal_code = models.CharField(
        max_length=20,
        verbose_name=_('Kod pocztowy')
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        default='free',
        max_length=20,
        verbose_name=_('Status')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Data dodania')
    )

    class Meta:
        verbose_name = _('Rejestracja nazwy')
        verbose_name_plural = _('Rejestracje nazw')

    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"
