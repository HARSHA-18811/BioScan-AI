import json
from pathlib import Path
import sys
sys.path.insert(0, "backend")
from ml.config import DEFAULT_CLASSES

additional = [
    "Curry_Leaf___healthy",
    "Money_Plant___Bacterial_leaf_spot",
    "Money_Plant___healthy"
]

all_classes = sorted(list(set(DEFAULT_CLASSES + additional)))
print(f"Total updated classes: {len(all_classes)}")

# Update config.py
config_path = Path("backend/ml/config.py")
content = config_path.read_text(encoding="utf-8")

py_classes_str = "DEFAULT_CLASSES: List[str] = " + json.dumps(all_classes, indent=4)
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
