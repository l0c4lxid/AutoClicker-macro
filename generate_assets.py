# -*- coding: utf-8 -*-
"""
Stealth Clicker Pro - Asset Generator
Generates high-resolution application icons (PNG and ICO formats) with a Cyberpunk design theme.
"""

import os
import sys

def create_cyberpunk_icon():
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        print("[!] Installing Pillow to generate icon assets...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
        from PIL import Image, ImageDraw

    assets_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
    os.makedirs(assets_dir, exist_ok=True)

    size = (512, 512)
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Background rounded rectangle (Cyberpunk obsidian black with dark cyan border)
    margin = 20
    rect_box = [margin, margin, size[0] - margin, size[1] - margin]
    radius = 80
    
    # Outer Glow / Shadow
    draw.rounded_rectangle(rect_box, radius=radius, fill=(15, 23, 42, 255), outline=(0, 240, 255, 255), width=16)

    # Center Mouse / Shield Icon
    cx, cy = size[0] // 2, size[1] // 2
    
    # Target / Shield Crosshair Hexagon
    poly_points = [
        (cx, cy - 140),
        (cx + 120, cy - 70),
        (cx + 120, cy + 70),
        (cx, cy + 140),
        (cx - 120, cy + 70),
        (cx - 120, cy - 70),
    ]
    draw.polygon(poly_points, fill=(10, 30, 50, 200), outline=(0, 240, 255, 255), width=10)

    # Lightning Bolt / Clicker Symbol (Neon Cyan & Bright Magenta accent)
    bolt_points = [
        (cx + 15, cy - 100),
        (cx - 50, cy + 10),
        (cx + 10, cy + 10),
        (cx - 15, cy + 100),
        (cx + 50, cy - 10),
        (cx - 10, cy - 10),
    ]
    draw.polygon(bolt_points, fill=(0, 240, 255, 255))
    
    # Inner accent core
    inner_bolt = [
        (cx + 10, cy - 70),
        (cx - 30, cy + 5),
        (cx + 5, cy + 5),
        (cx - 10, cy + 70),
        (cx + 30, cy - 5),
        (cx - 5, cy - 5),
    ]
    draw.polygon(inner_bolt, fill=(255, 255, 255, 255))

    # Save PNG
    png_path = os.path.join(assets_dir, "icon.png")
    img.save(png_path, format="PNG")
    print(f"[+] Created PNG Icon: {png_path}")

    # Save ICO (multiple sizes for Windows)
    ico_path = os.path.join(assets_dir, "icon.ico")
    icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    img.save(ico_path, format="ICO", sizes=icon_sizes)
    print(f"[+] Created ICO Icon: {ico_path}")

if __name__ == "__main__":
    create_cyberpunk_icon()
