# BioScan AI – REST API Specification

## Base URL
`http://127.0.0.1:8000`

---

### 1. Health Status
- **Method:** `GET`
- **Endpoint:** `/health`
- **Description:** Checks backend status, reports whether a trained model is loaded, model architecture, version, and supported class count.
- **Response `200 OK`:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "model_name": "BioScan-LiteCNN",
  "model_version": "1.0.0",
  "num_supported_classes": 15,
  "environment": "development/research"
}
```

---

### 2. Supported Classes
- **Method:** `GET`
- **Endpoint:** `/classes`
- **Description:** Returns the complete list of supported botanical categories and scientific metadata.
- **Response `200 OK`:**
```json
{
  "count": 15,
  "classes": [
    {
      "class_id": 0,
      "class_name": "Apple___Apple_scab",
      "plant": "Apple",
      "condition": "Apple Scab",
      "is_healthy": false,
      "scientific_name": "Malus domestica"
    }
  ]
}
```

---

### 3. Foliar Disease Inference
- **Method:** `POST`
- **Endpoint:** `/predict`
- **Content-Type:** `multipart/form-data`
- **Parameters:** `file` (Binary image file: JPEG/PNG, max 10MB)
- **Response `200 OK`:**
```json
{
  "id": "c76d2035-779d-472d-a2f0-e555772dd7ef",
  "image_filename": "sample_apple_scab.png",
  "predicted_class": "Apple___Apple_scab",
  "plant_name": "Apple",
  "condition_name": "Apple Scab",
  "confidence": 0.9421,
  "is_healthy": false,
  "top_predictions": [
    {
      "class_name": "Apple___Apple_scab",
      "plant": "Apple",
      "condition": "Apple Scab",
      "confidence": 0.9421,
      "is_healthy": false
    }
  ],
  "scientific_summary": "Specimen exhibits foliar lesion patterns consistent with Apple Scab...",
  "pathological_details": {
    "causal_agent": "Venturia inaequalis",
    "pathogen_type": "Fungal",
    "symptoms": "Olive-green to velvety dark brown lesions...",
    "pathology": "Ascospores overwinter in fallen dead leaves..."
  },
  "model_name": "BioScan-LITECNN",
  "model_version": "1.0.0",
  "timestamp": "2026-11-25T10:21:22.123456Z",
  "disclaimer": "BioScan AI is an educational research prototype..."
}
```

---

### 4. Analysis History
- **Method:** `GET`
- **Endpoint:** `/history`
- **Parameters:** `limit` (int, default 100)
- **Response `200 OK`:** Array of historical analysis objects.

- **Method:** `DELETE`
- **Endpoint:** `/history`
- **Response `200 OK`:** `{"message": "History cleared successfully", "deleted_records": 1}`

---

### 5. Evaluation Metrics
- **Method:** `GET`
- **Endpoint:** `/metrics`
- **Response `200 OK`:**
```json
{
  "evaluated": true,
  "model_architecture": "lite",
  "dataset_name": "PlantVillage Foliar Pathology Subset",
  "test_samples": 30,
  "accuracy": 0.1333,
  "macro_precision": 0.02,
  "macro_recall": 0.1333,
  "macro_f1": 0.0343,
  "weighted_f1": 0.0343,
  "class_names": [...],
  "per_class_metrics": {...},
  "confusion_matrix": [[...]]
}
```
*(If uncomputed, returns `{"evaluated": false, "notes": "Not evaluated yet..."}`)*
