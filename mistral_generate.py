import os
import requests

def mistral_translate(source_text):
    api_key = os.getenv("OPENROUTER_API_KEY")
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistral-7b-instruct",  # ✅ Make sure this model is available
        "messages": [
            {"role": "system", "content": "You are a professional translator. Translate to Catalan."},
            {"role": "user", "content": source_text}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("❌ Request failed:", e)
        print("📦 Response content:", response.text)
        raise

    return response.json()["choices"][0]["message"]["content"]
