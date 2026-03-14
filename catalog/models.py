from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
import cloudinary
import cloudinary.models


class ProductCategory(models.Model):
    name = models.CharField(_("Назва"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True, max_length=200)
    description = models.TextField(_("Опис"), blank=True)
    order = models.PositiveIntegerField(_("Порядок"), default=0)
    is_active = models.BooleanField(_("Активна"), default=True)

    class Meta:
        verbose_name = _("Категорія")
        verbose_name_plural = _("Категорії")
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:category", kwargs={"slug": self.slug})


AVAILABILITY_CHOICES = [
    ("InStock", _("В наявності")),
    ("OutOfStock", _("Немає в наявності")),
    ("PreOrder", _("Під замовлення")),
]

AVAILABILITY_SCHEMA = {
    "InStock": "https://schema.org/InStock",
    "OutOfStock": "https://schema.org/OutOfStock",
    "PreOrder": "https://schema.org/PreOrder",
}


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        verbose_name=_("Категорія"),
    )
    name = models.CharField(_("Назва"), max_length=255)
    slug = models.SlugField(_("Slug"), unique=True, max_length=255)
    short_description = models.CharField(_("Короткий опис"), max_length=500, blank=True)
    description = models.TextField(_("Повний опис"), blank=True)
    image = cloudinary.models.CloudinaryField(_("Головне фото"), blank=True, null=True)
    sku = models.CharField(_("Артикул (SKU)"), max_length=100, unique=True)
    brand = models.CharField(_("Бренд"), max_length=100, default="Magnum")
    price = models.DecimalField(_("Ціна"), max_digits=12, decimal_places=2, null=True, blank=True)
    currency = models.CharField(_("Валюта"), max_length=10, default="UAH")
    availability = models.CharField(
        _("Наявність"), max_length=20, choices=AVAILABILITY_CHOICES, default="InStock"
    )
    meta_title = models.CharField(_("Meta Title"), max_length=255, blank=True)
    meta_description = models.CharField(_("Meta Description"), max_length=500, blank=True)
    meta_keywords = models.CharField(_("Meta Keywords"), max_length=500, blank=True)
    is_active = models.BooleanField(_("Активний"), default=True)
    order = models.PositiveIntegerField(_("Порядок"), default=0)
    created_at = models.DateTimeField(_("Створено"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Оновлено"), auto_now=True)

    class Meta:
        verbose_name = _("Товар")
        verbose_name_plural = _("Товари")
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"slug": self.slug})

    def get_schema_availability(self):
        return AVAILABILITY_SCHEMA.get(self.availability, "https://schema.org/InStock")

    def get_main_image_url(self):
        if self.image:
            return self.image.url
        images = self.images.all()
        if images:
            return images[0].image.url
        return None


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images", verbose_name=_("Товар")
    )
    image = cloudinary.models.CloudinaryField(_("Зображення"))
    alt_text = models.CharField(_("Alt текст"), max_length=255, blank=True)
    order = models.PositiveIntegerField(_("Порядок"), default=0)

    class Meta:
        verbose_name = _("Зображення товару")
        verbose_name_plural = _("Зображення товару")
        ordering = ["order"]

    def __str__(self):
        return f"{self.product.name} — фото {self.order}"
