import uuid
from pathlib import Path
from datetime import datetime, timezone
from fastapi import APIRouter, UploadFile, File, HTTPException, status
from ..config import settings
from ..schemas.analysis import AnalysisResponse, PredictionItem
from ..services.preprocessing import validate_image_bytes
from ..services.plant_knowledge import parse_class_name
from ..database.database import save_analysis
from ml.predict import predictor_instance

router = APIRouter(tags=["Inference"])

DISCLAIMER_TEXT = (
    "BioScan AI is an educational research prototype. Its predictions are not a substitute "
    "for expert plant pathology assessment. Model confidence is a statistical probability "
    "metric and does not equate to absolute diagnostic accuracy."
)

@router.post("/predict", response_model=AnalysisResponse)
async def predict_foliar_disease(file: UploadFile = File(...)):
    # 1. Validate file content type and size
    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No filename provided in upload payload."
        )

    # Read bytes safely
    try:
        contents = await file.read()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to read uploaded file: {str(e)}"
        )

    # 2. Strict validation (size, MIME, integrity)
    is_valid, error_msg, pil_img = validate_image_bytes(
        contents,
        max_bytes=settings.MAX_IMAGE_SIZE_BYTES
    )

    if not is_valid or pil_img is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error_msg
        )

    # 3. Verify Model Availability
    if not predictor_instance.is_ready():
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=(
                "Model weights are not loaded. A trained PyTorch model is required for real inference. "
                "Execute the training script (python backend/ml/train.py) or supply weights in backend/saved_models/."
            )
        )

    # 4. Perform Real AI Inference
    sanitized_filename = Path(file.filename).name  # Avoid exposing directory paths
    try:
        inference_result = predictor_instance.predict_image(pil_img, filename=sanitized_filename, top_k=3)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Model inference failed: {str(e)}"
        )
    analysis_id = str(uuid.uuid4())
    current_timestamp = datetime.now(timezone.utc).isoformat()

    top_items = [
        PredictionItem(
            class_name=p["class_name"],
            plant=p["plant"],
            leaf_name=p.get("leaf_name", f"{p['plant']} Leaf"),
            condition=p["condition"],
            confidence=p["confidence"],
            is_healthy=p["is_healthy"]
        )
        for p in inference_result["top_predictions"]
    ]

    # Scientific summary
    best_cls = inference_result["predicted_class"]
    parsed = parse_class_name(best_cls)
    if parsed["is_healthy"]:
        scientific_summary = (
            f"Specimen displays foliar morphology consistent with healthy {parsed['plant_name']} "
            f"({parsed.get('scientific_name', '')}). No characteristic lesions or chlorosis detected."
        )
    else:
        scientific_summary = (
            f"Specimen exhibits foliar lesion patterns consistent with {parsed['condition_name']} "
            f"in {parsed['plant_name']} ({parsed.get('scientific_name', '')}). "
            f"Primary pathogen category: {parsed.get('pathogen_type', 'Unknown')} "
            f"({parsed.get('causal_agent', 'N/A')})."
        )

    # 5. Persist analysis record in local SQLite database
    db_record = {
        "id": analysis_id,
        "image_filename": sanitized_filename,
        "plant_name": inference_result["plant_name"],
        "condition_name": inference_result["condition_name"],
        "predicted_class": inference_result["predicted_class"],
        "confidence": inference_result["confidence"],
        "top_predictions": [item.model_dump() for item in top_items],
        "model_name": predictor_instance.architecture.upper(),
        "model_version": settings.VERSION,
        "timestamp": current_timestamp,
        "status": "completed",
        "is_healthy": inference_result["is_healthy"]
    }
    try:
        save_analysis(db_record)
    except Exception as e:
        print(f"Warning: Failed to save record to database: {e}")

    return AnalysisResponse(
        id=analysis_id,
        image_filename=sanitized_filename,
        predicted_class=inference_result["predicted_class"],
        plant_name=inference_result["plant_name"],
        leaf_name=inference_result.get("leaf_name", f"{inference_result['plant_name']} Leaf"),
        condition_name=inference_result["condition_name"],
        confidence=inference_result["confidence"],
        is_healthy=inference_result["is_healthy"],
        top_predictions=top_items,
        scientific_summary=scientific_summary,
        pathological_details=parsed,
        model_name=f"BioScan-{predictor_instance.architecture.upper()}",
        model_version=settings.VERSION,
        timestamp=current_timestamp,
        disclaimer=DISCLAIMER_TEXT
    )
