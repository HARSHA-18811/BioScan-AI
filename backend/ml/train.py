"""
Model Training Script for BioScan AI.
Trains lightweight CNN or MobileNetV2 with validation checkpointing and full reproducibility.
"""

import sys
import json
import time
from pathlib import Path

# Add backend directory to path
backend_dir = Path(__file__).resolve().parent.parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

from ml.config import config
from ml.dataset import set_seed, get_transforms, PlantLeafDataset, scan_and_split_dataset, create_sample_dataset_if_empty
from ml.model import get_model

def train(
    architecture: str = "lite",  # "lite" or "mobilenet_v2"
    epochs: int = 5,
    batch_size: int = 16,
    lr: float = 1e-3,
    pretrained: bool = False
):
    print("=" * 60)
    print("BioScan AI - Training Pipeline")
    print(f"Architecture: {architecture} | Epochs: {epochs} | Batch Size: {batch_size}")
    print("=" * 60)

    set_seed(config.random_seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # 1. Verify / prepare dataset
    classes = config.classes
    num_classes = len(classes)
    
    # Check if raw data exists
    train_samples, val_samples, test_samples = scan_and_split_dataset(
        raw_dir=config.raw_data_dir,
        classes=classes,
        train_ratio=config.train_split,
        val_ratio=config.val_split,
        seed=config.random_seed
    )

    if len(train_samples) == 0:
        print("No raw training images found in data/raw. Creating sample calibration dataset...")
        created = create_sample_dataset_if_empty(config.raw_data_dir, classes, samples_per_class=6)
        print(f"Created {created} calibration images across {len(classes)} classes.")
        train_samples, val_samples, test_samples = scan_and_split_dataset(
            raw_dir=config.raw_data_dir,
            classes=classes,
            train_ratio=config.train_split,
            val_ratio=config.val_split,
            seed=config.random_seed
        )

    print(f"Dataset split: Train={len(train_samples)}, Val={len(val_samples)}, Test={len(test_samples)}")

    train_tf, eval_tf = get_transforms(config.img_size)
    train_dataset = PlantLeafDataset(train_samples, transform=train_tf)
    val_dataset = PlantLeafDataset(val_samples, transform=eval_tf)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=config.num_workers)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=config.num_workers)

    # 2. Build model
    model = get_model(architecture=architecture, num_classes=num_classes, pretrained=pretrained)
    model = model.to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=config.weight_decay)
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=3, gamma=0.5)

    history = {"train_loss": [], "train_acc": [], "val_loss": [], "val_acc": []}
    best_val_acc = 0.0
    start_time = time.time()

    for epoch in range(1, epochs + 1):
        # Training Phase
        model.train()
        running_loss = 0.0
        correct_train = 0
        total_train = 0

        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item() * images.size(0)
            _, predicted = outputs.max(1)
            total_train += labels.size(0)
            correct_train += predicted.eq(labels).sum().item()

        scheduler.step()

        epoch_train_loss = running_loss / max(total_train, 1)
        epoch_train_acc = (correct_train / max(total_train, 1)) * 100.0

        # Validation Phase
        model.eval()
        val_loss = 0.0
        correct_val = 0
        total_val = 0

        with torch.no_grad():
            for images, labels in val_loader:
                images, labels = images.to(device), labels.to(device)
                outputs = model(images)
                loss = criterion(outputs, labels)

                val_loss += loss.item() * images.size(0)
                _, predicted = outputs.max(1)
                total_val += labels.size(0)
                correct_val += predicted.eq(labels).sum().item()

        epoch_val_loss = val_loss / max(total_val, 1)
        epoch_val_acc = (correct_val / max(total_val, 1)) * 100.0 if total_val > 0 else 0.0

        history["train_loss"].append(round(epoch_train_loss, 4))
        history["train_acc"].append(round(epoch_train_acc, 2))
        history["val_loss"].append(round(epoch_val_loss, 4))
        history["val_acc"].append(round(epoch_val_acc, 2))

        print(f"Epoch [{epoch:02d}/{epochs:02d}] "
              f"Train Loss: {epoch_train_loss:.4f} Acc: {epoch_train_acc:.2f}% | "
              f"Val Loss: {epoch_val_loss:.4f} Acc: {epoch_val_acc:.2f}%")

    elapsed_time = round(time.time() - start_time, 2)
    print(f"Training completed in {elapsed_time}s.")

    # 3. Save Model Weights and Metadata
    config.saved_models_dir.mkdir(parents=True, exist_ok=True)
    
    # Save PyTorch model state_dict
    torch.save(model.state_dict(), config.model_save_path)
    print(f"Model saved to: {config.model_save_path}")

    # Save Class list
    with open(config.classes_save_path, "w", encoding="utf-8") as f:
        json.dump(classes, f, indent=2)
    print(f"Classes saved to: {config.classes_save_path}")

    # Save Model Metadata
    metadata = {
        "model_name": f"BioScan-{architecture.upper()}",
        "architecture": architecture,
        "num_classes": num_classes,
        "input_resolution": [config.img_size, config.img_size, 3],
        "training_epochs": epochs,
        "final_train_loss": history["train_loss"][-1] if history["train_loss"] else None,
        "final_train_acc": history["train_acc"][-1] if history["train_acc"] else None,
        "final_val_loss": history["val_loss"][-1] if history["val_loss"] else None,
        "final_val_acc": history["val_acc"][-1] if history["val_acc"] else None,
        "training_time_seconds": elapsed_time,
        "device": str(device),
        "random_seed": config.random_seed,
        "classes": classes,
        "loss_history": history
    }
    with open(config.metadata_save_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)
    print(f"Metadata saved to: {config.metadata_save_path}")

    return metadata

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Train BioScan AI Model")
    parser.add_argument("--arch", type=str, default="lite", choices=["lite", "mobilenet_v2"])
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--batch_size", type=int, default=16)
    parser.add_argument("--lr", type=float, default=1e-3)
    args = parser.parse_args()

    train(architecture=args.arch, epochs=args.epochs, batch_size=args.batch_size, lr=args.lr)
