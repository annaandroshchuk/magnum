from django.db import models
from django.utils.translation import gettext_lazy as _


class CompanyInfo(models.Model):
    email = models.EmailField(_("Email"), default="magnum_tvk@ukr.net")
    phone = models.CharField(_("Телефон"), max_length=32, default="+38 073 3 777 333")
    address = models.CharField(_("Адреса"), max_length=255, default="49102, м. Дніпро, вул. Волинська, 46")
    city = models.CharField(_("Місто"), max_length=100, default="Дніпро")
    telegram = models.CharField(_("Telegram"), max_length=255, blank=True)
    viber = models.CharField(_("Viber"), max_length=32, blank=True)
    instagram = models.URLField(_("Instagram"), blank=True)
    facebook = models.URLField(_("Facebook"), blank=True)

    class Meta:
        verbose_name = _("Інформація про компанію")
        verbose_name_plural = _("Інформація про компанію")

    def __str__(self):
        return "Magnum — Інформація про компанію"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class ContactRequest(models.Model):
    name = models.CharField(_("Ім'я"), max_length=150)
    email = models.EmailField(_("Email"), blank=True)
    phone = models.CharField(_("Телефон"), max_length=32, blank=True)
    message = models.TextField(_("Повідомлення"))
    is_processed = models.BooleanField(_("Оброблено"), default=False)
    created_at = models.DateTimeField(_("Дата"), auto_now_add=True)

    class Meta:
        verbose_name = _("Заявка")
        verbose_name_plural = _("Заявки")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.created_at:%d.%m.%Y %H:%M}"
