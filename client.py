import os
from typing import Optional

import requests


class GeminiClient:
    """Minimal client for Google Gemini via REST generateContent API."""

    def __init__(self, api_key: Optional[str] = None, model: str = "gemini-1.5-flash") -> None:
        self.api_key = api_key or os.getenv("GEMINI_API_KEY", "")
        if not self.api_key:
            raise ValueError("Gemini API key not provided. Set GEMINI_API_KEY env var or pass api_key.")
        self.model = model
        self.base_url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent"

    def ask(self, prompt: str, max_output_tokens: int = 512) -> str:
        """Send a prompt and return the text response."""
        headers = {"Content-Type": "application/json"}
        params = {"key": self.api_key}
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"maxOutputTokens": max_output_tokens},
        }
        try:
            resp = requests.post(self.base_url, headers=headers, params=params, json=payload, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            # Extract first candidate text
            candidates = data.get("candidates", [])
            if not candidates:
                return "I couldn't generate a response."
            parts = candidates[0].get("content", {}).get("parts", [])
            if not parts:
                return "I couldn't generate a response."
            return parts[0].get("text", "I couldn't generate a response.")
        except Exception as exc:
            return f"Error contacting Gemini: {exc}"


