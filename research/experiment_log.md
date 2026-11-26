# BioScan AI – Experimentation Log

## Experiment Log 001: Baseline Calibration Verification
- **Date & Time:** 2026-11-25T15:40:00Z
- **Objective:** Verify end-to-end functionality of dataset synthesis, loader splitting, forward/backward pass, and model checkpoint serialization.
- **Hardware Platform:** Local Host CPU (Intel/AMD x64 Architecture, Windows OS)
- **Model Architecture:** BioScan-LiteCNN (4-Block Conv2D + BatchNorm + ReLU + MaxPool + AdaptiveAvgPool)
- **Epochs:** 3
- **Batch Size:** 16
- **Initial Learning Rate:** 0.001 (Adam Optimizer)
- **Weight Decay:** 1e-4
- **Random Seed:** 42
- **Training Samples:** 60
- **Validation Samples:** 0 [Calibration run]
- **Test Samples:** 30
- **Final Training Loss:** 2.5682
- **Final Training Accuracy:** 8.33%
- **Evaluation Accuracy on Test Set:** 13.33%
- **Macro F1-Score:** 0.0343
- **Artifacts Generated:**
  - Weights: `backend/saved_models/bioscan_mobilenet.pth`
  - Classes: `backend/saved_models/classes.json`
  - Metrics: `backend/saved_models/evaluation_metrics.json`
  - Metadata: `backend/saved_models/model_metadata.json`
- **Observations:** PyTorch pipeline verified functional. Preprocessing, model serialization, database recording, and REST endpoints verified operational without errors.

---

## Experiment Log 002: Transfer Learning MobileNetV2 Full Dataset
- **Date & Time:** [TO BE FILLED AFTER EXPERIMENT]
- **Objective:** Train MobileNetV2 with pre-trained weights on complete 54k PlantVillage corpus.
- **Hardware Platform:** [TO BE FILLED - e.g., NVIDIA RTX / CUDA GPU]
- **Epochs:** [TO BE FILLED - Recommended 15-30]
- **Batch Size:** [TO BE FILLED - Recommended 32]
- **Optimizer:** AdamW / SGD with Cosine Annealing
- **Validation Accuracy Target:** [TO BE FILLED]
- **Test Macro F1 Target:** [TO BE FILLED]
- **Observations:** [TO BE FILLED AFTER EXPERIMENT]
