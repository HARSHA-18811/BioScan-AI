import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

import torch
import torchvision.models as models
from torchvision import transforms
from PIL import Image
import numpy as np

# Load pretrained MobileNetV2
mobilenet = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)
mobilenet.eval()
feature_extractor = mobilenet.features

tf = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

print("MobileNetV2 feature extractor initialized successfully.")
