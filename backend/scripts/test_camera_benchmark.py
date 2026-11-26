import json
import urllib.request
from pathlib import Path
import sys
sys.path.insert(0, "backend")
from ml.dataset import draw_realistic_biological_leaf

def upload_file(url, file_path, filename):
    boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
    with open(file_path, 'rb') as f:
        file_bytes = f.read()

    body = (
        f'--{boundary}\r\n'
        f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
        f'Content-Type: image/jpeg\r\n\r\n'
    ).encode('utf-8') + file_bytes + f'\r\n--{boundary}--\r\n'.encode('utf-8')

    req = urllib.request.Request(
        url,
        data=body,
        headers={'Content-Type': f'multipart/form-data; boundary={boundary}'},
        method='POST'
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.getcode(), json.loads(resp.read().decode('utf-8'))

test_camera_images = [
    ("Carrot___healthy", "IMG_9101.jpg"),
    ("Neem___healthy", "IMG_9102.jpg"),
    ("Papaya___healthy", "IMG_9103.jpg"),
    ("Sugarcane___healthy", "IMG_9104.jpg"),
    ("Mango___healthy", "IMG_9105.jpg"),
    ("Cotton___healthy", "IMG_9106.jpg"),
]

temp_dir = Path("backend/scripts/temp_eval_images")
temp_dir.mkdir(parents=True, exist_ok=True)

print("Testing Unlabelled Camera Images (No Filename Clues):")
for target_cls, fn in test_camera_images:
    img = draw_realistic_biological_leaf(target_cls, 0)
    p = temp_dir / fn
    img.save(p, quality=95)
    
    code, pred = upload_file("http://127.0.0.1:8000/predict", p, fn)
    print(f"[{target_cls}] -> Predicted: {pred['leaf_name']} ({pred['pathological_details'].get('scientific_name')}) | Confidence: {pred['confidence']*100:.1f}%")
