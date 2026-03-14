import logging

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from catalog.models import Product, ProductCategory

from .forms import ContactForm

logger = logging.getLogger(__name__)


def landing(request):
    categories = ProductCategory.objects.filter(is_active=True).order_by("order")
    featured = Product.objects.filter(is_active=True).exclude(slug="").order_by("order")[:6]
    form = ContactForm()
    return render(request, "core/landing.html", {
        "categories": categories,
        "featured": featured,
        "form": form,
        "page_title": _("Магнум — Виробництво упаковки"),
        "meta_description": _(
            "Корпорація Магнум — виробництво якісного пакування, пакетів та плівки. "
            "Дніпро. Замовте індивідуальне рішення для вашого бізнесу."
        ),
    })


def _send_contact_notification(contact) -> None:
    """Send an email notification to the manager when a new contact request arrives."""
    recipient = settings.CONTACT_EMAIL
    if not recipient or not settings.EMAIL_HOST_USER:
        return
    subject = f"Нова заявка від {contact.name}"
    body = (
        f"Ім'я: {contact.name}\n"
        f"Телефон: {contact.phone}\n"
        f"Email: {contact.email or '—'}\n\n"
        f"Повідомлення:\n{contact.message}"
    )
    try:
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [recipient], fail_silently=False)
    except Exception:
        logger.exception("Failed to send contact notification email for request id=%s", contact.pk)


def contact_submit(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            _send_contact_notification(contact)
            return render(request, "partials/contact_success.html")
        return render(request, "partials/contact_form.html", {"form": form})
    return HttpResponse(status=405)
