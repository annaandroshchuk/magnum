from modeltranslation.translator import register, TranslationOptions
from .models import CompanyInfo


@register(CompanyInfo)
class CompanyInfoTranslationOptions(TranslationOptions):
    fields = ("address", "city")
