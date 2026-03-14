from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin
from .models import CompanyInfo, ContactRequest


@admin.register(CompanyInfo)
class CompanyInfoAdmin(TranslationAdmin):
    fieldsets = (
        (_("Контакти"), {"fields": ("email", "phone")}),
        (_("Адреса"), {"fields": ("address", "city")}),
        (_("Соцмережі"), {"fields": ("telegram", "viber", "instagram", "facebook")}),
    )

    def has_add_permission(self, request):
        return not CompanyInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "is_processed", "created_at")
    list_filter = ("is_processed", "created_at")
    search_fields = ("name", "email", "phone", "message")
    list_editable = ("is_processed",)
    readonly_fields = ("name", "email", "phone", "message", "created_at")
    ordering = ("-created_at",)
