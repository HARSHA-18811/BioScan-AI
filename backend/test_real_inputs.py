import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from PIL import Image, ImageDraw
import numpy as np
from ml.predict import predictor_instance

# 1. Corn leaf (elongated, green with orange-brown rust pustules)
corn_rust = Image.new("RGB", (120, 360), color=(255, 255, 255))
d = ImageDraw.Draw(corn_rust)
d.polygon([(60, 10), (100, 100), (105, 260), (60, 350), (15, 260), (20, 100)], fill=(70, 150, 40))
for y in [80, 120, 160, 200, 240, 280]:
    d.ellipse([50, y, 70, y + 15], fill=(185, 95, 20))
    d.ellipse([75, y + 20, 90, y + 32], fill=(195, 105, 25))

# 2. Grape leaf (palmate, lobed, wide)
grape_leaf = Image.new("RGB", (260, 240), color=(255, 255, 255))
d = ImageDraw.Draw(grape_leaf)
d.polygon([(130, 20), (190, 60), (240, 120), (190, 180), (130, 220), (70, 180), (20, 120), (70, 60)], fill=(45, 145, 55))

# 3. Tomato leaf with concentric early blight spots
tomato_blight = Image.new("RGB", (200, 220), color=(255, 255, 255))
d = ImageDraw.Draw(tomato_blight)
d.polygon([(100, 20), (160, 70), (140, 140), (100, 200), (60, 140), (40, 70)], fill=(65, 155, 45))
d.ellipse([70, 70, 120, 120], fill=(60, 40, 30), outline=(200, 180, 40), width=4)
d.ellipse([80, 80, 110, 110], fill=(90, 60, 40))

# 4. Mango leaf (lanceolate, glossy dark green)
mango_leaf = Image.new("RGB", (100, 300), color=(255, 255, 255))
d = ImageDraw.Draw(mango_leaf)
d.polygon([(50, 15), (85, 90), (90, 210), (50, 290), (10, 210), (15, 90)], fill=(25, 110, 35))

# 5. Apple leaf (simple oval, clean green)
apple_leaf = Image.new("RGB", (200, 250), color=(255, 255, 255))
d = ImageDraw.Draw(apple_leaf)
d.ellipse([35, 25, 165, 225], fill=(50, 165, 50))

# Completely generic filenames like what a camera or WhatsApp or screenshot produces!
tests = [
    (corn_rust, "IMG_001.jpg", "Expected Corn Rust"),
    (grape_leaf, "IMG_002.jpg", "Expected Grape"),
    (tomato_blight, "IMG_003.jpg", "Expected Tomato Blight"),
    (mango_leaf, "IMG_004.jpg", "Expected Mango Leaf"),
    (apple_leaf, "IMG_005.jpg", "Expected Apple Healthy"),
]

for img, fn, desc in tests:
    res = predictor_instance.predict_image(img, filename=fn)
    print(f"Test: {desc:<22} | Filename: {fn:<14} -> {res['leaf_name']:<15} | {res['condition_name']:<20} | Conf: {res['confidence']*100:.1f}%")
