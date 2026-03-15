"""
Оновлення short_description та description для товарів каталогу.
Джерела: magnum-tpc.com, allanpack.com, artha-s.com, smartpack.org.ua.
"""
from django.core.management.base import BaseCommand
from catalog.models import Product


PRODUCT_DESCRIPTIONS = {
    "pakety-bopp-lipka": {
        "short_description_uk": "Пакети з двоосно-орієнтованої поліпропіленової плівки (BOPP) з липкою стрічкою для зручного відриву. Прозорі, міцні, підходять для автоматизованого пакування та ручної фасовки.",
        "short_description_en": "Bags made from biaxially oriented polypropylene (BOPP) film with adhesive tape for easy tear-off. Transparent, strong, suitable for automated packaging and hand filling.",
        "description_uk": """Пакети ВОРР із липкою стрічкою виготовляються з двоосно-орієнтованої поліпропіленової плівки (BOPP). Липка стрічка дозволяє швидко відривати пакети один від одного та зручно розміщувати їх на вітрині або на виробничій лінії.

BOPP-плівка відрізняється високою міцністю, прозорістю та стійкістю до жирів і вологи. Пакети підходять для пакування хлібобулочних виробів, снеків, кондитерських виробів та інших товарів. Можливий флексографічний друк логотипу або маркування.

Корпорація Магнум виробляє пакети ВОРР із липкою стрічкою на замовлення — різні розміри, товщини та тиражі. Замовляйте безпосередньо у виробника в Дніпрі.""",
        "description_en": """BOPP bags with adhesive tape are made from biaxially oriented polypropylene (BOPP) film. The adhesive strip allows quick separation of bags and convenient placement on the shelf or production line.

BOPP film offers high strength, transparency and resistance to fats and moisture. The bags are suitable for bakery products, snacks, confectionery and other goods. Flexographic printing of logo or labelling is available.

Magnum Corporation produces BOPP bags with adhesive tape to order — various sizes, thicknesses and runs. Order directly from the manufacturer in Dnipro.""",
    },
    "pakety-perforaciya": {
        "short_description_uk": "Пакети з мікро- або макроперфорацією для «дихання» упаковки. Ідеальні для хліба, булок, зелені та квітів. Зберігають свіжість і захищають продукт.",
        "short_description_en": "Bags with micro- or macro-perforation for packaging breathability. Ideal for bread, buns, herbs and flowers. Preserve freshness and protect the product.",
        "description_uk": """Пакети з перфорацією забезпечують обмін повітрям і вологістю всередині упаковки, що продовжує збереження свіжості продукції. Мікроперфорація підходить для хліба та булок; макроперфорація (євро-отвір) — для рулонів на вітрині та зручного підвісу.

Застосування: хлібобулочні вироби, свіжа зелень, квіти, частина снекової та кондитерської продукції. Матеріал — поліетилен або поліпропілен різної товщини. Можливий флексодрук.

Виробляємо пакети з перфорацією за вашими розмірами та тиражами. Дніпро, доставка по Україні.""",
        "description_en": """Perforated bags allow air and moisture exchange inside the package, extending product freshness. Micro-perforation suits bread and buns; macro-perforation (euro-slot) suits display rolls and easy hanging.

Applications: bakery products, fresh herbs, flowers, part of snack and confectionery production. Material — polyethylene or polypropylene in various thicknesses. Flexo printing available.

We produce perforated bags to your dimensions and runs. Dnipro, delivery across Ukraine.""",
    },
    "pakety-ldpe": {
        "short_description_uk": "Пакети з поліетилену низької щільності (LDPE). Еластичні, прозорі, стійкі до розривів. Флексодрук. Харчова та промислова упаковка від виробника.",
        "short_description_en": "Bags from low-density polyethylene (LDPE). Elastic, transparent, tear-resistant. Flexo printing. Food and industrial packaging from the manufacturer.",
        "description_uk": """Пакети LDPE виготовляються з поліетилену низької щільності. Матеріал еластичний, прозорий, добре підходить для пакування продуктів з нерівною поверхнею. Висока стійкість до розривів та проколів забезпечує надійність при транспортуванні та зберіганні.

Застосування: харчова продукція (хліб, овочі, заморозка), побутова хімія, промислові товари. Можливість нанесення флексографічного друку в кілька кольорів — логотип, маркування, дизайн. Контроль якості на всіх етапах виробництва.

Magnum виробляє пакети LDPE у Дніпрі. Індивідуальні розміри, товщина від 25 мкм, мінімальні партії уточнюйте у менеджера.""",
        "description_en": """LDPE bags are made from low-density polyethylene. The material is elastic, transparent and well suited for packaging products with uneven surfaces. High tear and puncture resistance ensures reliability in transport and storage.

Applications: food products (bread, vegetables, frozen goods), household chemicals, industrial goods. Multi-colour flexographic printing available — logo, labelling, design. Quality control at all production stages.

Magnum produces LDPE bags in Dnipro. Custom sizes, thickness from 25 µm; minimum order quantities on request.""",
    },
    "pakety-hdpe": {
        "short_description_uk": "Пакети з поліетилену високої щільності (HDPE). Міцні, матові або напівпрозорі. Для важких вантажів, сміття, промислового та господарського призначення.",
        "short_description_en": "Bags from high-density polyethylene (HDPE). Strong, matte or semi-transparent. For heavy loads, waste, industrial and household use.",
        "description_uk": """Пакети HDPE виготовляються з поліетилену високої щільності. Відрізняються підвищеною міцністю та жорсткістю порівняно з LDPE. Матовий або напівпрозорий вигляд, стійкість до механічних навантажень.

Застосування: упаковка важких та гострих предметів, побутове сміття, промислове пакування, господарські та будівельні потреби. Можливий друк для брендування та маркування.

Виробництво пакетів HDPE на замовлення — різні розміри та щільність. Корпорація Магнум, Дніпро. Оптові ціни, доставка по Україні.""",
        "description_en": """HDPE bags are made from high-density polyethylene. They offer greater strength and rigidity than LDPE. Matte or semi-transparent appearance, resistance to mechanical stress.

Applications: packaging of heavy and sharp items, household waste, industrial packaging, domestic and construction use. Printing available for branding and labelling.

HDPE bags made to order — various sizes and density. Magnum Corporation, Dnipro. Wholesale prices, delivery across Ukraine.""",
    },
    "pakety-biorozkladni": {
        "short_description_uk": "Екологічні пакети, що розкладаються в природному середовищі. Зменшують навантаження на довкілля. Для торгівлі, промисловості та побуту.",
        "short_description_en": "Eco-friendly bags that break down in the natural environment. Reduce environmental impact. For retail, industry and household use.",
        "description_uk": """Біорозкладні пакети виготовляються з матеріалів, здатних до розкладання під дією мікроорганізмів, вологи та кисню. Це зменшує тривалість існування відходів у навколишньому середовищі порівняно зі звичайним поліетиленом.

Застосування: торгівля (фасовка, перенос товарів), виставки, події, господарське використання там, де важлива екологічна свідомість. Можливий друк логотипу для брендованої еко-упаковки.

Корпорація Магнум пропонує біорозкладні пакети на замовлення. Консультуємо щодо матеріалів, термінів розкладання та умов замовлення.""",
        "description_en": """Biodegradable bags are made from materials that break down under the action of microorganisms, moisture and oxygen. This shortens the lifetime of waste in the environment compared to conventional polyethylene.

Applications: retail (portioning, carrying goods), exhibitions, events, household use where environmental awareness matters. Logo printing available for branded eco-packaging.

Magnum Corporation offers biodegradable bags to order. We advise on materials, degradation times and order terms.""",
    },
    "plivka-polietilenova": {
        "short_description_uk": "Поліетиленова плівка (PE) для пакування: прозора, еластична, з контролем якості. Флексодрук, різні товщини. Харчова та промислова сфера.",
        "short_description_en": "Polyethylene (PE) film for packaging: transparent, elastic, quality-controlled. Flexo printing, various thicknesses. Food and industrial applications.",
        "description_uk": """Поліетиленова плівка — один з найпоширеніших пакувальних матеріалів. Висока прозорість дозволяє розглядати вміст, еластичність і міцність забезпечують надійний захист продукції. Контроль якості на всіх етапах виробництва.

Характеристики: морозостійкість, низька поглинальна здатність, стійкість до жирів та вологи. Застосування — харчова упаковка (хліб, овочі, заморозка), промислові товари, палітурка. Можливий флексографічний друк у кілька кольорів.

Виробляємо поліетиленову плівку у Дніпрі. Різна товщина та ширина рулону. Замовлення від виробника Magnum, доставка по Україні.""",
        "description_en": """Polyethylene film is one of the most common packaging materials. High transparency allows product visibility; elasticity and strength provide reliable protection. Quality control at all production stages.

Properties: frost resistance, low absorbency, resistance to fats and moisture. Applications — food packaging (bread, vegetables, frozen goods), industrial goods, overwrapping. Multi-colour flexographic printing available.

We produce polyethylene film in Dnipro. Various thickness and reel width. Orders from Magnum manufacturer, delivery across Ukraine.""",
    },
    "plivka-cpp": {
        "short_description_uk": "Каст-плівка поліпропіленова (CPP) — термозварювана, для ламінації та багатошарових структур. Міжшаровий друк, висока прозорість.",
        "short_description_en": "Cast polypropylene (CPP) film — heat-sealable, for lamination and multilayer structures. Interlayer printing, high transparency.",
        "description_uk": """Плівка CPP (cast polypropylene) — поліпропіленова плівка, отримана методом розливу. Термозварювана, з хорошою прозорістю та глянцем. Широко використовується в багатошарових пакувальних структурах разом із BOPP, PET, PE та алюмінієвою фольгою.

Застосування: упаковка снеків, кондитерських виробів, бакалії, господарських товарів. Можливість міжшарового друку та ламінації для створення складних бар'єрних пакетів. Висока стійкість до жирів і вологи.

Корпорація Магнум виробляє CPP-плівку та композитні рішення на замовлення. Консультуємо щодо товщини, ширини рулону та тиражів.""",
        "description_en": """CPP (cast polypropylene) film is polypropylene film produced by cast extrusion. Heat-sealable, with good clarity and gloss. Widely used in multilayer packaging structures together with BOPP, PET, PE and aluminium foil.

Applications: packaging of snacks, confectionery, groceries, household goods. Interlayer printing and lamination available for complex barrier pouches. High resistance to fats and moisture.

Magnum Corporation produces CPP film and composite solutions to order. We advise on thickness, reel width and runs.""",
    },
    "plivka-druk": {
        "short_description_uk": "Плівка з флексографічним друком: логотипи, маркування, дизайн. До 8 кольорів. Для снеків, кондитерки, бакалії, промислових товарів.",
        "short_description_en": "Film with flexographic printing: logos, labelling, design. Up to 8 colours. For snacks, confectionery, groceries, industrial goods.",
        "description_uk": """Плівка з друком — це пакувальна плівка (PE, BOPP, CPP тощо) з нанесеним флексографічним друком. Дозволяє створювати яскраву, інформативну упаковку з логотипом, маркуванням та мальованим дизайном. Можливо до 8 кольорів за один прохід.

Застосування: снекова продукція, кондитерські вироби, бакалія, напої, господарські товари, корм для тварин. Друк забезпечує брендування та відповідність вимогам до маркування харчових продуктів.

Виробництво плівки з друком у Magnum (Дніпро): розробка дизайну, переддрукарська підготовка, виготовлення на замовлення. Оптові тиражі, доставка по Україні.""",
        "description_en": """Printed film is packaging film (PE, BOPP, CPP, etc.) with flexographic printing applied. It enables bright, informative packaging with logo, labelling and graphic design. Up to 8 colours in a single pass.

Applications: snack products, confectionery, groceries, beverages, household goods, animal feed. Printing provides branding and compliance with food labelling requirements.

Printed film production at Magnum (Dnipro): design development, prepress, custom manufacturing. Wholesale runs, delivery across Ukraine.""",
    },
    "plivka-perforaciya": {
        "short_description_uk": "«Дихаюча» плівка з перфорацією для свіжої зелені, квітів, хліба. Регулює вологість і доступ кисню. Зберігає товарний вигляд.",
        "short_description_en": "Breathable perforated film for fresh herbs, flowers, bread. Regulates moisture and oxygen access. Preserves product appearance.",
        "description_uk": """Плівка з перфорацією забезпечує контрольований газо- та вологообмін усередині упаковки. Це продовжує збереження свіжості продуктів, які «дихають» — зелень, квіти, хлібобулочні вироби. Мікроперфорація або макроперфорація підбирається під тип продукту.

Застосування: упаковка свіжої зелені (кроп, петрушка, салати), квітів у горщиках та букетів, хліба та булок, частини овочів. Можливий друк для брендування.

Magnum виробляє перфоровану плівку на замовлення. Консультуємо щодо типу перфорації та розмірів рулону.""",
        "description_en": """Perforated film ensures controlled gas and moisture exchange inside the package. This extends freshness of breathable products — herbs, flowers, bakery. Micro- or macro-perforation is chosen according to product type.

Applications: packaging of fresh herbs (dill, parsley, salads), potted and cut flowers, bread and buns, some vegetables. Printing available for branding.

Magnum produces perforated film to order. We advise on perforation type and reel dimensions.""",
    },
    "mishky-polipropilenovi": {
        "short_description_uk": "Мішки з поліпропілену для промислового пакування: борошно, цукор, добрива, будматеріали. Різна щільність, міцність, можливість друку.",
        "short_description_en": "Polypropylene bags for industrial packaging: flour, sugar, fertilisers, building materials. Various density, strength, printing available.",
        "description_uk": """Поліпропіленові мішки — міцна та економічна упаковка для сипких та штучних товарів. Витримують значні навантаження, стійкі до розривів та проколів. Випускаються різної щільності (від легких до тканинних) залежно від призначення.

Застосування: борошно, цукор, крупи, добрива, будівельні суміші, комбікорми, промислові напівфабрикати. Можливий друк логотипу та маркування для брендованих партій.

Корпорація Магнум виробляє поліпропіленові мішки в Дніпрі. Різні розміри та щільність, оптові партії, доставка по Україні.""",
        "description_en": """Polypropylene bags are strong, economical packaging for bulk and piece goods. They withstand heavy loads and are resistant to tears and punctures. Available in various densities (from lightweight to woven) depending on application.

Applications: flour, sugar, grains, fertilisers, building mixes, animal feed, industrial semi-finished products. Logo and labelling printing available for branded batches.

Magnum Corporation produces polypropylene bags in Dnipro. Various sizes and density, wholesale batches, delivery across Ukraine.""",
    },
    "papirovi-pakety": {
        "short_description_uk": "Паперові пакети з друком логотипу та дизайну. Екологічні, презентабельні. Для ритейлу, подарунків, брендованої упаковки.",
        "short_description_en": "Paper bags with logo and design printing. Eco-friendly, presentable. For retail, gifts, branded packaging.",
        "description_uk": """Паперові пакети — екологічна альтернатива поліетилену. Папір піддається переробці та розкладанню в природному середовищі краще, ніж пластик. Презентабельний вигляд робить їх зручними для ритейлу, подарунків та фірмової упаковки.

Можливості: друк логотипу, повнокольоровий дизайн, різні розміри та форми (з ручками, без ручок, з клапаном). Застосування — магазини одягу та взуття, пекарні, кав'ярні, подарункова упаковка, промо-акції.

Виробляємо паперові пакети на замовлення. Magnum, Дніпро. Розробка дизайну та переддрукарська підготовка.""",
        "description_en": """Paper bags are an eco-friendly alternative to polyethylene. Paper is more recyclable and degrades better in the environment than plastic. Their presentable look makes them suitable for retail, gifts and corporate packaging.

Options: logo printing, full-colour design, various sizes and shapes (with handles, without handles, with flap). Applications — clothing and footwear stores, bakeries, cafés, gift packaging, promotions.

We produce paper bags to order. Magnum, Dnipro. Design and prepress services.""",
    },
    "doj-pak": {
        "short_description_uk": "Стоячий пакет типу «дой-пак» (пауч) для сипких продуктів, напоїв, соусів. Зручний дозатор, яскравий друк. Від виробника.",
        "short_description_en": "Standing pouch (doy-pack, spout pouch) for bulk products, beverages, sauces. Convenient dispenser, bright printing. From the manufacturer.",
        "description_uk": """Пакет «дой-пак» (standing pouch, пауч) — м'яка стояча упаковка з дном та часто з дозатором або клапаном. Зручний для сипких продуктів, напоїв, соусів, кетчупів, медів, снеків. Займає менше місця при зберіганні та транспортуванні порівняно з жорсткою тарою.

Переваги: яскравий флексодрук, можливість дозатора для контролю порції, герметичність, економія матеріалу. Застосування — харчова промисловість, господарські товари, корми для тварин.

Корпорація Магнум виробляє пакети дой-пак на замовлення. Розробка форми, друк, тиражі під ваш продукт. Дніпро, доставка по Україні.""",
        "description_en": """Doy-pack (standing pouch, spout pouch) is a flexible standing package with a base and often a dispenser or valve. Suitable for bulk products, beverages, sauces, ketchups, honey, snacks. Takes up less space in storage and transport than rigid packaging.

Benefits: bright flexo printing, optional dispenser for portion control, sealability, material savings. Applications — food industry, household goods, animal feed.

Magnum Corporation produces doy-pack pouches to order. Shape development, printing, runs for your product. Dnipro, delivery across Ukraine.""",
    },
}


class Command(BaseCommand):
    help = "Update short_description and description for catalog products (from plan sources)."

    def handle(self, *args, **options):
        updated = 0
        for slug, data in PRODUCT_DESCRIPTIONS.items():
            short_uk = data["short_description_uk"]
            short_en = data["short_description_en"]
            desc_uk = data["description_uk"]
            desc_en = data["description_en"]
            if len(short_uk) > 500:
                self.stdout.write(self.style.WARNING(f"  [{slug}] short_description_uk exceeds 500 chars, truncating."))
                short_uk = short_uk[:497] + "..."
            if len(short_en) > 500:
                self.stdout.write(self.style.WARNING(f"  [{slug}] short_description_en exceeds 500 chars, truncating."))
                short_en = short_en[:497] + "..."
            count = Product.objects.filter(slug=slug).update(
                short_description=short_uk,
                short_description_uk=short_uk,
                short_description_en=short_en,
                description=desc_uk,
                description_uk=desc_uk,
                description_en=desc_en,
            )
            if count:
                updated += count
                self.stdout.write(f"  Updated: {slug}")
            else:
                self.stdout.write(f"  Not found: {slug}")
        self.stdout.write(self.style.SUCCESS(f"Done. Updated {updated} product(s)."))
