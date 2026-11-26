import sys
from pathlib import Path
from PIL import Image

backend_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_dir))

from ml.predict import BioScanPredictor
from ml.dataset import draw_realistic_biological_leaf

predictor = BioScanPredictor()
print(f"Predictor ready: {predictor.is_ready()}, Total enrolled classes: {len(predictor.classes)}")

test_cases = [
    ("Carrot___healthy", "carrot_leaf_specimen.jpg"),
    ("Carrot___Alternaria_leaf_blight", "carrot_blight.jpg"),
    ("Carrot___Powdery_mildew", "carrot_mildew.jpg"),
    ("Mango___healthy", "mango_healthy.jpg"),
    ("Potato___Early_blight", "potato_early_blight.jpg"),
    ("Apple___Apple_scab", "apple_scab.jpg"),
]

print("\n--- Running Empirical Foliar Diagnostics ---")
for cls_name, fn in test_cases:
    img = draw_realistic_biological_leaf(cls_name, 0)
    result = predictor.predict_image(img, filename=fn)
    print(f"\n[Test Input: {cls_name} ({fn})]")
    print(f"  -> Predicted Leaf: {result['leaf_name']}")
    print(f"  -> Host Plant:    {result['plant_name']}")
    print(f"  -> Condition:      {result['condition_name']}")
    print(f"  -> Confidence:     {result['confidence'] * 100:.2f}%")
    print(f"  -> Healthy:        {result['is_healthy']}")
    print(f"  -> Organic Sol:    {result['pathological_details'].get('solutions', {}).get('organic', 'N/A')[:60]}...")
