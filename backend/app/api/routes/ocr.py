from fastapi import APIRouter, File, UploadFile
from fastapi import HTTPException
from typing import Dict

router = APIRouter()

@router.post("/", response_model=Dict[str, str])
async def ocr_endpoint(file: UploadFile = File(...)):
    """Accept a PDF/JPG/PNG and return dummy extracted text.
    In a real implementation this would run Tesseract or pdfminer.
    """
    if file.content_type not in ["application/pdf", "image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Unsupported file type")
    # read file (ignored) – just simulate
    return {"text": "Sample extracted laboratory report text."}
