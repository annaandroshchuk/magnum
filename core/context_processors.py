from django.core.cache import cache

from .models import CompanyInfo

_CACHE_KEY = "company_info_singleton"
_CACHE_TTL = 300  # 5 minutes


def company_info(request):
    company = cache.get(_CACHE_KEY)
    if company is None:
        company = CompanyInfo.get()
        cache.set(_CACHE_KEY, company, _CACHE_TTL)
    return {"company": company}
