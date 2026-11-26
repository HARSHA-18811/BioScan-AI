"""
Model Evaluation Pipeline for BioScan AI.
Computes real test-set accuracy, precision, recall, F1-scores, and confusion matrix.
Strictly records genuine metrics without fabrication.
"""

import sys
import json
from pathlib import Path
from datetime import datetime, timezone

# Add backend directory to path
backend_dir = Path(__file__).resolve().parent.parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

import torch
from torch.utils.data import DataLoader
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix

from ml.config import config
from ml.dataset import set_seed, get_transforms, PlantLeafDataset, scan_and_split_dataset
from ml.model import get_model

def evaluate(
    model_path: Path = None,
    classes_path: Path = None,
    architecture: str = "lite",
    batch_size: int = 16
):
    print("=" * 60)
    print("BioScan AI - Model Evaluation Pipeline")
    print("=" * 60)

    model_path = model_path or config.model_save_path
    classes_path = classes_path or config.classes_save_path

    if not model_path.exists():
        print(f"Error: Model file not found at {model_path}.")
        print("Please run train.py first to train and produce model weights.")
        return None

    if not classes_path.exists():
        print(f"Error: Classes file not found at {classes_path}.")
        return None

    with open(classes_path, "r", encoding="utf-8") as f:
        classes = json.load(f)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Evaluation Device: {device}")

    # Load test split
    _, _, test_samples = scan_and_split_dataset(
        raw_dir=config.raw_data_dir,
        classes=classes,
        train_ratio=config.train_split,
        val_ratio=config.val_split,
        seed=config.random_seed
    )

    if len(test_samples) == 0:
        print("No test samples found in data/raw test split.")
        return None

    print(f"Evaluating on {len(test_samples)} test samples across {len(classes)} classes...")

    _, eval_tf = get_transforms(config.img_size)
    test_dataset = PlantLeafDataset(test_samples, transform=eval_tf)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=config.num_workers)

    # Load model
    model = get_model(architecture=architecture, num_classes=len(classes), pretrained=False)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model = model.to(device)
    model.eval()

    all_preds = []
    all_targets = []

    with torch.no_grad():
        for images, labels in test_loader:
            images = images.to(device)
            outputs = model(images)
            _, predicted = outputs.max(1)
            all_preds.extend(predicted.cpu().numpy().tolist())
            all_targets.extend(labels.numpy().tolist())

    # Compute metrics
    acc = accuracy_score(all_targets, all_preds)
    macro_p, macro_r, macro_f1, _ = precision_recall_fscore_support(
        all_targets, all_preds, average="macro", zero_division=0
    )
    weighted_p, weighted_r, weighted_f1, _ = precision_recall_fscore_support(
        all_targets, all_preds, average="weighted", zero_division=0
    )

    # Per-class metrics
    per_class_p, per_class_r, per_class_f1, support = precision_recall_fscore_support(
        all_targets, all_preds, average=None, labels=list(range(len(classes))), zero_division=0
    )

    per_class_dict = {}
    for i, cls_name in enumerate(classes):
        per_class_dict[cls_name] = {
            "precision": round(float(per_class_p[i]), 4),
            "recall": round(float(per_class_r[i]), 4),
            "f1_score": round(float(per_class_f1[i]), 4),
            "support": int(support[i])
        }

    # Confusion matrix
    cm = confusion_matrix(all_targets, all_preds, labels=list(range(len(classes))))
    cm_list = cm.tolist()

    metrics_result = {
        "evaluated": True,
        "model_architecture": architecture,
        "model_file": model_path.name,
        "dataset_name": "PlantVillage Foliar Pathology Subset",
        "test_samples": len(test_samples),
        "accuracy": round(float(acc), 4),
        "macro_precision": round(float(macro_p), 4),
        "macro_recall": round(float(macro_r), 4),
        "macro_f1": round(float(macro_f1), 4),
        "weighted_f1": round(float(weighted_f1), 4),
        "class_names": classes,
        "per_class_metrics": per_class_dict,
        "confusion_matrix": cm_list,
        "evaluation_date": datetime.now(timezone.utc).isoformat(),
        "notes": "Evaluation performed on held-out test split with zero data leakage."
    }

    with open(config.metrics_save_path, "w", encoding="utf-8") as f:
        json.dump(metrics_result, f, indent=2)

    print(f"Accuracy: {metrics_result['accuracy'] * 100:.2f}%")
    print(f"Macro F1-Score: {metrics_result['macro_f1']:.4f}")
    print(f"Saved evaluation metrics to: {config.metrics_save_path}")

    return metrics_result

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Evaluate BioScan AI Model")
    parser.add_argument("--arch", type=str, default="lite", choices=["lite", "mobilenet_v2"])
    parser.add_argument("--batch_size", type=int, default=16)
    args = parser.parse_args()

    evaluate(architecture=args.arch, batch_size=args.batch_size)
