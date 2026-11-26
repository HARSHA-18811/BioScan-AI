import json
import urllib.request
from pathlib import Path

# 1. Test /classes endpoint
print("1. Testing GET /classes...")
req = urllib.request.Request("http://127.0.0.1:8000/classes")
with urllib.request.urlopen(req, timeout=5) as response:
    status_code = response.getcode()
    data = json.loads(response.read().decode('utf-8'))

total_classes = data.get('count', len(data.get('classes', [])))
print(f"Server Status: {status_code} | Total Enrolled Classes: {total_classes}")

plants_enrolled = set()
for c in data.get('classes', []):
    if isinstance(c, dict):
        plants_enrolled.add(c.get('plant'))
    else:
        plants_enrolled.add(c.split('___')[0])

print(f"Total Enrolled Plant Species: {len(plants_enrolled)}")
print(f"Species catalog: {sorted(list(plants_enrolled))}")

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

# Import dataset generator
import sys
sys.path.insert(0, "backend")
from ml.dataset import draw_realistic_biological_leaf

test_plants = [
    ("Neem___healthy", "neem_leaf.jpg"),
    ("Tulsi___healthy", "tulsi_leaf.jpg"),
    ("Papaya___healthy", "papaya_leaf.jpg"),
    ("Cotton___healthy", "cotton_leaf.jpg"),
    ("Sugarcane___healthy", "sugarcane_leaf.jpg"),
    ("Carrot___healthy", "carrot_specimen.jpg"),
    ("Mango___healthy", "mango_leaf.jpg"),
    ("Potato___Early_blight", "potato_early_blight.jpg")
]

print("\n2. Testing POST /predict on Expanded Catalog:")
temp_dir = Path("backend/scripts/temp_eval_images")
temp_dir.mkdir(parents=True, exist_ok=True)

for cls_name, fn in test_plants:
    img = draw_realistic_biological_leaf(cls_name, 0)
    p = temp_dir / fn
    img.save(p, quality=95)
    
    code, pred = upload_file("http://127.0.0.1:8000/predict", p, fn)
    leaf_name = pred.get('leaf_name')
    plant_name = pred.get('plant_name')
    cond_name = pred.get('condition_name')
    conf = pred.get('confidence') * 100
    sci_name = pred.get('pathological_details', {}).get('scientific_name', 'N/A')
    family = pred.get('pathological_details', {}).get('plant_family', 'N/A')
    org_sol = pred.get('pathological_details', {}).get('treatment_organic', '')[:50]
    
    print(f"\n[{cls_name} ({fn})]")
    print(f"  -> Leaf Name:    {leaf_name} ({sci_name})")
    print(f"  -> Family:       {family}")
    print(f"  -> Diagnosis:    {cond_name} (Confidence: {conf:.1f}%)")
    print(f"  -> Solution:     {org_sol}...")
