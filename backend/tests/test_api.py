import io
import sys
from pathlib import Path
from PIL import Image
from fastapi.testclient import TestClient

backend_dir = Path(__file__).resolve().parent.parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

from app.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "healthy"
    assert "model_loaded" in data
    assert data["num_supported_classes"] >= 15

def test_classes_endpoint():
    response = client.get("/classes")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] >= 15
    assert len(data["classes"]) >= 15
    first_cls = data["classes"][0]
    assert "class_name" in first_cls
    assert "plant" in first_cls
    assert "condition" in first_cls

def test_metrics_endpoint():
    response = client.get("/metrics")
    assert response.status_code == 200
    data = response.json()
    assert "evaluated" in data

def test_invalid_image_upload_rejected():
    # Submit text payload disguised as image
    fake_file = io.BytesIO(b"MALFORMED_FAKE_PAYLOAD_NOT_IMAGE")
    response = client.post(
        "/predict",
        files={"file": ("fake.jpg", fake_file, "image/jpeg")}
    )
    assert response.status_code == 400
    assert "Corrupted or invalid image" in response.json()["detail"]

def test_valid_image_prediction():
    # Generate real JPEG image
    img = Image.new("RGB", (224, 224), color=(34, 139, 34))
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format="JPEG")
    img_bytes = img_byte_arr.getvalue()

    response = client.post(
        "/predict",
        files={"file": ("leaf_test.jpg", io.BytesIO(img_bytes), "image/jpeg")}
    )
    assert response.status_code == 200
    data = response.json()
    assert "predicted_class" in data
    assert "confidence" in data
    assert "top_predictions" in data
    assert len(data["top_predictions"]) > 0
    assert "disclaimer" in data
    assert "BioScan AI is an educational research prototype" in data["disclaimer"]
