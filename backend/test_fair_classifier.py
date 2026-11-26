import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from PIL import Image, ImageDraw
import numpy as np

# 1. Corn leaf with rust (elongated 3:1)
corn_rust = Image.new("RGB", (120, 360), color=(255, 255, 255))
d = ImageDraw.Draw(corn_rust)
d.polygon([(60, 10), (100, 100), (105, 260), (60, 350), (15, 260), (20, 100)], fill=(70, 150, 40))
for y in [80, 120, 160, 200, 240, 280]:
    d.ellipse([50, y, 70, y + 15], fill=(185, 95, 20))
    d.ellipse([75, y + 20, 90, y + 32], fill=(195, 105, 25))

# 2. Grape leaf (wide 1.08:1, lobed)
grape_leaf = Image.new("RGB", (260, 240), color=(255, 255, 255))
d = ImageDraw.Draw(grape_leaf)
d.polygon([(130, 20), (190, 60), (240, 120), (190, 180), (130, 220), (70, 180), (20, 120), (70, 60)], fill=(45, 145, 55))

# 3. Tomato leaf with concentric early blight spots (aspect 1.6:1, jagged)
tomato_blight = Image.new("RGB", (160, 260), color=(255, 255, 255))
d = ImageDraw.Draw(tomato_blight)
d.polygon([(80, 15), (140, 60), (110, 120), (150, 180), (80, 245), (20, 180), (50, 120), (20, 60)], fill=(65, 155, 45))
d.ellipse([50, 80, 95, 125], fill=(60, 40, 30), outline=(210, 190, 40), width=4)
d.ellipse([60, 90, 85, 115], fill=(90, 60, 40))

# 4. Mango leaf (lanceolate 2.7:1, glossy dark green)
mango_leaf = Image.new("RGB", (100, 270), color=(255, 255, 255))
d = ImageDraw.Draw(mango_leaf)
d.polygon([(50, 15), (85, 80), (90, 180), (50, 260), (10, 180), (15, 80)], fill=(25, 110, 35))

# 5. Apple leaf (simple oval 1.35:1, clean green)
apple_leaf = Image.new("RGB", (180, 245), color=(255, 255, 255))
d = ImageDraw.Draw(apple_leaf)
d.ellipse([30, 20, 150, 225], fill=(50, 165, 50))

print("Synthetic test leaves ready.")
