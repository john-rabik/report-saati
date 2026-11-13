import os
import httpx
from typing import List, Dict, Any
from pydantic import BaseModel

# Gemini endpoint – using the public generative language API (v1beta)
_GEMINI_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent"

class GeminiResult(BaseModel):
    test_name: str
    value: str | None = None
    unit: str | None = None
    reference_range: str | None = None
    explanation: str
    note: str | None = None

async def request_gemini(text: str, api_key: str) -> List[GeminiResult]:
    """Send extracted report text to Gemini and parse a structured JSON response.
    The function expects Gemini to return a JSON array of objects matching GeminiResult.
    If Gemini returns malformed JSON, a ValidationError will be raised and caught by the caller.
    """
    # Build the prompt that instructs Gemini to output exactly the JSON we need.
    system_prompt = (
        "You are a medical laboratory report summarizer. Extract each test from the given text and return a JSON array. "
        "Each object must contain the keys: test_name (string), value (string or null), unit (string or null), "
        "reference_range (string or null), explanation (plain‑language explanation, no medical advice), "
        "and note (optional, a short note when the information is missing or unclear). "
        "Do NOT invent any values, units, or reference ranges. If a field is not present in the source text, set it to null. "
        "If the report is ambiguous, include a note asking the user to consult a qualified clinician. "
        "Return ONLY the JSON array, no extra text."
    )

    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": text}]},
            {"role": "system", "parts": [{"text": system_prompt}]},
        ],
        "generationConfig": {"responseMimeType": "application/json"},
    }
    headers = {"Content-Type": "application/json"}
    url = f"{_GEMINI_ENDPOINT}?key={api_key}"
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.post(url, json=payload, headers=headers)
        resp.raise_for_status()
        data = resp.json()
        # The response format from Gemini is {"candidates": [{"content": {"parts": [{"text": "..."}]}}]}
        try:
            raw_text = data["candidates"][0]["content"]["parts"][0]["text"]
            # Parse the JSON array from the raw text
            parsed = httpx.loads(raw_text) if isinstance(raw_text, str) else raw_text
        except Exception as e:
            raise ValueError(f"Failed to parse Gemini response: {e}")
        # Validate each entry against GeminiResult model
        results: List[GeminiResult] = []
        for item in parsed:
            try:
                result = GeminiResult(**item)
                results.append(result)
            except Exception as ve:
                # Skip malformed entries but keep processing
                continue
        return results
