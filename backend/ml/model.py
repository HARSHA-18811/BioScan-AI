"""
Deep Learning Model Architecture for BioScan AI.
Provides:
1. MobileNetV2 with custom classification head for plant pathology.
2. BioScanLiteCNN: Lightweight multi-layer CNN for fast training/inference on CPU.
"""

import torch
import torch.nn as nn
import torchvision.models as models

class BioScanMobileNetV2(nn.Module):
    """
    MobileNetV2 Transfer Learning Architecture.
    Pre-trained feature extractor with custom classifier head and dropout for regularization.
    """
    def __init__(self, num_classes: int = 15, pretrained: bool = False, dropout_rate: float = 0.3):
        super(BioScanMobileNetV2, self).__init__()
        weights = models.MobileNet_V2_Weights.DEFAULT if pretrained else None
        base_model = models.mobilenet_v2(weights=weights)
        self.features = base_model.features
        
        in_features = base_model.classifier[1].in_features
        self.classifier = nn.Sequential(
            nn.Dropout(p=dropout_rate),
            nn.Linear(in_features, 256),
            nn.ReLU(inplace=True),
            nn.Dropout(p=dropout_rate),
            nn.Linear(256, num_classes)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.features(x)
        # Global Average Pooling
        x = nn.functional.adaptive_avg_pool2d(x, (1, 1))
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x


class BioScanLiteCNN(nn.Module):
    """
    Lightweight, fast-converging CNN architecture for biological image analysis.
    Designed specifically for quick training and inference without external weight dependencies.
    """
    def __init__(self, num_classes: int = 15):
        super(BioScanLiteCNN, self).__init__()
        self.features = nn.Sequential(
            # Block 1: 3 -> 32
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),  # 112x112

            # Block 2: 32 -> 64
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),  # 56x56

            # Block 3: 64 -> 128
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),  # 28x28

            # Block 4: 128 -> 256
            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.AdaptiveAvgPool2d((4, 4))
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Dropout(0.3),
            nn.Linear(256 * 4 * 4, 256),
            nn.ReLU(inplace=True),
            nn.Dropout(0.2),
            nn.Linear(256, num_classes)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.features(x)
        x = self.classifier(x)
        return x


def get_model(architecture: str = "mobilenet_v2", num_classes: int = 15, pretrained: bool = False) -> nn.Module:
    """Factory function to build the requested model."""
    if architecture.lower() in {"mobilenet", "mobilenet_v2", "mobilenetv2"}:
        return BioScanMobileNetV2(num_classes=num_classes, pretrained=pretrained)
    elif architecture.lower() in {"lite", "bioscan_lite", "lite_cnn"}:
        return BioScanLiteCNN(num_classes=num_classes)
    else:
        raise ValueError(f"Unsupported architecture: {architecture}")
