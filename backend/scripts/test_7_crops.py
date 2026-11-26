import sys
from pathlib import Path
from PIL import Image
import numpy as np
import torch

backend_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_dir))

from ml.predict import BioScanPredictor, extract_biological_features, compute_biological_logits, gaussian_kernel
from ml.dataset import draw_realistic_biological_leaf
from app.services.preprocessing import preprocess_for_inference
from ml.config import config

predictor = BioScanPredictor()

test_cases = [
    ("Carrot___healthy", "DSC_001.jpg"),
    ("Carrot___Alternaria_leaf_blight", "DSC_002.jpg"),
    ("Mango___healthy", "DSC_003.jpg"),
    ("Potato___Early_blight", "DSC_004.jpg"),
    ("Apple___Apple_scab", "DSC_005.jpg"),
    ("Corn___Common_rust", "DSC_006.jpg"),
    ("Tomato___Bacterial_spot", "DSC_007.jpg"),
]

correct = 0
for cls_name, fn in test_cases:
    img = draw_realistic_biological_leaf(cls_name, 0)
    tensor = preprocess_for_inference(img, target_size=config.img_size)
    tensor = torch.from_numpy(tensor).to(predictor.device) if isinstance(tensor, np.ndarray) else tensor.to(predictor.device)
    with torch.no_grad():
        raw_logits = predictor.model(tensor)
        cnn_logits = raw_logits.squeeze(0).cpu().numpy()
    
    bio_features = extract_biological_features(img)
    bio_logits = compute_biological_logits(predictor.classes, bio_features, filename=fn)
    
    cnn_mean = float(np.mean(cnn_logits))
    cnn_std = float(np.std(cnn_logits)) + 1e-5
    norm_cnn = (cnn_logits - cnn_mean) / cnn_std

    fused = (bio_logits * 0.7) + (norm_cnn * 1.8)
    best_idx = int(np.argmax(fused))
    pred_cls = predictor.classes[best_idx]
    target_plant = cls_name.split("___")[0]
    pred_plant = pred_cls.split("___")[0]
    match = target_plant == pred_plant
    if match: correct += 1
    print(f"  [{cls_name}] -> Pred: {pred_cls} | Match: {match}")

print(f"\nFinal Result Across Crops: {correct}/{len(test_cases)} Passed!")
