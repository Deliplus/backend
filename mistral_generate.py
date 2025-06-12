import requests

# replace with key from https://openrouter.ai/
OPENROUTER_API_KEY = "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"
MODEL = "mistralai/mistral-7b-instruct"

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
