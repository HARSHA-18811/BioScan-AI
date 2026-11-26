import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path
from PIL import Image

backend_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_dir))

from ml.dataset import draw_realistic_biological_leaf

# 1. Test /classes endpoint
print("1. Testing GET /classes...")
req = urllib.request.Request("http://127.0.0.1:8000/classes")
with urllib.request.urlopen(req, timeout=5) as response:
    status_code = response.getcode()
    data = json.loads(response.read().decode('utf-8'))

print(f"Status: {status_code}")
print(f"Total enrolled classes in live server: {data.get('count')}")
carrot_live = [c for c in data.get('classes', []) if 'Carrot' in c]
print(f"Carrot classes enrolled in live server: {carrot_live}")

# Helper for multipart form upload using urllib
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

# 2. Test /predict with Carrot Healthy
print("\n2. Testing POST /predict with Carrot Healthy Leaf...")
temp_carrot_path = Path("backend/scripts/temp_carrot.jpg")
test_carrot_img = draw_realistic_biological_leaf("Carrot___healthy", 0)
test_carrot_img.save(temp_carrot_path, quality=95)

status, pred_data = upload_file("http://127.0.0.1:8000/predict", temp_carrot_path, "carrot_healthy.jpg")
print(f"Status: {status}")
print("SUCCESSFUL PREDICTION RESPONSE:")
print(f"  1) Leaf Specimen Name: {pred_data.get('leaf_name')}")
print(f"     Host Plant:         {pred_data.get('plant_name')}")
print(f"     Scientific Host:    {pred_data.get('pathological_details', {}).get('scientific_name')}")
print(f"  2) Disease Diagnosed:  {pred_data.get('condition_name')} (Healthy: {pred_data.get('is_healthy')})")
print(f"     Pathogen:           {pred_data.get('pathological_details', {}).get('causal_agent')}")
print(f"     Confidence:         {pred_data.get('confidence') * 100:.1f}%")
print(f"  3) Treatments & Solutions:")
print(f"     - Organic:    {pred_data.get('pathological_details', {}).get('treatment_organic')}")
print(f"     - Chemical:   {pred_data.get('pathological_details', {}).get('treatment_chemical')}")
print(f"     - Prevention: {pred_data.get('pathological_details', {}).get('prevention_guide')}")

# 3. Test /predict with Carrot Alternaria Blight
print("\n3. Testing POST /predict with Carrot Alternaria Blight...")
temp_blight_path = Path("backend/scripts/temp_carrot_blight.jpg")
test_blight_img = draw_realistic_biological_leaf("Carrot___Alternaria_leaf_blight", 0)
test_blight_img.save(temp_blight_path, quality=95)

status_b, b_data = upload_file("http://127.0.0.1:8000/predict", temp_blight_path, "carrot_blight.jpg")
print(f"Status: {status_b}")
print("SUCCESSFUL BLIGHT PREDICTION RESPONSE:")
print(f"  1) Leaf Specimen Name: {b_data.get('leaf_name')}")
print(f"  2) Disease Diagnosed:  {b_data.get('condition_name')}")
print(f"     Causal Agent:       {b_data.get('pathological_details', {}).get('causal_agent')}")
print(f"  3) Solutions:")
print(f"     - Organic:  {b_data.get('pathological_details', {}).get('treatment_organic')}")
print(f"     - Chemical: {b_data.get('pathological_details', {}).get('treatment_chemical')}")
