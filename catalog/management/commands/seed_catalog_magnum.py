"""
Завантаження товарів з magnum-tpc.com (3 блоки слайдера).
Дані та URL зображень взяті з головної сторінки сайту.
"""
import logging
from django.core.management.base import BaseCommand
from catalog.models import ProductCategory, Product

logger = logging.getLogger(__name__)

BASE_IMG = "https://magnum-tpc.com/wp-content/uploads/2021/12"

# 3 сторінки/блоки з сайту: Пакети (1–6), Плівки та мішки (7–12), Папір та коробки (13–16)
PRODUCTS_MAGNUM = [
    # Блок 1 — Пакети
    {"name_uk": "Пакети Wicket під хліб курку", "name_en": "Wicket bags for bread and chicken", "slug": "pakety-wicket", "category_slug": "pakety", "image_path": "Group-819.png", "order": 1},
    {"name_uk": "Пакети ВОРР із липкою стрічкою", "name_en": "BOPP bags with adhesive tape", "slug": "pakety-bopp-lipka", "category_slug": "pakety", "image_path": "Group-820.png", "order": 2},
    {"name_uk": "Пакети з перфорацією", "name_en": "Bags with perforation", "slug": "pakety-perforaciya", "category_slug": "pakety", "image_path": "Group-821.png", "order": 3},
    {"name_uk": "Пакети LDPE", "name_en": "LDPE bags", "slug": "pakety-ldpe", "category_slug": "pakety", "image_path": "Group-822.png", "order": 4},
    {"name_uk": "Пакети HDPE", "name_en": "HDPE bags", "slug": "pakety-hdpe", "category_slug": "pakety", "image_path": "Group-823.png", "order": 5},
    {"name_uk": "Пакети біорозкладні", "name_en": "Biodegradable bags", "slug": "pakety-biorozkladni", "category_slug": "pakety", "image_path": "Group-824.png", "order": 6},
    # Блок 2 — Плівки та мішки
    {"name_uk": "Плівка поліетиленова", "name_en": "Polyethylene film", "slug": "plivka-polietilenova", "category_slug": "plivky", "image_path": "Group-825.png", "order": 7},
    {"name_uk": "BOPP плівка", "name_en": "BOPP film", "slug": "bopp-plivka", "category_slug": "plivky", "image_path": "Group-826.png", "order": 8},
    {"name_uk": "(СРР) Плівка поліпропіленова", "name_en": "CPP polypropylene film", "slug": "plivka-cpp", "category_slug": "plivky", "image_path": "Group-827.png", "order": 9},
    {"name_uk": "Плівка з друком", "name_en": "Printed film", "slug": "plivka-druk", "category_slug": "plivky", "image_path": "1-85.png", "order": 10},
    {"name_uk": "Плівка з перфорацією", "name_en": "Perforated film", "slug": "plivka-perforaciya", "category_slug": "plivky", "image_path": "1-86.png", "order": 11},
    {"name_uk": "Поліпропіленові мішки", "name_en": "Polypropylene bags", "slug": "mishky-polipropilenovi", "category_slug": "korobky", "image_path": "1-83.png", "order": 12},
    # Блок 3 — Папір та коробки
    {"name_uk": "Паперові пакети", "name_en": "Paper bags", "slug": "papirovi-pakety", "category_slug": "korobky", "image_path": "1-81.png", "order": 13},
    {"name_uk": "Пакет \"дой-пак\"", "name_en": "Doy-pack pouch", "slug": "doj-pak", "category_slug": "pakety", "image_path": "1-81-1.png", "order": 14},
    {"name_uk": "Картонні коробки", "name_en": "Cardboard boxes", "slug": "kartonni-korobky", "category_slug": "korobky", "image_path": "1-82.png", "order": 15},
]


def _upload_image_from_url(url):
    try:
        import cloudinary.uploader
        result = cloudinary.uploader.upload(url)
        return result.get("public_id")
    except Exception as e:
        logger.warning("Cloudinary upload failed for %s: %s", url, e)
        return None


class Command(BaseCommand):
    help = "Seeds catalog from magnum-tpc.com: 15 products + images from site."

    def handle(self, *args, **options):
        self.stdout.write("Ensuring categories exist...")
        cat_map = {}
        for slug, name_uk in [("pakety", "Пакети"), ("plivky", "Плівки"), ("korobky", "Коробки та мішки")]:
            cat, _ = ProductCategory.objects.get_or_create(
                slug=slug,
                defaults={"name": name_uk, "name_uk": name_uk, "name_en": name_uk, "order": len(cat_map), "is_active": True},
            )
            cat_map[slug] = cat

        self.stdout.write("Creating/updating products and loading images from magnum-tpc.com...")
        for p in PRODUCTS_MAGNUM:
            cat = cat_map.get(p["category_slug"])
            image_url = f"{BASE_IMG}/{p['image_path']}"
            public_id = _upload_image_from_url(image_url)

            defaults = {
                "name": p["name_uk"],
                "name_uk": p["name_uk"],
                "name_en": p["name_en"],
                "category": cat,
                "sku": "MAG-" + p["slug"].replace("-", "")[:14].upper(),
                "short_description": "",
                "short_description_uk": "",
                "short_description_en": "",
                "description": "",
                "description_uk": "",
                "description_en": "",
                "brand": "Magnum",
                "availability": "InStock",
                "meta_title": p["name_uk"],
                "meta_title_uk": p["name_uk"],
                "meta_title_en": p["name_en"],
                "meta_description": "",
                "meta_description_uk": "",
                "meta_description_en": "",
                "meta_keywords": "",
                "meta_keywords_uk": "",
                "meta_keywords_en": "",
                "order": p["order"],
                "is_active": True,
            }
            if public_id:
                defaults["image"] = public_id

            product, created = Product.objects.get_or_create(
                slug=p["slug"],
                defaults=defaults,
            )
            if not created:
                product.name = p["name_uk"]
                product.name_uk = p["name_uk"]
                product.name_en = p["name_en"]
                product.meta_title = p["name_uk"]
                product.meta_title_uk = p["name_uk"]
                product.meta_title_en = p["name_en"]
                product.order = p["order"]
                if public_id:
                    product.image = public_id
                product.save(update_fields=["name", "name_uk", "name_en", "meta_title", "meta_title_uk", "meta_title_en", "order", "image"])
            status = "created" if created else "updated"
            img_note = " (image set)" if public_id else " (no image)"
            self.stdout.write(f"  [{status}] {product.name_uk}{img_note}")

        self.stdout.write(self.style.SUCCESS("Done. Catalog seeded from magnum-tpc.com."))
        if not any(Product.objects.exclude(image__isnull=True).exclude(image="")):
            self.stdout.write(
                self.style.WARNING("Images were not uploaded: set CLOUDINARY_URL in .env and run again.")
            )
