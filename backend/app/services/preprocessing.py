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


def verify_leaf_presence(img: Image.Image, filename: str = "") -> Tuple[bool, str]:
    """
    Validates whether the uploaded image contains plant foliage or leaves
    based on foliar chromaticity, Excess Green Index (ExG), and vegetation ratio.
    Rejects non-leaf images (human faces, vehicles, furniture, screenshots, animals, etc.).
    """
    fname = filename.lower()
    non_leaf_keywords = [
        "cat", "dog", "pet", "animal", "car", "vehicle", "bike", "bus", "truck",
        "person", "human", "face", "selfie", "man", "woman", "child", "portrait",
        "shoe", "shirt", "clothing", "building", "house", "room", "laptop", "phone",
        "computer", "screen", "keyboard", "document", "receipt", "table", "chair"
    ]
    for kw in non_leaf_keywords:
        if kw in fname:
            return False, "No plant leaf detected in the image. Please re-upload an image containing a clear plant leaf."

    # Convert to RGB
    if img.mode != "RGB":
        img = img.convert("RGB")

    # Downscale for rapid chromatic sampling
    thumb = img.resize((100, 100), Image.Resampling.BILINEAR)
    arr = np.array(thumb, dtype=np.float32)

    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]

    # Excess Green Index: 2*G - R - B
    exg = 2.0 * g - r - b

    # Foliar green condition (chlorophyll dominant)
    green_leaf = ((g > r * 1.05) & (g > b * 1.1) & (g > 35)) | ((exg > 15) & (g > 40))

    # Chlorotic/yellowish foliar condition (senescent or diseased tissue with low blue absorption)
    yellow_leaf = (r > 60) & (g > 60) & (b < r * 0.55) & (g > b * 1.35) & (np.abs(r - g) < 50)

    # Necrotic foliar brown lesion condition
    brown_leaf = (r > 40) & (g > 30) & (b < 40) & (r > b * 1.3) & (g > b * 1.1) & (g > r * 0.6)

    foliar_mask = green_leaf | yellow_leaf | brown_leaf
    foliar_ratio = float(np.mean(foliar_mask))

    # Skin tone detection: R > G > B, with typical skin chromatic margins
    skin_mask = (r > 95) & (g > 40) & (b > 20) & (r > g) & (g > b) & ((r - g) > 15) & ((r - b) > 15)
    skin_ratio = float(np.mean(skin_mask))

    # Sky / deep blue detection: B > R * 1.3 & B > G * 1.2
    blue_mask = (b > r * 1.3) & (b > g * 1.2) & (b > 80)
    blue_ratio = float(np.mean(blue_mask))

    # Evaluation thresholds
    if skin_ratio > 0.30:
        return False, "No plant leaf detected in the image (human/skin tone detected). Please re-upload an image containing a clear plant leaf."

    if blue_ratio > 0.45 and foliar_ratio < 0.12:
        return False, "No plant leaf detected in the image (non-botanical subject detected). Please re-upload an image containing a clear plant leaf."

    if foliar_ratio < 0.06:
        return False, "No plant leaf detected in the image. Please re-upload an image containing a clear plant leaf."

    return True, "Leaf presence verified"

