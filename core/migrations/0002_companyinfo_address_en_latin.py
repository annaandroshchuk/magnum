# Set English address and city to Latin script for EN version

from django.db import migrations


def set_address_en_latin(apps, schema_editor):
    CompanyInfo = apps.get_model("core", "CompanyInfo")
    obj = CompanyInfo.objects.filter(pk=1).first()
    if obj:
        obj.address_en = "49102, Dnipro, 46 Volynska St"
        obj.city_en = "Dnipro"
        obj.save()


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(set_address_en_latin, noop),
    ]
