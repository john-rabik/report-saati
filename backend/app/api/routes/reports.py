import os
import shutil
import uuid
from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Literal

from app.core import ocr as ocr_utils

router = APIRouter()

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB
ALLOWED_TYPES = {
    "application/pdf": "pdf",
    "image/jpeg": "jpg",
    "image/png": "png",
}

class AnalyzeResponse(BaseModel):
    status: Literal["success", "error"]
    filename: str | None = None
    text: str | None = None
    detail: str | None = None

def _validate_upload(file: UploadFile):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Unsupported file type")
    # FastAPI streams the file; we need to check size after reading to temp
    return ALLOWED_TYPES[file.content_type]

@router.post("/api/reports/analyze", response_model=AnalyzeResponse)
async def analyze_report(file: UploadFile = File(...)):
    """Accept a PDF/JPG/PNG, extract raw text and return it.
    The file is written to a temporary location that is deleted after processing.
    """
    # Validation of type
    ext = _validate_upload(file)
    # Write to a safe temporary file
    tmp_dir = os.path.join(os.getcwd(), "tmp")
    os.makedirs(tmp_dir, exist_ok=True)
    tmp_name = f"{uuid.uuid4()}.{ext}"
    tmp_path = os.path.join(tmp_dir, tmp_name)
    try:
        with open(tmp_path, "wb") as out_fp:
            size = 0
            while content := await file.read(1024 * 64):
                size += len(content)
                if size > MAX_FILE_SIZE:
                    raise HTTPException(status_code=413, detail="File too large (max 5 MB)")
                out_fp.write(content)
        # Extract text according to file type
        if ext == "pdf":
            text = ocr_utils.extract_text_from_pdf(tmp_path)
            if not text.strip():
                # fallback to OCR on first page if pdfminer found nothing
                text = ocr_utils.ocr_pdf(tmp_path)
        else:
            text = ocr_utils.extract_text_from_image(tmp_path)
        if not text:
            return AnalyzeResponse(status="error", filename=file.filename, text="", detail="No readable text found")
        return AnalyzeResponse(status="success", filename=file.filename, text=text)
    finally:
        # Cleanup temporary file safely
        try:
            os.remove(tmp_path)
        except FileNotFoundError:
            pass
