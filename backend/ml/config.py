"""
ML Pipeline Configuration for BioScan AI.
Fixed random seeds, dataset specifications, hyperparameters, and class indices.
Supports full agricultural crop catalog: Carrot, Strawberry, Banana, Cucumber, Rose,
Guava, Cabbage, Onion, Rice, Wheat, Mango, Citrus, Pepper, Apple, Corn, Grape, Potato, Tomato.
"""

from pathlib import Path
from dataclasses import dataclass, field
from typing import List

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
SAVED_MODELS_DIR = BASE_DIR / "saved_models"

# Ensure directories exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
SAVED_MODELS_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_CLASSES: List[str] = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Ashoka___healthy",
    "Bamboo___healthy",
    "Banana___Black_sigatoka",
    "Banana___healthy",
    "Banyan___healthy",
    "Brinjal___healthy",
    "Cabbage___Black_rot",
    "Cabbage___healthy",
    "Carrot___Alternaria_leaf_blight",
    "Carrot___Powdery_mildew",
    "Carrot___healthy",
    "Citrus___Citrus_canker",
    "Citrus___healthy",
    "Coconut___healthy",
    "Coffee___Leaf_rust",
    "Coffee___healthy",
    "Corn___Common_rust",
    "Corn___Northern_Leaf_Blight",
    "Corn___healthy",
    "Cotton___Bacterial_blight",
    "Cotton___healthy",
    "Cucumber___Powdery_mildew",
    "Cucumber___healthy",
    "Curry_Leaf___healthy",
    "Eucalyptus___healthy",
    "Ginger___healthy",
    "Grape___Black_rot",
    "Grape___healthy",
    "Guava___Wilt",
    "Guava___healthy",
    "Hibiscus___healthy",
    "Mango___Anthracnose",
    "Mango___Bacterial_canker",
    "Mango___healthy",
    "Mint___healthy",
    "Money_Plant___Bacterial_leaf_spot",
    "Money_Plant___healthy",
    "Moringa___healthy",
    "Neem___Leaf_spot",
    "Neem___healthy",
    "Onion___Purple_blotch",
    "Onion___healthy",
    "Papaya___Leaf_curl",
    "Papaya___healthy",
    "Pepper___Bacterial_spot",
    "Pepper___healthy",
    "Pomegranate___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Rice___Brown_spot",
    "Rice___healthy",
    "Rose___Black_spot",
    "Rose___healthy",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Sugarcane___Red_rot",
    "Sugarcane___healthy",
    "Tea___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___healthy",
    "Tulsi___Powdery_mildew",
    "Tulsi___healthy",
    "Watermelon___healthy",
    "Wheat___Leaf_rust",
    "Wheat___healthy"
]

@dataclass
class MLConfig:
    random_seed: int = 42
    img_size: int = 224
    batch_size: int = 16
    num_workers: int = 0  # 0 is safe for Windows CPU multi-processing
    epochs: int = 15
    learning_rate: float = 1e-3
    weight_decay: float = 1e-4
    train_split: float = 0.70
    val_split: float = 0.15
    test_split: float = 0.15
    model_architecture: str = "lite"
    classes: List[str] = field(default_factory=lambda: DEFAULT_CLASSES)
    
    # Paths
    raw_data_dir: Path = RAW_DATA_DIR
    processed_data_dir: Path = PROCESSED_DATA_DIR
    saved_models_dir: Path = SAVED_MODELS_DIR
    model_save_path: Path = SAVED_MODELS_DIR / "bioscan_mobilenet.pth"
    classes_save_path: Path = SAVED_MODELS_DIR / "classes.json"
    metadata_save_path: Path = SAVED_MODELS_DIR / "model_meta.json"

config = MLConfig()
