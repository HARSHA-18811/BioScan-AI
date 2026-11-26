from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class PredictionItem(BaseModel):
    class_name: str
    plant: str
    leaf_name: Optional[str] = None
    condition: str
    confidence: float
    is_healthy: bool

class AnalysisResponse(BaseModel):
    id: str
    image_filename: str
    predicted_class: str
    plant_name: str
    leaf_name: Optional[str] = None
    condition_name: str
    confidence: float
    is_healthy: bool
    top_predictions: List[PredictionItem]
    scientific_summary: str
    pathological_details: Dict[str, Any]
    model_name: str
    model_version: str
    timestamp: str
    disclaimer: str

class HealthStatus(BaseModel):
    status: str
    model_loaded: bool
    model_name: Optional[str] = None
    model_version: Optional[str] = None
    num_supported_classes: int
    environment: str

class ClassInfo(BaseModel):
    class_id: int
    class_name: str
    plant: str
    condition: str
    is_healthy: bool
    scientific_name: Optional[str] = None

class ClassesResponse(BaseModel):
    count: int
    classes: List[ClassInfo]

class EvaluationMetrics(BaseModel):
    evaluated: bool
    model_architecture: Optional[str] = None
    dataset_name: Optional[str] = None
    test_samples: Optional[int] = None
    accuracy: Optional[float] = None
    macro_precision: Optional[float] = None
    macro_recall: Optional[float] = None
    macro_f1: Optional[float] = None
    weighted_f1: Optional[float] = None
    class_names: Optional[List[str]] = None
    per_class_metrics: Optional[Dict[str, Dict[str, float]]] = None
    confusion_matrix: Optional[List[List[int]]] = None
    evaluation_date: Optional[str] = None
    notes: Optional[str] = None
