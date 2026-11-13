from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import ocr, explain
from app.config import Settings

settings = Settings()

app = FastAPI(title="ReportSaathi Backend")

# CORS (allow frontend dev server)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ocr.router, prefix="/ocr", tags=["OCR"])
app.include_router(explain.router, prefix="/explain", tags=["Explain"])
app.include_router(__import__('app.api.routes.reports', fromlist=['router']).router, prefix="", tags=["Reports"])
