from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict

router = APIRouter()

class ExplainRequest(BaseModel):
    text: str

@router.post("/", response_model=Dict[str, str])
async def explain_endpoint(req: ExplainRequest):
    """Placeholder that pretends to call Gemini and returns a dummy explanation.
    In a real implementation this would forward the text to the Gemini API.
    """
    if not req.text:
        raise HTTPException(status_code=400, detail="Empty text")
    # Simple static demo response
    explanation = "This is a simulated plain‑language explanation of the laboratory report."
    return {"explanation": explanation}
