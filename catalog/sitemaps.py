from django.contrib.sitemaps import Sitemap
from .models import Product, ProductCategory


class ProductSitemap(Sitemap):
    priority = 0.9
    changefreq = "weekly"
    i18n = True

    def items(self):
        return Product.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at


class CategorySitemap(Sitemap):
    priority = 0.8
    changefreq = "monthly"
    i18n = True

    def items(self):
        return ProductCategory.objects.filter(is_active=True).prefetch_related("products")

    def lastmod(self, obj):
        latest = obj.products.filter(is_active=True).order_by("-updated_at").values_list("updated_at", flat=True).first()
        return latest
