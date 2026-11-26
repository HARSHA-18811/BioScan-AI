import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from PIL import Image, ImageDraw
import numpy as np
from ml.predict import extract_biological_features

corn_rust = Image.new("RGB", (120, 360), color=(255, 255, 255))
d = ImageDraw.Draw(corn_rust)
d.polygon([(60, 10), (100, 100), (105, 260), (60, 350), (15, 260), (20, 100)], fill=(70, 150, 40))

grape_leaf = Image.new("RGB", (260, 240), color=(255, 255, 255))
d = ImageDraw.Draw(grape_leaf)
d.polygon([(130, 20), (190, 60), (240, 120), (190, 180), (130, 220), (70, 180), (20, 120), (70, 60)], fill=(45, 145, 55))

print("Corn features: ", extract_biological_features(corn_rust))
print("Grape features:", extract_biological_features(grape_leaf))
