from django import forms
from django.utils.translation import gettext_lazy as _

from .models import ContactRequest


class ContactForm(forms.ModelForm):
    # Honeypot: bots fill it, humans leave it empty.
    website = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = ContactRequest
        fields = ("name", "phone", "email", "message")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": _("Ваше ім'я *"), "autocomplete": "name"}),
            "phone": forms.TextInput(attrs={"placeholder": _("Телефон *"), "autocomplete": "tel"}),
            "email": forms.EmailInput(attrs={"placeholder": _("Email"), "autocomplete": "email"}),
            "message": forms.Textarea(attrs={"placeholder": _("Ваше повідомлення або запитання..."), "rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["phone"].required = True
        self.fields["email"].required = False

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("website"):
            raise forms.ValidationError("Bot detected.")
        return cleaned_data
