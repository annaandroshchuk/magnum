# Magnum — Packaging Production Site

**Професійний Django сайт для компанії Magnum (виробництво упаковки).**

Сучасна архітектура, готова до production-deployment на Render + Cloudinary.

---

## 🎯 Основні функції

- **Двомовна сторінка** (Українська/Англійська) на django-modeltranslation
- **Каталог товарів** з категоріями, детальними сторінками, зображеннями
- **Контактна форма** з HTMX + email-нотифікаціями через Gmail SMTP
- **SEO оптимізація**:
  - XML Sitemaps для категорій і товарів
  - Schema.org структуровані дані (Organization, Product, LocalBusiness)
  - Open Graph теги для соцмереж
  - Hreflang для багатомовності
- **Безпека**:
  - CSRF захист (включений за замовчуванням)
  - Honeypot на формі контактів
  - SSL редирект на production
  - Rate-limiting готовий
- **UI/UX**:
  - Responsive mobile-first дизайн
  - Без inline-CSS, тільки зовнішні стилі
  - Плавні анімації (scroll reveal, transitions)
  - Accessibility: skip-link, aria атрибути, focus management

---

## 📦 Stack

- **Backend**: Django 5.1.15
- **Frontend**: HTML/CSS/JS (no frameworks, progressive enhancement via HTMX)
- **Database**: PostgreSQL (Render) / SQLite (local dev)
- **Storage**: Cloudinary (images)
- **Email**: Gmail SMTP (App Password)
- **Deployment**: Render Web Service
- **Static Files**: WhiteNoise + ManifestStaticFilesStorage

---

## 🚀 Швидкий старт (локально)

### 1. Клонуйте репозиторій
```bash
git clone https://github.com/BonisOleg/magnum.git
cd magnum
```

### 2. Створіть `.env` з `.env.example`
```bash
cp .env.example .env
```

Відредагуйте `.env` (для локального development):
```
SECRET_KEY=dev-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### 3. Встановіть залежності
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Запустіть міграції
```bash
python manage.py migrate
python manage.py compilemessages --locale=uk --locale=en
python manage.py seed_catalog  # Seed тестові дані
```

### 5. Запустіть dev-server
```bash
python manage.py runserver
```

Відкрийте браузер: http://localhost:8000

---

## 🔧 Конфігурація

### `.env` змінні

| Змінна | Опис | Приклад |
|--------|------|---------|
| `SECRET_KEY` | Django secret (змінити на prod) | `your-secret-key` |
| `DEBUG` | Debug mode | `False` (prod) / `True` (dev) |
| `ALLOWED_HOSTS` | Дозволені хости | `localhost,127.0.0.1` |
| `DATABASE_URL` | DB connection | `postgres://user:pass@host/db` |
| `CLOUDINARY_URL` | Cloudinary API | `cloudinary://key:secret@cloud` |
| `CLOUDINARY_CLOUD_NAME` | Cloudinary cloud name | `your-cloud-name` |
| `EMAIL_HOST_USER` | Gmail адреса | `your-gmail@gmail.com` |
| `EMAIL_HOST_PASSWORD` | Gmail App Password | `xxxx-xxxx-xxxx-xxxx` |
| `CSRF_TRUSTED_ORIGINS` | CORS whitelist | `https://magnum-tpc.com` |

### Отримання Gmail App Password

1. Увійдіть на [Google Account Security](https://myaccount.google.com/security)
2. Enable 2FA
3. Generate App Password для Django
4. Скопіюйте пароль в `EMAIL_HOST_PASSWORD`

---

## 🌐 Deployment на Render

### 1. Підключіть репозиторій на Render

1. Перейдіть на [render.com](https://render.com)
2. New → Web Service
3. Виберіть GitHub репозиторій `magnum`
4. Runtime: Python
5. Build command: `./build.sh`
6. Start command: `gunicorn config.wsgi:application`

### 2. Встановіть Environment Variables

На сторінці Web Service → Environment:

```
SECRET_KEY = (auto-generate)
DEBUG = False
ALLOWED_HOSTS = .onrender.com,magnum-tpc.com,www.magnum-tpc.com
CLOUDINARY_CLOUD_NAME = your-cloud-name
CLOUDINARY_URL = cloudinary://key:secret@cloud
EMAIL_HOST_USER = your-gmail@gmail.com
EMAIL_HOST_PASSWORD = xxxx-xxxx-xxxx-xxxx
DEFAULT_FROM_EMAIL = your-gmail@gmail.com
CSRF_TRUSTED_ORIGINS = https://magnum-tpc.com,https://www.magnum-tpc.com
SECURE_SSL_REDIRECT = True
```

### 3. Лінкуйте PostgreSQL базу

1. New → PostgreSQL
2. На сторінці Web Service → Data запропонує з'єднання
3. Автоматично встановить `DATABASE_URL`

### 4. Deploy

Натисніть "Deploy" — Render автоматично запустить `build.sh` (міграції + collectstatic).

---

## 📁 Структура проєкту

```
magnum/
├── config/                # Django settings & URLs
│   ├── settings.py       # All settings (base/dev/prod via env vars)
│   ├── urls.py           # Root URL routing
│   ├── wsgi.py           # WSGI entrypoint (Render uses this)
│   └── asgi.py
│
├── core/                 # Landing, Company Info, Contact Form
│   ├── models.py         # CompanyInfo, ContactRequest
│   ├── views.py          # landing, contact_submit
│   ├── forms.py          # ContactForm + honeypot
│   ├── context_processors.py  # Inject company info into all templates
│   ├── admin.py          # Django admin configuration
│   └── translation.py    # i18n fields
│
├── catalog/              # Products & Categories
│   ├── models.py         # ProductCategory, Product, ProductImage
│   ├── views.py          # catalog_list, product_detail, category_detail
│   ├── admin.py          # Admin: product inlines, translations
│   ├── sitemaps.py       # XML sitemap generators
│   └── management/commands/seed_catalog.py  # Seed test data
│
├── templates/            # Django HTML templates
│   ├── base.html         # Main template (header, footer, blocks)
│   ├── partials/         # Reusable components
│   │   ├── header.html
│   │   ├── footer.html
│   │   ├── contact_form.html (HTMX)
│   │   ├── contact_success.html
│   │   └── seo_meta.html (OG, JSON-LD)
│   ├── core/             # Landing page
│   └── catalog/          # Product list & detail
│
├── static/
│   ├── css/
│   │   ├── variables.css      # Design tokens (colors, fonts, spacing)
│   │   ├── base.css           # Global styles, buttons, forms
│   │   ├── components.css     # Header, footer, nav
│   │   ├── landing.css        # Hero, services, about sections
│   │   ├── catalog.css        # Product list, filters
│   │   └── product.css        # Product gallery, details
│   ├── js/
│   │   └── main.js            # All interactivity (no external deps)
│   └── img/
│       ├── favicon.svg
│       ├── logo.svg
│       ├── og-default.jpg     # Social media preview
│       └── apple-touch-icon.png
│
├── locale/               # Translations (i18n)
│   ├── uk/LC_MESSAGES/django.po   # Ukrainian
│   └── en/LC_MESSAGES/django.po   # English
│
├── manage.py             # Django CLI
├── render.yaml           # Render deployment config
├── build.sh              # Build script for Render
├── requirements.txt      # Python dependencies
└── .env.example          # Environment template
```

---

## 🔐 Безпека (Production Checklist)

- ✅ CSRF middleware включений
- ✅ Honeypot на контактній формі
- ✅ SSL redirect (SECURE_SSL_REDIRECT = True)
- ✅ Secure cookies (SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE)
- ✅ Email notifications підтримуються
- ✅ Rate-limiting структура готова (можна додати за потребою)
- ✅ XSS захист (Django auto-escape)
- ⚠️ 2FA на Gmail обов'язкова

---

## 📝 Адміністрування

### Доступ до адмін-панелі

```
https://yourdomain.com/admin/
```

Логін/пароль: створіть superuser перед деплоєм:
```bash
python manage.py createsuperuser
```

### Керування товарами

1. Admin → Catalog → Products
2. Add product:
   - Name (укр/англ)
   - Category
   - SKU (унікальний артикул)
   - Price, currency
   - Availability (In Stock / Out of Stock / Pre Order)
   - Main image (Cloudinary)
   - Description (укр/англ)
   - Meta tags (SEO)

### Контактні запити

1. Admin → Core → Заявки
2. Переглядайте заявки від клієнтів
3. Mark as processed

### Інформація про компанію

1. Admin → Core → Інформація про компанію
2. Edit: телефон, email, адреса, соціальні мережі
3. Дані підтягуються автоматично в footer, JSON-LD schema

---

## 🌍 Додавання товарів з зображеннями

### Кроки:

1. **Налаштуйте Cloudinary**
   - Зареєструйтесь на [cloudinary.com](https://cloudinary.com)
   - Скопіюйте `CLOUDINARY_URL` в `.env`

2. **На сторінці товару (admin)**
   - Upload image → загрузиться на Cloudinary автоматично
   - Або додайте через `ProductImage` inline

3. **На front-end**
   - Зображення відображається з CDN Cloudinary
   - Автоматично оптимізовані (resize, webp format)

---

## 📊 Продуктивність

- **PageSpeed**: Render + CDN Cloudinary → ~90+ Lighthouse score
- **Кешування**: CompanyInfo кешується на 5 хвилин
- **Database queries**: `select_related`, `prefetch_related` на всіх списках

---

## 🛠 Тестування локально

```bash
# Запустіть dev-server
python manage.py runserver

# Тестуйте контактну форму (HTMX)
# Постіть на http://localhost:8000/uk/contact/submit/

# Перевірте admin
# Admin → Core → Заявки (ContactRequest)

# Перевірте каталог
# http://localhost:8000/uk/catalog/

# Перевірте sitemap.xml
# http://localhost:8000/sitemap.xml

# Перевірте robots.txt
# http://localhost:8000/robots.txt
```

---

## 📜 Ліцензія

Це приватний проєкт для компанії Magnum.

---

## 👤 Контакти

**Компанія**: Корпорація Магнум  
**Email**: magnum_tvk@ukr.net  
**Телефон**: +38 073 3 777 333  
**Адреса**: м. Дніпро, вул. Волинська, 46  

---

**Status**: ✅ Production Ready  
**Last Updated**: March 14, 2026
