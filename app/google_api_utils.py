import requests

from app.config import settings


async def get_translation(word, target_language):
    url = "https://translation.googleapis.com/language/translate/v2"
    params = {"q": word, "target": target_language, "key": settings.GOOGLE_API_KEY}
    try:
        response = requests.get(url, params=params)
        return [
            trans["translatedText"] for trans in response.json()["data"]["translations"]
        ]
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
