import json
from pathlib import Path

ADDITIONAL_CLASSES = [
    "Ashoka___healthy",
    "Bamboo___healthy",
    "Banyan___healthy",
    "Brinjal___healthy",
    "Coconut___healthy",
    "Coffee___Leaf_rust",
    "Coffee___healthy",
    "Cotton___Bacterial_blight",
    "Cotton___healthy",
    "Eucalyptus___healthy",
    "Ginger___healthy",
    "Hibiscus___healthy",
    "Mint___healthy",
    "Moringa___healthy",
    "Neem___Leaf_spot",
    "Neem___healthy",
    "Papaya___Leaf_curl",
    "Papaya___healthy",
    "Pomegranate___healthy",
    "Sugarcane___Red_rot",
    "Sugarcane___healthy",
    "Tea___healthy",
    "Tulsi___Powdery_mildew",
    "Tulsi___healthy",
    "Watermelon___healthy"
]

config_path = Path("backend/ml/config.py")
content = config_path.read_text(encoding="utf-8")

# Extract current DEFAULT_CLASSES
import sys
sys.path.insert(0, "backend")
from ml.config import DEFAULT_CLASSES

all_classes = sorted(list(set(DEFAULT_CLASSES + ADDITIONAL_CLASSES)))
print(f"Total updated classes: {len(all_classes)}")

# Replace DEFAULT_CLASSES in config.py
classes_str = json.dumps(all_classes, indent=4)
# Format as Python list
py_classes_str = "DEFAULT_CLASSES: List[str] = " + classes_str

start_marker = "DEFAULT_CLASSES: List[str] = ["
end_marker = "]"
idx_start = content.find(start_marker)
idx_end = content.find(end_marker, idx_start) + 1

new_content = content[:idx_start] + py_classes_str + content[idx_end:]
config_path.write_text(new_content, encoding="utf-8")
print("Updated backend/ml/config.py successfully!")

# Update classes.json
classes_json_path = Path("backend/saved_models/classes.json")
classes_json_path.write_text(json.dumps(all_classes, indent=2), encoding="utf-8")
print(f"Updated {classes_json_path} successfully!")
