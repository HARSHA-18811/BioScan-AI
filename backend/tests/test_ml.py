import sys
from pathlib import Path
from PIL import Image
import torch

backend_dir = Path(__file__).resolve().parent.parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

from ml.model import get_model
from ml.dataset import scan_and_split_dataset
from app.services.preprocessing import preprocess_for_inference, validate_image_bytes

def test_model_forward_pass():
    model = get_model(architecture="lite", num_classes=15)
    model.eval()
    dummy_input = torch.randn(1, 3, 224, 224)
    with torch.no_grad():
        out = model(dummy_input)
    assert out.shape == (1, 15), f"Expected shape (1, 15), got {out.shape}"

def test_image_preprocessing():
    # Create test image in RGBA
    img = Image.new("RGBA", (300, 400), color=(100, 150, 200, 255))
    tensor = preprocess_for_inference(img, target_size=224)
    assert isinstance(tensor, torch.Tensor)
    assert tensor.shape == (1, 3, 224, 224), f"Expected tensor shape (1, 3, 224, 224), got {tensor.shape}"

def test_image_validation_rejection():
    # Non-image data
    corrupt_bytes = b"this is not an image file header"
    is_valid, msg, img = validate_image_bytes(corrupt_bytes)
    assert is_valid is False
    assert img is None
    assert "Corrupted or invalid" in msg or "Unsupported format" in msg
