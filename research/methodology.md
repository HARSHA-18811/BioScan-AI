# BioScan AI – Research Methodology Specification

## 1. Research Protocol Overview
This document specifies the exact empirical pipeline implemented in BioScan AI for reproducible training, image processing, model evaluation, and inference.

```
+-------------------------------------------------------------+
|                Biological Specimen Capture                  |
|                 (Raw Foliar Leaf Image)                     |
+-------------------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|                   Image Sanitization & PIL                  |
|     - Size boundary check (<= 10MB)                         |
|     - Format verification (JPEG / PNG)                      |
|     - Multi-channel conversion to 3-channel RGB             |
+-------------------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|               Tensor Normalization Pipeline                 |
|     - Bilinear interpolation to 224 x 224                   |
|     - Pixel scaling to [0.0, 1.0]                           |
|     - ImageNet z-score normalization (mean, std)            |
+-------------------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|               Deep Convolutional Inference                  |
|     - Model: MobileNetV2 / BioScanLiteCNN                   |
|     - Spatial feature maps -> Global Avg Pool               |
|     - Dense Classification Head -> Logits                   |
|     - Softmax activation -> Class probabilities             |
+-------------------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|               Structured Diagnostic Report                  |
|     - Top-1 & Top-K candidates                              |
|     - Pathological details (etiology, pathogen, symptoms)   |
|     - Statistical confidence vs diagnostic accuracy note    |
|     - SQLite audit persistence                              |
+-------------------------------------------------------------+
```

## 2. Dataset Partitioning Protocol
- **Stratified Partitioning:** Splitting is carried out on a per-class basis to maintain equal class representations across splits.
- **Random Seed:** A fixed seed of `42` is set across Python `random`, NumPy, and PyTorch (`torch.manual_seed(42)`).
- **Leakage Prevention:** Augmentations are applied strictly during runtime inside `train_loader`. No augmented duplicates are stored on disk or present in test evaluation.

## 3. Mathematical Evaluation Formulations

### Accuracy
$$\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}$$

### Precision (Positive Predictive Value)
$$\text{Precision}_c = \frac{\text{TP}_c}{\text{TP}_c + \text{FP}_c}$$

### Recall (Sensitivity)
$$\text{Recall}_c = \frac{\text{TP}_c}{\text{TP}_c + \text{FN}_c}$$

### F1-Score
$$F_1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$$

### Macro-Averaging
$$\text{Macro } F_1 = \frac{1}{C} \sum_{c=1}^{C} F_{1, c}$$
