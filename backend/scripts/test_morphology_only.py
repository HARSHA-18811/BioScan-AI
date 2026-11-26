import sys
import json
import urllib.request
from pathlib import Path

backend_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_dir))

from ml.dataset import draw_realistic_biological_leaf

# Draw a realistic Carrot leaf image
img = draw_realistic_biological_leaf("Carrot___healthy", 2)
temp_path = Path("backend/scripts/arbitrary_name_leaf.jpg")
img.save(temp_path, quality=95)

boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
with open(temp_path, 'rb') as f:
    file_bytes = f.read()

# Filename with NO plant name in it: e.g. "DSC_9941.jpg"
body = (
    f'--{boundary}\r\n'
    f'Content-Disposition: form-data; name="file"; filename="DSC_9941.jpg"\r\n'
    f'Content-Type: image/jpeg\r\n\r\n'
).encode('utf-8') + file_bytes + f'\r\n--{boundary}--\r\n'.encode('utf-8')

req = urllib.request.Request(
    "http://127.0.0.1:8000/predict",
    data=body,
    headers={'Content-Type': f'multipart/form-data; boundary={boundary}'},
    method='POST'
)
with urllib.request.urlopen(req, timeout=10) as resp:
    res = json.loads(resp.read().decode('utf-8'))

print("Visual-Only Morphology Test (filename: 'DSC_9941.jpg'):")
print(f"Predicted Leaf: {res.get('leaf_name')}")
print(f"Host Plant:     {res.get('plant_name')}")
print(f"Condition:      {res.get('condition_name')}")
print(f"Confidence:     {res.get('confidence') * 100:.2f}%")
print(f"Top 3 predictions:")
for p in res.get('top_predictions', []):
    print(f"  - {p['leaf_name']} ({p['condition']}): {p['confidence']*100:.1f}%")
