from langchain.tools import tool
import requests

@tool
def translate_text(text: str) -> str:
    """
    Translate the given text to Hindi using LibreTranslate.
    """
    try:
        url = "https://libretranslate.com/translate"
        payload = {
            "q": text,
            "source": "en",
            "target": "hi",  # You can modify this for other target languages
            "format": "text"
        }
        headers = {"Content-Type": "application/json"}

        res = requests.post(url, json=payload, headers=headers)
        translated = res.json().get("translatedText", "❌ Failed to translate")
        return translated
    except Exception as e:
        return f"Error: {e}"
