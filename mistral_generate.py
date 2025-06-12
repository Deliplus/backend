import requests
import os
# replace with key from https://openrouter.ai/
OPENROUTER_API_KEY = "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"
MODEL = "mistralai/mistral-7b-instruct"
api_key = os.getenv("OPENROUTER_API_KEY")
def mistral_translate(source_text: str) -> str:
    prompt = f"[ONLY RETURN CATALAN TRANSLATION, NO EXPLANATION]\nTranslate to CATALAN:\n{source_text}"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    body = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()
