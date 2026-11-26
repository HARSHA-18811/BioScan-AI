import json
from fastapi import APIRouter
from ..config import settings
from ..schemas.analysis import EvaluationMetrics

router = APIRouter(tags=["Metrics"])

@router.get("/metrics", response_model=EvaluationMetrics)
def get_metrics():
    metrics_path = settings.METRICS_PATH
    if not metrics_path.exists():
        return EvaluationMetrics(
            evaluated=False,
            notes="Not evaluated yet. Run 'python backend/ml/evaluate.py' to perform repeatable test-set evaluation."
        )

    try:
        with open(metrics_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return EvaluationMetrics(**data)
    except Exception as e:
        return EvaluationMetrics(
            evaluated=False,
            notes=f"Error reading evaluation metrics: {str(e)}"
        )
