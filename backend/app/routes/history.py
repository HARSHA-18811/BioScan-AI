from typing import List, Dict, Any
from fastapi import APIRouter
from ..database.database import get_all_analyses, clear_all_history

router = APIRouter(tags=["History"])

@router.get("/history", response_model=List[Dict[str, Any]])
def get_history(limit: int = 100):
    return get_all_analyses(limit=limit)

@router.delete("/history")
def clear_history():
    deleted_count = clear_all_history()
    return {"message": "History cleared successfully", "deleted_records": deleted_count}
