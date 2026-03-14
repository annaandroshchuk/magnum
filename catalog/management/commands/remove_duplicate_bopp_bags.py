"""
Видалення дублікатів товару «Пакети ВОРР із липкою стрічкою».
Залишає запис із SKU MAG-M02 (або той, у якого вже відображається фото), видаляє інші.
Після цього встановлює slug=pakety-bopp-lipka та очищає Cloudinary image, щоб показувалось статичне фото Group-820.
"""
from django.core.management.base import BaseCommand
from django.db.models import Q
from catalog.models import Product


PREFERRED_SKU = "MAG-M02"


class Command(BaseCommand):
    help = "Remove duplicate 'Пакети ВОРР із липкою стрічкою', keep SKU MAG-M02, ensure Group-820 photo displays."

    def handle(self, *args, **options):
        candidates = list(
            Product.objects.filter(
                Q(slug="pakety-bopp-lipka") | Q(name__icontains="Пакети ВОРР із липкою стрічкою")
            )
        )
        if len(candidates) <= 1:
            to_keep = candidates[0] if candidates else None
            if not to_keep:
                self.stdout.write("No matching product found.")
                return
        else:
            by_sku = [p for p in candidates if p.sku == PREFERRED_SKU]
            with_photo = [p for p in candidates if not p.image]
            to_keep = by_sku[0] if by_sku else (with_photo[0] if with_photo else candidates[0])
            to_delete = [p for p in candidates if p.pk != to_keep.pk]
            for p in to_delete:
                self.stdout.write(f"Deleting duplicate: {p.name} (pk={p.pk}, slug={p.slug}, sku={p.sku})")
                p.delete()

        need_save = False
        if to_keep.slug != "pakety-bopp-lipka":
            to_keep.slug = "pakety-bopp-lipka"
            need_save = True
        if to_keep.image:
            to_keep.image = None
            need_save = True
        if need_save:
            to_keep.save(update_fields=["slug", "image"])
            self.stdout.write(self.style.SUCCESS("Updated slug/image so Group-820 displays."))

        self.stdout.write(self.style.SUCCESS(f"Kept: {to_keep.name} (pk={to_keep.pk}, slug={to_keep.slug}, sku={to_keep.sku})"))
