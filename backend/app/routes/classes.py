from fastapi import APIRouter
from ..schemas.analysis import ClassesResponse, ClassInfo
from ..services.plant_knowledge import parse_class_name
from ml.predict import predictor_instance

router = APIRouter(tags=["Classes"])

@router.get("/classes", response_model=ClassesResponse)
def get_classes():
    classes_list = predictor_instance.classes
    info_list = []
    for i, cls_name in enumerate(classes_list):
        parsed = parse_class_name(cls_name)
        info_list.append(ClassInfo(
            class_id=i,
            class_name=cls_name,
            plant=parsed["plant_name"],
            condition=parsed["condition_name"],
            is_healthy=parsed["is_healthy"],
            scientific_name=parsed.get("scientific_name")
        ))
    return ClassesResponse(count=len(info_list), classes=info_list)
