import sys
from pathlib import Path
import shutil

backend_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_dir))

from ml.config import config
from ml.dataset import create_sample_dataset_if_empty
from app.services.plant_knowledge import CLASS_KNOWLEDGE_BASE, PLANT_SPECIES_INFO

print(f"Total config classes: {len(config.classes)}")
print(f"Carrot in species info: {'Carrot' in PLANT_SPECIES_INFO}")
carrot_classes = [c for c in config.classes if "Carrot" in c]
print(f"Carrot classes in config: {carrot_classes}")

for c in carrot_classes:
    print(f"  Knowledge for {c}: {c in CLASS_KNOWLEDGE_BASE}")

raw_dir = config.raw_data_dir
print(f"Raw data dir: {raw_dir}")

# Clear and re-populate raw dataset for all 43 classes
if raw_dir.exists():
    shutil.rmtree(raw_dir)
raw_dir.mkdir(parents=True, exist_ok=True)

print("Generating realistic biological foliar calibration samples for all 43 classes...")
create_sample_dataset_if_empty(raw_dir, config.classes, samples_per_class=10)

classes_present = [d.name for d in raw_dir.iterdir() if d.is_dir()]
total_samples = sum(len(list(d.glob("*.jpg"))) for d in raw_dir.iterdir() if d.is_dir())
print(f"Dataset preparation complete: {len(classes_present)} classes generated, {total_samples} total images.")
