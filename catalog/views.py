from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from .models import Product, ProductCategory


def catalog_list(request):
    categories = ProductCategory.objects.filter(is_active=True).prefetch_related(
        "products"
    ).order_by("order")
    products = Product.objects.filter(is_active=True).select_related("category").order_by("order")
    category_slug = request.GET.get("category")
    active_category = None
    if category_slug:
        active_category = get_object_or_404(ProductCategory, slug=category_slug, is_active=True)
        products = products.filter(category=active_category)
    return render(request, "catalog/catalog.html", {
        "categories": categories,
        "products": products,
        "active_category": active_category,
        "page_title": _("Каталог продукції — Magnum"),
        "meta_description": _(
            "Каталог пакувальної продукції Magnum: пакети, плівки, коробки. "
            "Власне виробництво у Дніпрі. Доставка по Україні."
        ),
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    images = product.images.all()
    related = Product.objects.filter(
        category=product.category, is_active=True
    ).exclude(pk=product.pk)[:4]
    return render(request, "catalog/product_detail.html", {
        "product": product,
        "images": images,
        "related": related,
        "page_title": product.meta_title or product.name,
        "meta_description": product.meta_description or product.short_description,
    })


def category_detail(request, slug):
    category = get_object_or_404(ProductCategory, slug=slug, is_active=True)
    products = Product.objects.filter(category=category, is_active=True).order_by("order")
    categories = ProductCategory.objects.filter(is_active=True).order_by("order")
    return render(request, "catalog/catalog.html", {
        "categories": categories,
        "products": products,
        "active_category": category,
        "page_title": f"{category.name} — Magnum",
        "meta_description": category.description or _(
            "Пакувальна продукція Magnum — власне виробництво, доставка по Україні."
        ),
    })
