import sys
from pathlib import Path

backend_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_dir))

from ml.dataset import draw_realistic_biological_leaf
from ml.predict import extract_biological_features, compute_plant_morphology_score

img = draw_realistic_biological_leaf("Carrot___healthy", 2)
feats = extract_biological_features(img)
print("Extracted features for Carrot leaf:")
for k, v in feats.items():
    print(f"  {k}: {v:.4f}")

print("\nMorphology scores for different crops:")
for plant in ["Carrot", "Cabbage", "Grape", "Apple", "Potato", "Tomato"]:
    score = compute_plant_morphology_score(plant, feats["aspect"], feats["solidity"], feats["dark_green"], feats["circularity"])
    print(f"  {plant}: {score:.4f}")
