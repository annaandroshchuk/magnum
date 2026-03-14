from modeltranslation.translator import register, TranslationOptions
from .models import ProductCategory, Product, ProductImage


@register(ProductCategory)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ("name", "description")


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "short_description",
        "description",
        "meta_title",
        "meta_description",
        "meta_keywords",
    )


@register(ProductImage)
class ProductImageTranslationOptions(TranslationOptions):
    fields = ("alt_text",)
