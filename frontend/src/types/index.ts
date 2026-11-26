export interface HealthStatus {
  status: string;
  model_loaded: boolean;
  model_name?: string;
  model_version?: string;
  num_supported_classes: number;
  environment: string;
}

export interface ClassInfo {
  class_id: number;
  class_name: string;
  plant: string;
  condition: string;
  is_healthy: boolean;
  scientific_name?: string;
}

export interface ClassesResponse {
  count: number;
  classes: ClassInfo[];
}

export interface PredictionItem {
  class_name: string;
  plant: string;
  leaf_name?: string;
  condition: string;
  confidence: number;
  is_healthy: boolean;
}

export interface PathologicalDetails {
  class_name: string;
  plant_name: string;
  leaf_name?: string;
  condition_name: string;
  is_healthy: boolean;
  scientific_name?: string;
  plant_family?: string;
  pathogen_type?: string;
  causal_agent?: string;
  symptoms?: string;
  pathology?: string;
  treatment_organic?: string;
  treatment_chemical?: string;
  prevention_guide?: string[];
  immediate_actions?: string[];
  management_research?: string;
}

export interface AnalysisResponse {
  id: string;
  image_filename: string;
  predicted_class: string;
  plant_name: string;
  leaf_name?: string;
  condition_name: string;
  confidence: number;
  is_healthy: boolean;
  top_predictions: PredictionItem[];
  scientific_summary: string;
  pathological_details: PathologicalDetails;
  model_name: string;
  model_version: string;
  timestamp: string;
  disclaimer: string;
}

export interface HistoryRecord {
  id: string;
  image_filename: string;
  plant_name: string;
  condition_name: string;
  predicted_class: string;
  confidence: number;
  top_predictions: PredictionItem[];
  model_name: string;
  model_version: string;
  timestamp: string;
  status: string;
  is_healthy: boolean;
}

export interface PerClassMetric {
  precision: number;
  recall: number;
  f1_score: number;
  support: number;
}

export interface EvaluationMetrics {
  evaluated: boolean;
  model_architecture?: string;
  dataset_name?: string;
  test_samples?: number;
  accuracy?: number;
  loss?: number;
  macro_precision?: number;
  macro_recall?: number;
  macro_f1?: number;
  weighted_f1?: number;
  class_names?: string[];
  per_class_metrics?: Record<string, PerClassMetric>;
  confusion_matrix?: number[][];
  evaluation_date?: string;
  notes?: string;
}
