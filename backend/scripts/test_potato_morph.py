import math
from PIL import Image, ImageDraw
import numpy as np

def test_potato_morph():
    img = Image.new("RGB", (256, 256), color=(242, 245, 242))
    draw = ImageDraw.Draw(img)
    leaf_color = (40, 135, 38)
    draw.line([(128, 30), (128, 235)], fill=(75, 165, 65), width=3)
    draw.ellipse([98, 25, 158, 105], fill=leaf_color, outline=(22, 90, 20), width=2)
    draw.ellipse([45, 75, 105, 145], fill=leaf_color, outline=(22, 90, 20), width=2)
    draw.ellipse([151, 75, 211, 145], fill=leaf_color, outline=(22, 90, 20), width=2)
    draw.ellipse([55, 135, 115, 200], fill=leaf_color, outline=(22, 90, 20), width=2)
    draw.ellipse([141, 135, 201, 200], fill=leaf_color, outline=(22, 90, 20), width=2)

    thumb = img.convert("RGB")
    thumb.thumbnail((240, 240), Image.Resampling.BILINEAR)
    arr = np.array(thumb, dtype=np.float32)
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    exg = 2.0 * g - r - b
    is_neutral_bg = (r > 185.0) & (g > 185.0) & (b > 185.0) & (np.abs(r - g) < 22.0) & (np.abs(g - b) < 22.0)
    foreground = ~is_neutral_bg
    mask = foreground & ((exg > 12.0) | ((g > r * 1.08) & (g > b * 1.08) & (g > 35.0)))
    y_coords, x_coords = np.where(mask)
    h_span = float(np.max(y_coords) - np.min(y_coords) + 1)
    w_span = float(np.max(x_coords) - np.min(x_coords) + 1)
    bbox_area = max(h_span * w_span, 1.0)
    solidity = float(len(y_coords)) / bbox_area
    m00 = float(len(y_coords))
    x_bar = float(np.mean(x_coords))
    y_bar = float(np.mean(y_coords))
    u20 = float(np.mean((x_coords - x_bar) ** 2))
    u02 = float(np.mean((y_coords - y_bar) ** 2))
    u11 = float(np.mean((x_coords - x_bar) * (y_coords - y_bar)))
    common_term = math.sqrt(max((u20 - u02) ** 2 + 4.0 * (u11 ** 2), 0.0))
    lambda1 = (u20 + u02 + common_term) / 2.0
    lambda2 = max((u20 + u02 - common_term) / 2.0, 1e-4)
    aspect = math.sqrt(max(lambda1 / lambda2, 1.0))
    print(f"Realistic Compound Potato: aspect = {aspect:.3f}, solidity = {solidity:.3f}")

test_potato_morph()
