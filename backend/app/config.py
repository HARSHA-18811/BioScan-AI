import os
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Set

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"
SAVED_MODELS_DIR = BASE_DIR / "saved_models"
METRICS_FILE = SAVED_MODELS_DIR / "evaluation_metrics.json"
MODEL_WEIGHTS_FILE = SAVED_MODELS_DIR / "bioscan_mobilenet.pth"
CLASSES_FILE = SAVED_MODELS_DIR / "classes.json"
DATABASE_PATH = BASE_DIR / "database.sqlite3"

# Ensure runtime directories exist
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
SAVED_MODELS_DIR.mkdir(parents=True, exist_ok=True)

@dataclass
class Settings:
    PROJECT_NAME: str = "BioScan AI – Biological Image Analysis"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    ALLOWED_EXTENSIONS: Set[str] = field(default_factory=lambda: {".jpg", ".jpeg", ".png"})
    MAX_IMAGE_SIZE_BYTES: int = 10 * 1024 * 1024  # 10 MB
    DEFAULT_IMG_SIZE: int = 224
    DATABASE_PATH: Path = DATABASE_PATH
    MODEL_PATH: Path = MODEL_WEIGHTS_FILE
    CLASSES_PATH: Path = CLASSES_FILE
    METRICS_PATH: Path = METRICS_FILE
    CORS_ORIGINS: List[str] = field(default_factory=lambda: [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ])

settings = Settings()
