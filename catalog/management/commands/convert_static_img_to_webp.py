"""
Конвертує всі PNG у static/img/ у WebP з тими ж базовими іменами (x.png → x.webp).
"""
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Convert PNG images in static/img to WebP (same base names)."

    def handle(self, *args, **options):
        img_dir = Path(settings.BASE_DIR) / "static" / "img"
        if not img_dir.is_dir():
            self.stdout.write(self.style.WARNING(f"Directory not found: {img_dir}"))
            return

        png_files = sorted(img_dir.glob("*.png"))
        if not png_files:
            self.stdout.write(self.style.WARNING("No PNG files found in static/img."))
            return

        try:
            from PIL import Image
        except ImportError:
            self.stdout.write(self.style.ERROR("Pillow is required. Install with: pip install Pillow"))
            return

        converted = 0
        for png_path in png_files:
            webp_path = png_path.with_suffix(".webp")
            try:
                with Image.open(png_path) as im:
                    if im.mode in ("RGBA", "P"):
                        im = im.convert("RGBA")
                    elif im.mode != "RGB":
                        im = im.convert("RGB")
                    im.save(webp_path, "WEBP", quality=85)
                self.stdout.write(f"  {png_path.name} -> {webp_path.name}")
                converted += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"  {png_path.name}: {e}"))

        self.stdout.write(self.style.SUCCESS(f"\nConverted {converted} image(s) to WebP."))
