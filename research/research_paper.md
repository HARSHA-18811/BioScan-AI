# BioScan AI: Deep Learning-Driven Foliar Pathology Classification for Academic Botanical Diagnostics

**Authors:** [Student Name / Author Placeholder], [Advisor Name / Mentor Placeholder]  
**Affiliation:** [Department of Biology & Computer Science / Academic Institution Placeholder]  
**Date:** November 2026  
**Document Status:** Academic Research Draft / Experimental Milestone  

---

## Abstract

Automated foliar disease identification presents a significant technological opportunity to mitigate worldwide agricultural crop loss. In this experiential learning research project, we construct **BioScan AI**, a full-stack, modular, and reproducible computer vision system tailored for plant leaf pathology analysis. The system combines lightweight convolutional neural networks (incorporating MobileNetV2 depthwise separable architectures and lightweight multi-tier convolutional baselines) with an end-to-end web deployment stack using FastAPI, SQLite, and React. To ensure research integrity and eliminate optimistic bias, data splits are stratified with a deterministic random seed to prevent data leakage between training, validation, and test partitions. In this initial implementation, the system classifies 15 distinct foliar categories across five agricultural crops (*Malus domestica*, *Zea mays*, *Vitis vinifera*, *Solanum tuberosum*, and *Solanum lycopersicum*). We detail the preprocessing normalization pipeline, statistical softmax probability distribution analysis, empirical confusion matrix evaluation, and discuss why model confidence must not be conflated with diagnostic accuracy.

**Keywords:** Foliar Pathology, Convolutional Neural Networks, Transfer Learning, MobileNetV2, Data Leakage Prevention, Biological Computer Vision.

---

## 1. Introduction

Foliar infections caused by fungal pathogens (e.g., *Alternaria solani*, *Venturia inaequalis*, *Puccinia sorghi*), bacterial agents (*Xanthomonas spp.*), and oomycetes (*Phytophthora infestans*) account for substantial reductions in photosynthetic efficiency and global agricultural yields. Classical phytopathological diagnosis mandates on-site visual assessment by trained agronomists or laboratory microscopic isolation. In rural or resource-constrained farming environments, access to certified plant pathologists is limited, delaying interventions.

Recent advances in deep learning offer viable pathways toward automated foliar disease identification. However, many contemporary educational prototypes suffer from severe scientific deficits:
1. Fabricated simulated inferences presented to users as authentic model outputs;
2. Unacknowledged data leakage across training and test splits;
3. Conflation of model confidence with diagnostic accuracy;
4. Monolithic architectures incapable of accommodating additional biological modalities such as microscopy or genomics.

BioScan AI was developed as an academic experiential learning prototype to address these deficiencies, demonstrating how computer vision pipelines can be constructed with strict adherence to scientific reproducibility, decoupled full-stack design, and transparent empirical evaluation.

---

## 2. Materials and Dataset Preparation

### 2.1 Dataset Source and Target Flora
The primary benchmark utilized for model training and benchmarking is derived from the public **PlantVillage** dataset (Hughes and Salathé, 2015), released under the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) license. 

For the initial prototype implementation, a 15-class foliar pathology subset was designated across five major food and economic crops:
- **Apple (*Malus domestica*):** Apple Scab, Black Rot, Cedar Apple Rust, Healthy
- **Corn (*Zea mays*):** Common Rust, Northern Leaf Blight, Healthy
- **Grape (*Vitis vinifera*):** Black Rot, Healthy
- **Potato (*Solanum tuberosum*):** Early Blight, Late Blight, Healthy
- **Tomato (*Solanum lycopersicum*):** Bacterial Spot, Early Blight, Healthy

### 2.2 Data Leakage Mitigation and Stratified Splitting
To eliminate spatial and specimen leakage, data partitions are generated using stratified sampling with a locked pseudo-random seed (`seed=42`). The partition ratios are established as:
- **Training Partition:** 70%
- **Validation Partition:** 15%
- **Held-Out Test Partition:** 15%

Data augmentation transformations (random horizontal flips $p=0.5$, vertical flips $p=0.2$, rotational perturbations $\pm 15^\circ$, and color jitter $\pm 10\%$) are strictly applied during the training phase. The validation and test partitions remain completely unaugmented and deterministic.

---

## 3. Methodology and Architecture

### 3.1 Input Preprocessing Pipeline
Input foliar imagery is subjected to standardized image preprocessing:
1. **Header Validation:** File bytes are examined via PIL to confirm authentic JPEG/PNG image structure and detect corrupted bitstreams.
2. **Color Standardisation:** Images with extraneous channels (e.g., alpha channel in RGBA or CMYK print profiles) are converted to 3-channel sRGB.
3. **Spatial Rescaling:** Inputs are rescaled to a spatial dimension of $224 \times 224$ pixels using bilinear interpolation.
4. **Channel Normalization:** Pixel values are mapped to $[0.0, 1.0]$ and z-score normalized using ImageNet parameters:
   $$\mu = [0.485, 0.456, 0.406], \quad \sigma = [0.229, 0.224, 0.225]$$

### 3.2 Deep Learning Architectures
BioScan AI incorporates two complementary model backbones:
1. **BioScan-LiteCNN:** A lightweight 4-block convolutional network featuring batch normalization, ReLU activation, $2 \times 2$ max pooling, adaptive average pooling, and dropout regularization ($p=0.3$). This architecture requires zero external pre-trained weight downloads and converges rapidly on standard CPU infrastructure.
2. **BioScan-MobileNetV2:** A transfer learning architecture utilizing pre-trained inverted residual bottlenecks with linear activations and depthwise separable convolutions, capped with a custom two-stage dense classification head:
   $$\text{Classifier} = \text{Dropout}(0.3) \to \text{Linear}(1280 \to 256) \to \text{ReLU} \to \text{Dropout}(0.3) \to \text{Linear}(256 \to 15)$$

---

## 4. Experimental Results and Analysis

*Note: In accordance with academic honesty guidelines, empirical scores recorded below reflect the actual evaluation performed on the current test partition.*

### 4.1 Test Partition Performance Summary
- **Evaluation Dataset:** PlantVillage Foliar Pathology Subset
- **Evaluated Checkpoint:** `bioscan_mobilenet.pth`
- **Architecture:** BioScan-LiteCNN
- **Test Samples Evaluated ($N$):** 30
- **Overall Accuracy:** 13.33% [Calibration Phase]
- **Macro Precision:** 0.0200
- **Macro Recall:** 0.1333
- **Macro F1-Score:** 0.0343
- **Weighted F1-Score:** 0.0343

*Extended full-epoch benchmark results on full PlantVillage corpus (54,306 images):*
[TO BE FILLED AFTER MULTI-EPOCH GPU TRAINING ON COMPLETE DATASET]

### 4.2 Distinguishing Confidence from Diagnostic Accuracy
The application interface explicitly decouples model softmax confidence from accuracy:
$$P(\hat{y} = k \mid \mathbf{x}) = \frac{e^{z_k}}{\sum_{j=1}^{C} e^{z_j}}$$
A high posterior probability $P(\hat{y} = k \mid \mathbf{x}) > 0.90$ merely reflects relative activation magnitude within the closed label space and does not imply diagnostic ground truth, particularly in the presence of out-of-distribution leaf samples or novel physiological disorders.

---

## 5. System Implementation & Deployment

The complete application is structured into decoupled tiers:
- **Inference Engine & REST API:** Implemented in Python with FastAPI, Uvicorn, and PyTorch. Exposes `/health`, `/classes`, `/predict`, `/history`, and `/metrics`.
- **Relational Persistence:** SQLite database tracking analysis history, specimen metadata, timestamps, and model versions.
- **Scientific Research UI:** React, Vite, TypeScript, Tailwind CSS, Lucide icons, and Recharts, presenting real-time confusion matrices and probability distributions.

---

## 6. Limitations and Future Work

1. **Laboratory Setting Bias:** Current public datasets depict detached leaves photographed against neutral or black backdrops. Real field deployments face background soil and foliage clutter.
2. **Coinfection:** Multiple pathogens frequently coexist on single leaves; the current multiclass formulation assumes single-label mutually exclusive classifications.
3. **Future Extension:** Integrating Explainable AI (Grad-CAM heatmaps), microscopy cell segmentation, and genomics sequencing correlation.

---

## 7. Conclusion

BioScan AI provides an educational, research-oriented platform demonstrating genuine deep learning foliar analysis. By enforcing non-simulated predictions, transparent metric reporting, and modular architecture, it establishes a verifiable foundation for AI applications in plant pathology and agricultural biology.

---

## References

1. Hughes, D., & Salathé, M. (2015). An open access repository of images on plant health to enable the development of mobile disease diagnostics. *arXiv preprint arXiv:1511.08060*.
2. Sandler, M., Howard, A., Zhu, M., Zhmoginov, A., & Chen, L. C. (2018). MobileNetV2: Inverted Residuals and Linear Bottlenecks. *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 4510-4520.
3. Mohanty, S. P., Hughes, D. P., & Salathé, M. (2016). Using deep learning for image-based plant disease detection. *Frontiers in Plant Science*, 7, 1419.
