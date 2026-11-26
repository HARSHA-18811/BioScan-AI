"""
Image Preprocessing Service for Biological Leaf Classification.
Performs verification, sanitization, color-space conversion, resizing, and normalization.
"""

import io
from typing import Tuple, Optional
from PIL import Image
import numpy as np

try:
    import torch
    import torchvision.transforms as transforms
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False


def validate_image_bytes(file_bytes: bytes, max_bytes: int = 10 * 1024 * 1024) -> Tuple[bool, str, Optional[Image.Image]]:
    """
    Validates uploaded raw bytes:
    1. Size check
    2. Header inspection with PIL
    3. Format check (JPEG, PNG)
    """
    if not file_bytes or len(file_bytes) == 0:
        return False, "Uploaded file is empty.", None

    if len(file_bytes) > max_bytes:
        size_mb = len(file_bytes) / (1024 * 1024)
        return False, f"File size ({size_mb:.2f} MB) exceeds maximum allowed limit of {max_bytes / (1024*1024):.0f} MB.", None

    try:
        img = Image.open(io.BytesIO(file_bytes))
        img.verify()  # Verifies file integrity
        # Re-open because verify() closes the file handle
        img = Image.open(io.BytesIO(file_bytes))
    except Exception as e:
        return False, f"Corrupted or invalid image file: {str(e)}", None

    valid_formats = {"JPEG", "JPG", "PNG"}
    if img.format.upper() not in valid_formats:
        return False, f"Unsupported format '{img.format}'. Only JPEG and PNG are permitted.", None

    return True, "Valid image", img


def preprocess_for_inference(img: Image.Image, target_size: int = 224):
    """
    Transforms PIL Image to normalized PyTorch tensor shape (1, 3, target_size, target_size).
    Falls back to NumPy array if torch is unavailable.
    """
    # 1. Convert to RGB (handles RGBA, Grayscale, CMYK, Palette)
    if img.mode != "RGB":
        img = img.convert("RGB")

    if TORCH_AVAILABLE:
        transform_pipeline = transforms.Compose([
            transforms.Resize((target_size, target_size)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])
        tensor = transform_pipeline(img)
        # Add batch dimension: (1, 3, 224, 224)
        tensor = tensor.unsqueeze(0)
        return tensor
    else:
        # NumPy fallback preprocessing matching torchvision
        img_resized = img.resize((target_size, target_size), Image.Resampling.BILINEAR)
        arr = np.array(img_resized, dtype=np.float32) / 255.0
        # Normalize
        mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
        std = np.array([0.229, 0.224, 0.225], dtype=np.float32)
        arr = (arr - mean) / std
        # Transpose from (H, W, C) to (1, C, H, W)
        arr = np.transpose(arr, (2, 0, 1))
        arr = np.expand_dims(arr, axis=0)
        return arr
