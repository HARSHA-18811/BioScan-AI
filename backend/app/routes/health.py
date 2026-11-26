from fastapi import APIRouter
from ..config import settings
from ..schemas.analysis import HealthStatus
from ml.predict import predictor_instance

router = APIRouter(tags=["Health"])

@router.get("/health", response_model=HealthStatus)
def get_health():
    is_ready = predictor_instance.is_ready()
    return HealthStatus(
        status="healthy",
        model_loaded=is_ready,
        model_name="BioScan-LiteCNN" if is_ready else None,
        model_version=settings.VERSION,
        num_supported_classes=len(predictor_instance.classes),
        environment="development/research"
    )
