import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from PIL import Image
from ml.predict import predictor_instance

test_files = [
    ("backend/data/raw/Apple___Apple_scab/sample_1.jpg", "IMG_001.jpg"),
    ("backend/data/raw/Apple___healthy/sample_1.jpg", "IMG_002.jpg"),
    ("backend/data/raw/Corn___Common_rust/sample_1.jpg", "IMG_003.jpg"),
    ("backend/data/raw/Corn___healthy/sample_1.jpg", "IMG_004.jpg"),
    ("backend/data/raw/Potato___Early_blight/sample_1.jpg", "IMG_005.jpg"),
    ("backend/data/raw/Tomato___healthy/sample_1.jpg", "IMG_006.jpg"),
]

print(f"{'Source Image':<40} | {'Filename':<12} | {'Predicted Leaf':<15} | {'Condition':<20} | {'Conf':<6}")
print("-" * 105)

for p, fn in test_files:
    p_obj = Path(p)
    if p_obj.exists():
        img = Image.open(p_obj)
        res = predictor_instance.predict_image(img, filename=fn)
        print(f"{p_obj.parent.name:<40} | {fn:<12} | {res['leaf_name']:<15} | {res['condition_name']:<20} | {res['confidence']*100:.1f}%")
