from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import ProductCategory, Product, ProductImage


class ProductImageInline(TranslationTabularInline):
    model = ProductImage
    extra = 1
    fields = ("image", "alt_text", "order")


@admin.register(ProductCategory)
class ProductCategoryAdmin(TranslationAdmin):
    list_display = ("name", "slug", "order", "is_active")
    list_editable = ("order", "is_active")
    prepopulated_fields = {"slug": ("name_uk",)}
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ("name", "sku", "category", "availability", "is_active", "order")
    list_filter = ("category", "availability", "is_active")
    list_editable = ("is_active", "order", "availability")
    search_fields = ("name", "sku", "description")
    prepopulated_fields = {"slug": ("name_uk",)}
    inlines = [ProductImageInline]
    fieldsets = (
        (_("Основна інформація"), {
            "fields": ("name", "slug", "category", "sku", "brand")
        }),
        (_("Опис"), {
            "fields": ("short_description", "description", "image")
        }),
        (_("Ціна та наявність"), {
            "fields": ("price", "currency", "availability")
        }),
        (_("SEO"), {
            "fields": ("meta_title", "meta_description", "meta_keywords"),
            "classes": ("collapse",)
        }),
        (_("Публікація"), {
            "fields": ("is_active", "order")
        }),
    )
