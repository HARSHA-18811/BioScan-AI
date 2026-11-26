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

temp_dir = Path("backend/scripts/temp_eval_images")
temp_dir.mkdir(parents=True, exist_ok=True)

# 1. Test Money Plant with labelled filename
print("1. Testing Money Plant (filename: 'money_plant_specimen.jpg'):")
img = draw_realistic_biological_leaf("Money_Plant___healthy", 0)
p1 = temp_dir / "money_test1.jpg"
img.save(p1, quality=95)

code1, pred1 = upload_file("http://127.0.0.1:8000/predict", p1, "money_plant_specimen.jpg")
print(f"  -> Leaf Name:    {pred1['leaf_name']}")
print(f"  -> Scientific:   {pred1['pathological_details'].get('scientific_name')}")
print(f"  -> Family:       {pred1['pathological_details'].get('plant_family')}")
print(f"  -> Condition:    {pred1['condition_name']} (Confidence: {pred1['confidence']*100:.1f}%)")
print(f"  -> Organic Sol:  {pred1['pathological_details'].get('treatment_organic')[:60]}...")

# 2. Test Money Plant with camera filename (DSC_4021.jpg - no name in filename)
print("\n2. Testing Money Plant with Camera Filename (filename: 'DSC_4021.jpg'):")
code2, pred2 = upload_file("http://127.0.0.1:8000/predict", p1, "DSC_4021.jpg")
print(f"  -> Leaf Name:    {pred2['leaf_name']}")
print(f"  -> Scientific:   {pred2['pathological_details'].get('scientific_name')}")
print(f"  -> Family:       {pred2['pathological_details'].get('plant_family')}")
print(f"  -> Condition:    {pred2['condition_name']} (Confidence: {pred2['confidence']*100:.1f}%)")

# 3. Test Coffee leaf (ensure Coffee doesn't conflict)
print("\n3. Testing Coffee Leaf (filename: 'coffee_leaf.jpg'):")
c_img = draw_realistic_biological_leaf("Coffee___healthy", 0)
p2 = temp_dir / "coffee_test.jpg"
c_img.save(p2, quality=95)
code3, pred3 = upload_file("http://127.0.0.1:8000/predict", p2, "coffee_leaf.jpg")
print(f"  -> Leaf Name:    {pred3['leaf_name']}")
print(f"  -> Scientific:   {pred3['pathological_details'].get('scientific_name')}")
