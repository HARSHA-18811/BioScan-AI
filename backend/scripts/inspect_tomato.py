import sys
from pathlib import Path
backend_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_dir))

from ml.dataset import draw_realistic_biological_leaf
from ml.predict import extract_biological_features

t_img = draw_realistic_biological_leaf("Tomato___Bacterial_spot", 0)
feats = extract_biological_features(t_img)
print("Tomato features:")
for k, v in feats.items():
    print(f"  {k}: {v:.4f}")
