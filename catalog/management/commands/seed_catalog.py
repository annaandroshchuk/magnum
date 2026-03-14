from django.core.management.base import BaseCommand
from catalog.models import ProductCategory, Product


CATEGORIES = [
    {
        "name_uk": "Пакети",
        "name_en": "Bags",
        "slug": "pakety",
        "description_uk": "Пакети різних форм, матеріалів та розмірів — від продовольчих до промислових.",
        "description_en": "Bags of various shapes, materials and sizes — from food to industrial.",
        "order": 1,
    },
    {
        "name_uk": "Плівки",
        "name_en": "Films",
        "slug": "plivky",
        "description_uk": "Поліетиленові, поліпропіленові та BOPP плівки для пакування різних товарів.",
        "description_en": "Polyethylene, polypropylene and BOPP films for packaging various goods.",
        "order": 2,
    },
    {
        "name_uk": "Коробки та мішки",
        "name_en": "Boxes & Bags",
        "slug": "korobky",
        "description_uk": "Картонні коробки, поліпропіленові мішки та паперові пакети.",
        "description_en": "Cardboard boxes, polypropylene bags and paper packages.",
        "order": 3,
    },
]

PRODUCTS = [
    {
        "name_uk": "Пакети Wicket під хліб та курку",
        "name_en": "Wicket Bags for Bread and Chicken",
        "slug": "pakety-wicket",
        "category_slug": "pakety",
        "short_description_uk": "Пакети Wicket на підвісній стрічці — ідеальні для пакування хлібобулочних виробів та м'ясної продукції (курки, ковбаси).",
        "short_description_en": "Wicket bags on a hanging strip — ideal for packaging bakery products and meat products (chicken, sausage).",
        "description_uk": """Пакети Wicket (вікет-пакети) — вид поліетиленових пакетів на стрічці, що дозволяє автоматизувати процес пакування продукції.

Основні характеристики:
— Матеріал: LDPE, HDPE або BOPP
— Кріплення на підвісній стрічці (wicket)
— Можливість нанесення флексодруку до 6 кольорів
— Розміри: від 18×30 до 45×65 см
— Товщина: 25–50 мкм
— Перфорація: мікро або макро (євро) — опційно

Застосування: хліб, батони, булки, курка, ковбасні вироби, заморожені продукти.

Виготовляємо за вашими розмірами та дизайном. Мінімальне замовлення уточнюйте у менеджера.""",
        "description_en": """Wicket bags are a type of polyethylene bags on a strip that allows automating the product packaging process.

Main characteristics:
— Material: LDPE, HDPE or BOPP
— Mounting on a hanging strip (wicket)
— Possibility of flexo printing up to 6 colors
— Sizes: from 18×30 to 45×65 cm
— Thickness: 25–50 microns
— Perforation: micro or macro (euro) — optional

Applications: bread, loaves, rolls, chicken, sausage products, frozen foods.

We produce according to your sizes and design. Minimum order — contact the manager.""",
        "sku": "MAG-WKT-001",
        "meta_title_uk": "Пакети Wicket — купити від виробника Magnum | Дніпро",
        "meta_title_en": "Wicket Bags — Buy from Manufacturer Magnum | Dnipro",
        "meta_description_uk": "Пакети Wicket під хліб та курку від виробника Magnum (Дніпро). Флексодрук, будь-які розміри. Оптові ціни.",
        "meta_description_en": "Wicket bags for bread and chicken from Magnum manufacturer (Dnipro). Flexo printing, any sizes. Wholesale prices.",
        "meta_keywords_uk": "пакети wicket, вікет пакети, пакети для хліба, пакети для курки, купити пакети виробник",
        "meta_keywords_en": "wicket bags, bread bags, chicken bags, buy bags manufacturer Ukraine",
        "order": 1,
    },
    {
        "name_uk": "BOPP плівка для пакування",
        "name_en": "BOPP Packaging Film",
        "slug": "bopp-plivka",
        "category_slug": "plivky",
        "short_description_uk": "Двоосно-орієнтована поліпропіленова плівка (BOPP) — прозора, матова або металізована. Флексодрук до 8 кольорів.",
        "short_description_en": "Biaxially oriented polypropylene film (BOPP) — transparent, matte or metallized. Flexo printing up to 8 colors.",
        "description_uk": """BOPP (Biaxially Oriented Polypropylene) — двоосно-орієнтована поліпропіленова плівка, широко застосовується в пакувальній промисловості.

Технічні характеристики:
— Ширина рулону: 200–1200 мм
— Товщина: 20–40 мкм
— Прозора, матова, металізована (BOPPmet), біла (перлова)
— Друк: флексографія до 8 кольорів
— Можливість ламінування з CPP, PE, металізованим шаром

Переваги BOPP плівки:
— Висока прозорість
— Стійкість до жирів та вологи
— Хороші барʼєрні властивості
— Можливість термозварювання

Застосування: упаковка снеків, кондитерських виробів, бакалії, косметики, господарських товарів.

Власне виробництво у Дніпрі. Замовлення від 500 кг.""",
        "description_en": """BOPP (Biaxially Oriented Polypropylene) is a biaxially oriented polypropylene film widely used in the packaging industry.

Technical specifications:
— Roll width: 200–1200 mm
— Thickness: 20–40 microns
— Transparent, matte, metallized (BOPPmet), white (pearlescent)
— Printing: flexography up to 8 colors
— Lamination with CPP, PE, metallized layer possible

Advantages of BOPP film:
— High transparency
— Resistance to fats and moisture
— Good barrier properties
— Heat sealing capability

Applications: packaging of snacks, confectionery, grocery, cosmetics, household goods.

Own production in Dnipro. Orders from 500 kg.""",
        "sku": "MAG-BPP-001",
        "meta_title_uk": "BOPP плівка — купити від виробника у Дніпрі | Magnum",
        "meta_title_en": "BOPP Film — Buy from Manufacturer in Dnipro | Magnum",
        "meta_description_uk": "BOPP плівка для пакування від Magnum (Дніпро). Прозора, матова, металізована. Флексодрук. Оптові ціни від виробника.",
        "meta_description_en": "BOPP packaging film from Magnum (Dnipro). Transparent, matte, metallized. Flexo printing. Wholesale prices from manufacturer.",
        "meta_keywords_uk": "BOPP плівка, поліпропіленова плівка, пакувальна плівка, купити плівку, виробник Дніпро",
        "meta_keywords_en": "BOPP film, polypropylene film, packaging film, buy film manufacturer Dnipro Ukraine",
        "order": 2,
    },
    {
        "name_uk": "Картонні коробки на замовлення",
        "name_en": "Custom Cardboard Boxes",
        "slug": "kartonni-korobky",
        "category_slug": "korobky",
        "short_description_uk": "Картонні коробки будь-яких розмірів, форм та кількості. Друк логотипу, розробка дизайну.",
        "short_description_en": "Cardboard boxes of any size, shape and quantity. Logo printing, design development.",
        "description_uk": """Картонні коробки — надійна та естетична упаковка для широкого спектру товарів. Виробляємо на замовлення за вашими розмірами.

Типи коробок:
— Звичайні прямокутні (RSC, FOL)
— Коробки з клапаном
— Самозбірні коробки
— Коробки-пеналки
— Коробки зі вставками та ложементами
— Архівні коробки

Матеріали:
— Мікрогофрокартон (E-flute)
— Тришарова гофра (B, C flute)
— Пятишарова гофра (BC, EB flute)
— Твердий картон 1.5–3 мм

Друк:
— Флексодрук 1-4 кольори
— Офсетний друк (на замовлення)
— Без друку (крафт)

Виготовляємо від 500 шт. Доставка по Україні.""",
        "description_en": """Cardboard boxes — reliable and aesthetic packaging for a wide range of goods. We produce to order according to your dimensions.

Box types:
— Regular rectangular (RSC, FOL)
— Flap boxes
— Self-assembling boxes
— Tube boxes
— Boxes with inserts and trays
— Archive boxes

Materials:
— Micro corrugated (E-flute)
— Three-layer corrugated (B, C flute)
— Five-layer corrugated (BC, EB flute)
— Solid cardboard 1.5–3 mm

Printing:
— Flexo printing 1-4 colors
— Offset printing (on request)
— No printing (kraft)

Production from 500 pcs. Delivery throughout Ukraine.""",
        "sku": "MAG-BOX-001",
        "meta_title_uk": "Картонні коробки на замовлення від виробника | Magnum Дніпро",
        "meta_title_en": "Custom Cardboard Boxes from Manufacturer | Magnum Dnipro",
        "meta_description_uk": "Картонні коробки на замовлення від виробника Magnum (Дніпро). Будь-які розміри, друк, доставка по Україні.",
        "meta_description_en": "Custom cardboard boxes from Magnum manufacturer (Dnipro). Any sizes, printing, delivery across Ukraine.",
        "meta_keywords_uk": "картонні коробки, коробки на замовлення, гофрокоробки, купити коробки виробник Дніпро",
        "meta_keywords_en": "cardboard boxes, custom boxes, corrugated boxes, buy boxes manufacturer Dnipro Ukraine",
        "order": 1,
    },
]


class Command(BaseCommand):
    help = "Seeds the database with initial catalog data (3 products + categories)"

    def handle(self, *args, **options):
        self.stdout.write("Creating categories...")
        cat_map = {}
        for cat_data in CATEGORIES:
            cat, created = ProductCategory.objects.get_or_create(
                slug=cat_data["slug"],
                defaults={
                    "name": cat_data["name_uk"],
                    "name_uk": cat_data["name_uk"],
                    "name_en": cat_data["name_en"],
                    "description": cat_data.get("description_uk", ""),
                    "description_uk": cat_data.get("description_uk", ""),
                    "description_en": cat_data.get("description_en", ""),
                    "order": cat_data["order"],
                    "is_active": True,
                }
            )
            cat_map[cat_data["slug"]] = cat
            status = "created" if created else "exists"
            self.stdout.write(f"  [{status}] {cat.name_uk}")

        self.stdout.write("Creating products...")
        for p in PRODUCTS:
            cat = cat_map.get(p["category_slug"])
            product, created = Product.objects.get_or_create(
                slug=p["slug"],
                defaults={
                    "name": p["name_uk"],
                    "name_uk": p["name_uk"],
                    "name_en": p["name_en"],
                    "category": cat,
                    "short_description": p["short_description_uk"],
                    "short_description_uk": p["short_description_uk"],
                    "short_description_en": p["short_description_en"],
                    "description": p["description_uk"],
                    "description_uk": p["description_uk"],
                    "description_en": p["description_en"],
                    "sku": p["sku"],
                    "brand": "Magnum",
                    "availability": "InStock",
                    "meta_title": p["meta_title_uk"],
                    "meta_title_uk": p["meta_title_uk"],
                    "meta_title_en": p["meta_title_en"],
                    "meta_description": p["meta_description_uk"],
                    "meta_description_uk": p["meta_description_uk"],
                    "meta_description_en": p["meta_description_en"],
                    "meta_keywords": p["meta_keywords_uk"],
                    "meta_keywords_uk": p["meta_keywords_uk"],
                    "meta_keywords_en": p["meta_keywords_en"],
                    "order": p["order"],
                    "is_active": True,
                }
            )
            status = "created" if created else "exists"
            self.stdout.write(f"  [{status}] {product.name_uk} (SKU: {product.sku})")

        self.stdout.write(self.style.SUCCESS("\nDone! Catalog seeded successfully."))
        self.stdout.write("You can now log into admin and add photos via Cloudinary.")
