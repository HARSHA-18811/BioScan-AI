# BioScan AI – Results Table Template

| Run ID | Architecture | Dataset Split | Epochs | Batch Size | Learning Rate | Test Accuracy | Macro Precision | Macro Recall | Macro F1-Score |
|---|---|---|---|---|---|---|---|---|---|
| EXP-001 | BioScan-LiteCNN | Calibration Subset (N=30 test) | 3 | 16 | 0.001 | 13.33% | 0.0200 | 0.1333 | 0.0343 |
| EXP-002 | MobileNetV2 (Pre-trained) | Full PlantVillage (70/15/15) | [TO BE FILLED] | [TO BE FILLED] | [TO BE FILLED] | [TO BE FILLED] | [TO BE FILLED] | [TO BE FILLED] | [TO BE FILLED] |
| EXP-003 | ResNet50 (Baseline) | Full PlantVillage (70/15/15) | [TO BE FILLED] | [TO BE FILLED] | [TO BE FILLED] | [TO BE FILLED] | [TO BE FILLED] | [TO BE FILLED] | [TO BE FILLED] |

### Per-Class Performance Summary (Current Calibration Checkpoint)
| Class Name | Plant Species | Pathological Condition | Precision | Recall | F1-Score | Support |
|---|---|---|---|---|---|---|
| Apple___Apple_scab | Apple | Apple Scab | 0.0000 | 0.0000 | 0.0000 | 2 |
| Apple___Black_rot | Apple | Black Rot | 0.0000 | 0.0000 | 0.0000 | 2 |
| Apple___Cedar_apple_rust | Apple | Cedar Apple Rust | 0.0000 | 0.0000 | 0.0000 | 2 |
| Apple___healthy | Apple | Healthy | 0.0000 | 0.0000 | 0.0000 | 2 |
| Corn___Common_rust | Corn | Common Rust | 0.1333 | 1.0000 | 0.2353 | 2 |
| Corn___Northern_Leaf_Blight | Corn | Northern Leaf Blight | 0.0000 | 0.0000 | 0.0000 | 2 |
| Corn___healthy | Corn | Healthy | 0.0000 | 0.0000 | 0.0000 | 2 |
| Grape___Black_rot | Grape | Black Rot | 0.0000 | 0.0000 | 0.0000 | 2 |
| Grape___healthy | Grape | Healthy | 0.0000 | 0.0000 | 0.0000 | 2 |
| Potato___Early_blight | Potato | Early Blight | 0.0000 | 0.0000 | 0.0000 | 2 |
| Potato___Late_blight | Potato | Late Blight | 0.0000 | 0.0000 | 0.0000 | 2 |
| Potato___healthy | Potato | Healthy | 0.0000 | 0.0000 | 0.0000 | 2 |
| Tomato___Bacterial_spot | Tomato | Bacterial Spot | 0.0000 | 0.0000 | 0.0000 | 2 |
| Tomato___Early_blight | Tomato | Early Blight | 0.0000 | 0.0000 | 0.0000 | 2 |
| Tomato___healthy | Tomato | Healthy | 0.0000 | 0.0000 | 0.0000 | 2 |
