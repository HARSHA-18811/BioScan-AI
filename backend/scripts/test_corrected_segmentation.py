import sys
from pathlib import Path
from PIL import Image
import numpy as np
import math

backend_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_dir))

from ml.dataset import draw_realistic_biological_leaf
from ml.predict import compute_plant_morphology_score

img = draw_realistic_biological_leaf("Carrot___healthy", 2)
thumb = img.convert("RGB")
thumb.thumbnail((240, 240), Image.Resampling.BILINEAR)
arr = np.array(thumb, dtype=np.float32)
r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]

exg = 2.0 * g - r - b

# Proper leaf tissue segmentation
# Exclude light neutral background
is_neutral_bg = (r > 190.0) & (g > 190.0) & (b > 190.0) & (np.abs(r - g) < 20.0) & (np.abs(g - b) < 20.0)
is_dark_bg = (r < 25.0) & (g < 25.0) & (b < 25.0)

green_tissue = (~is_neutral_bg & ~is_dark_bg) & ((exg > 15.0) | ((g > r * 1.10) & (g > b * 1.10) & (g > 35.0)))
rust_tissue = (~is_neutral_bg & ~is_dark_bg) & (r > 115.0) & (r > g * 1.25) & (r - g > 25.0) & (r > b * 1.50) & (b < 100.0)
necrotic_tissue = (~is_neutral_bg & ~is_dark_bg) & (((r < 75.0) & (g < 70.0) & (b < 65.0) & (r + g + b > 25.0)) | ((r > 50.0) & (r < 135.0) & (g > 30.0) & (g < 100.0) & (b < 65.0) & (r > g * 1.12)))
yellow_tissue = (~is_neutral_bg & ~is_dark_bg) & (r > 100.0) & (g > 90.0) & (b < 85.0) & (r >= g * 0.90) & (r <= g * 1.24) & ~rust_tissue

leaf_mask = green_tissue | rust_tissue | necrotic_tissue | yellow_tissue

y_coords, x_coords = np.where(leaf_mask)
print(f"Leaf pixels detected: {len(y_coords)}")

if len(y_coords) > 80:
    m00 = float(len(y_coords))
    x_bar = float(np.mean(x_coords))
    y_bar = float(np.mean(y_coords))
    u20 = float(np.mean((x_coords - x_bar) ** 2))
    u02 = float(np.mean((y_coords - y_bar) ** 2))
    u11 = float(np.mean((x_coords - x_bar) * (y_coords - y_bar)))
    common_term = math.sqrt(max((u20 - u02) ** 2 + 4.0 * (u11 ** 2), 0.0))
    lambda1 = (u20 + u02 + common_term) / 2.0
    lambda2 = max((u20 + u02 - common_term) / 2.0, 1e-4)
    leaf_aspect = math.sqrt(max(lambda1 / lambda2, 1.0))
    h_span = float(np.max(y_coords) - np.min(y_coords) + 1)
    w_span = float(np.max(x_coords) - np.min(x_coords) + 1)
    bbox_area = max(h_span * w_span, 1.0)
    solidity = float(len(y_coords)) / bbox_area

    print(f"Aspect ratio: {leaf_aspect:.4f}")
    print(f"Solidity:     {solidity:.4f}")

    print("\nMorphology scores with corrected segmentation:")
    for plant in ["Carrot", "Cabbage", "Grape", "Apple", "Potato", "Tomato"]:
        score = compute_plant_morphology_score(plant, leaf_aspect, solidity, 0.0, 0.5)
        print(f"  {plant}: {score:.4f}")
