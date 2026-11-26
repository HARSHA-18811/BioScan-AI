import sys
import json
import urllib.request
from pathlib import Path

backend_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_dir))

from ml.dataset import draw_realistic_biological_leaf

def test_upload(cls_name, dummy_filename):
    img = draw_realistic_biological_leaf(cls_name, 0)
    temp_path = Path(f"backend/scripts/temp_eval.jpg")
    img.save(temp_path, quality=95)

    boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
    with open(temp_path, 'rb') as f:
        file_bytes = f.read()

    body = (
        f'--{boundary}\r\n'
        f'Content-Disposition: form-data; name="file"; filename="{dummy_filename}"\r\n'
        f'Content-Type: image/jpeg\r\n\r\n'
    ).encode('utf-8') + file_bytes + f'\r\n--{boundary}--\r\n'.encode('utf-8')

    req = urllib.request.Request(
        "http://127.0.0.1:8000/predict",
        data=body,
        headers={'Content-Type': f'multipart/form-data; boundary={boundary}'},
        method='POST'
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode('utf-8'))

eval_suite = [
    ("Carrot___healthy", "IMG_0001.jpg"),
    ("Carrot___Alternaria_leaf_blight", "IMG_0002.jpg"),
    ("Mango___healthy", "IMG_0003.jpg"),
    ("Potato___Early_blight", "IMG_0004.jpg"),
    ("Apple___Apple_scab", "IMG_0005.jpg"),
    ("Corn___Common_rust", "IMG_0006.jpg"),
    ("Tomato___Bacterial_spot", "IMG_0007.jpg"),
]

print("Batch Multi-Crop Camera Image Evaluation (No Filename Hints):")
for target_cls, fn in eval_suite:
    res = test_upload(target_cls, fn)
    leaf = res.get('leaf_name')
    cond = res.get('condition_name')
    conf = res.get('confidence') * 100
    print(f"[{target_cls}] -> {leaf} | {cond} ({conf:.1f}%)")
