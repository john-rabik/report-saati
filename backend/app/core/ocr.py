import os
from typing import Optional

from pdfminer.high_level import extract_text as pdf_extract_text
from pdfminer.pdfparser import PDFSyntaxError

import pytesseract
from PIL import Image

# Helper to extract text from a PDF using pdfminer
def extract_text_from_pdf(pdf_path: str) -> str:
    """Return the raw text extracted from a PDF.
    If pdfminer fails (e.g., scanned PDF), returns an empty string.
    """
    try:
        return pdf_extract_text(pdf_path) or ""
    except PDFSyntaxError:
        return ""
    except Exception as e:
        # Log could be added later
        return ""

# OCR fallback for PDFs (convert first page to image via pdf2image would be ideal,
# but to keep dependencies light we simply return empty – the API will try OCR
# only for image uploads.)
def ocr_pdf(pdf_path: str) -> str:
    """Placeholder: In a full implementation we would rasterise the PDF and run OCR.
    For now we return an empty string to indicate no OCR path.
    """
    return ""

def extract_text_from_image(image_path: str) -> str:
    """Run Tesseract OCR on an image file and return the plain text.
    Assumes the `tesseract` binary is on PATH or pointed to by the TESSERACT_CMD env.
    """
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text or ""
    except Exception as e:
        # In production we would log the error
        return ""
