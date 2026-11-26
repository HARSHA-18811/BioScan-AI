import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from PIL import Image, ImageDraw
import numpy as np

def analyze_leaf_morphology(image: Image.Image):
    orig_w, orig_h = image.size
    img_aspect = max(orig_h / max(orig_w, 1.0), orig_w / max(orig_h, 1.0))

    # Resize preserving approximate proportions for pixel statistics
    thumb = image.convert("RGB")
    thumb.thumbnail((180, 180))
    arr = np.array(thumb, dtype=np.float32)

    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]

    # Background detection
    corners_r = [r[0, 0], r[0, -1], r[-1, 0], r[-1, -1]]
    corners_g = [g[0, 0], g[0, -1], g[-1, 0], g[-1, -1]]
    corners_b = [b[0, 0], b[0, -1], b[-1, 0], b[-1, -1]]
    mean_corner = (np.mean(corners_r) + np.mean(corners_g) + np.mean(corners_b)) / 3.0

    if mean_corner > 180:
        bg_mask = (r > 215) & (g > 215) & (b > 215)
    elif mean_corner < 45:
        bg_mask = (r < 30) & (g < 30) & (b < 30)
    else:
        bg_mask = (np.abs(r - np.mean(corners_r)) < 25) & (np.abs(g - np.mean(corners_g)) < 25) & (np.abs(b - np.mean(corners_b)) < 25)

    leaf_mask = ~bg_mask
    leaf_pixels = max(float(np.sum(leaf_mask)), 100.0)

    # Chlorophyll Green
    green_mask = leaf_mask & (g > r * 1.06) & (g > b * 1.06) & (g > 40)
    green_ratio = float(np.sum(green_mask)) / leaf_pixels

    # Rust spores (cinnamon orange)
    rust_mask = leaf_mask & (r > 110) & (r > g * 1.15) & (r > b * 1.45) & (b < 100)
    rust_ratio = float(np.sum(rust_mask)) / leaf_pixels

    # Necrotic dark lesions
    dark_mask = leaf_mask & (r < 65) & (g < 60) & (b < 55) & (r + g + b > 25)
    brown_mask = leaf_mask & (r > 55) & (r < 140) & (g > 35) & (g < 105) & (b < 70) & (r > g * 1.15)
    necrotic_ratio = float(np.sum(dark_mask | brown_mask)) / leaf_pixels

    # Chlorotic yellow halo
    yellow_mask = leaf_mask & (r > 110) & (g > 105) & (b < 85) & (np.abs(r - g) < 40)
    yellow_ratio = float(np.sum(yellow_mask)) / leaf_pixels

    # Convex hull / Solidity / Lobing
    y_idx, x_idx = np.where(leaf_mask)
    if len(y_idx) > 50:
        h_span = float(np.max(y_idx) - np.min(y_idx) + 1)
        w_span = float(np.max(x_idx) - np.min(x_idx) + 1)
        bbox_area = h_span * w_span
        solidity = leaf_pixels / max(bbox_area, 1.0)
    else:
        solidity = 0.8

    return {
        "aspect": img_aspect,
        "green": green_ratio,
        "rust": rust_ratio,
        "necrotic": necrotic_ratio,
        "yellow": yellow_ratio,
        "solidity": solidity
    }

# 1. Corn leaf (aspect 3:1)
corn = Image.new("RGB", (120, 360), color=(255, 255, 255))
d = ImageDraw.Draw(corn)
d.polygon([(60, 10), (100, 100), (105, 260), (60, 350), (15, 260), (20, 100)], fill=(70, 150, 40))

# 2. Grape leaf (wide, aspect 1.08, lobed)
grape = Image.new("RGB", (260, 240), color=(255, 255, 255))
d = ImageDraw.Draw(grape)
d.polygon([(130, 20), (190, 60), (240, 120), (190, 180), (130, 220), (70, 180), (20, 120), (70, 60)], fill=(45, 145, 55))

# 3. Mango leaf (lanceolate, aspect 2.6)
mango = Image.new("RGB", (110, 290), color=(255, 255, 255))
d = ImageDraw.Draw(mango)
d.polygon([(55, 15), (90, 90), (95, 200), (55, 280), (15, 200), (20, 90)], fill=(25, 110, 35))

# 4. Apple leaf (oval, aspect 1.35)
apple = Image.new("RGB", (180, 245), color=(255, 255, 255))
d = ImageDraw.Draw(apple)
d.ellipse([30, 20, 150, 225], fill=(50, 165, 50))

print("Corn:  ", analyze_leaf_morphology(corn))
print("Grape: ", analyze_leaf_morphology(grape))
print("Mango: ", analyze_leaf_morphology(mango))
print("Apple: ", analyze_leaf_morphology(apple))
