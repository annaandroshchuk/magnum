from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from django.http import HttpResponse
from core.sitemaps import StaticViewSitemap
from catalog.sitemaps import ProductSitemap, CategorySitemap

admin.site.site_header = "Корпорація Магнум"
admin.site.site_title = "Magnum Admin"
admin.site.index_title = "Панель керування"

sitemaps = {
    "static": StaticViewSitemap,
    "products": ProductSitemap,
    "categories": CategorySitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("healthz", lambda r: HttpResponse("ok"), name="healthz"),
]

urlpatterns += i18n_patterns(
    path("", include("core.urls")),
    path("catalog/", include("catalog.urls")),
    prefix_default_language=True,
)
