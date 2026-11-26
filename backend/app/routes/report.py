import os
from pathlib import Path
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, PlainTextResponse, JSONResponse

router = APIRouter(prefix="/report", tags=["Research Report"])

# Root is one level up from backend
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
OVERLEAF_DIR = PROJECT_ROOT / "research" / "overleaf"
ZIP_PATH = OVERLEAF_DIR / "BioScan_AI_Overleaf.zip"
TEX_PATH = OVERLEAF_DIR / "main.tex"
INSTRUCTIONS_PATH = OVERLEAF_DIR / "OVERLEAF_INSTRUCTIONS.md"
PDF_PATH = PROJECT_ROOT / "research" / "BioScan_AI_Research_Report.pdf"

@router.get("/info")
def get_report_info():
    """Returns metadata about the research report and Overleaf bundle."""
    return {
        "title": "BioScan AI: A Reproducible Deep Learning Architecture for Automated Foliar Pathology Diagnosis and Biological Image Analysis",
        "format": "Academic Research & Experiential Learning Report (Standard Non-IEEE Format)",
        "target_pages": "8-9 Pages",
        "figures_count": 8,
        "tables_count": 4,
        "algorithms_count": 1,
        "references_count": 24,
        "classes_count": 15,
        "latex_file_exists": TEX_PATH.exists(),
        "zip_file_exists": ZIP_PATH.exists(),
        "pdf_file_exists": PDF_PATH.exists(),
        "pdf_size_bytes": PDF_PATH.stat().st_size if PDF_PATH.exists() else 0,
        "zip_size_bytes": ZIP_PATH.stat().st_size if ZIP_PATH.exists() else 0,
        "compiler": "pdfLaTeX / ReportLab Native Engine",
        "tex_distribution": "TeX Live / Overleaf Standard"
    }

@router.get("/pdf")
def download_compiled_pdf():
    """Serves the compiled 8-page academic research report PDF directly."""
    if not PDF_PATH.exists():
        raise HTTPException(status_code=404, detail="Compiled PDF report not found.")
    return FileResponse(
        path=str(PDF_PATH),
        filename="BioScan_AI_Research_Report.pdf",
        media_type="application/pdf",
        headers={"Content-Disposition": "inline; filename=BioScan_AI_Research_Report.pdf"}
    )

@router.get("/latex", response_class=PlainTextResponse)
def get_latex_source():
    """Returns the complete LaTeX source of the research report for one-click copy."""
    if not TEX_PATH.exists():
        raise HTTPException(status_code=404, detail="LaTeX source file main.tex not found.")
    try:
        with open(TEX_PATH, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read LaTeX source: {str(e)}")

@router.get("/download")
def download_overleaf_zip():
    """Serves the complete pre-packaged Overleaf zip archive for direct download."""
    if not ZIP_PATH.exists():
        raise HTTPException(status_code=404, detail="Overleaf zip package not found.")
    return FileResponse(
        path=str(ZIP_PATH),
        filename="BioScan_AI_Overleaf.zip",
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=BioScan_AI_Overleaf.zip"}
    )

@router.get("/instructions", response_class=PlainTextResponse)
def get_overleaf_instructions():
    """Returns step-by-step instructions for compiling in Overleaf."""
    if not INSTRUCTIONS_PATH.exists():
        raise HTTPException(status_code=404, detail="Overleaf instructions not found.")
    try:
        with open(INSTRUCTIONS_PATH, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read instructions: {str(e)}")
