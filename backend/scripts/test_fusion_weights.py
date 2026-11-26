import sys
from pathlib import Path
from PIL import Image
import numpy as np

backend_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_dir))

from ml.predict import BioScanPredictor
from ml.dataset import draw_realistic_biological_leaf

predictor = BioScanPredictor()

test_cases = [
    ("Carrot___healthy", "DSC_001.jpg"),
    ("Carrot___Alternaria_leaf_blight", "DSC_002.jpg"),
    ("Mango___healthy", "DSC_003.jpg"),
    ("Potato___Early_blight", "DSC_004.jpg"),
    ("Apple___Apple_scab", "DSC_005.jpg"),
    ("Corn___Common_rust", "DSC_006.jpg"),
    ("Tomato___Bacterial_spot", "DSC_007.jpg"),
]

print("Comparing Fusion Weights on Unlabelled Camera Images:")
for bio_w, cnn_w in [(1.0, 0.4), (0.7, 1.2), (0.8, 1.8), (0.5, 2.0)]:
    correct = 0
    print(f"\n--- Bio Weight: {bio_w}, CNN Weight: {cnn_w} ---")
    for cls_name, fn in test_cases:
        img = draw_realistic_biological_leaf(cls_name, 0)
        # Manually compute with weights
        tensor = predictor.model
        res = predictor.predict_image(img, filename=fn)
        # We can simulate inside predictor or test output
        target_plant = cls_name.split("___")[0]
        match = res["plant_name"] == target_plant
        if match: correct += 1
        print(f"  [{cls_name}] -> {res['leaf_name']} ({res['condition_name']}) | Target: {target_plant} | Match: {match}")
    print(f"Accuracy: {correct}/{len(test_cases)}")
