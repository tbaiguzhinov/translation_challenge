import requests

from app.config import settings
from app.db_utils import client
from app.models import Translation

db = client["translation"]
collection = db["translations"]


async def get_translation(word, target_language):
    cached_translation = collection.find_one({"word": word, "target": target_language})
    if cached_translation:
        cached_translation = Translation(**cached_translation)
        return cached_translation.translation

    url = "https://translation.googleapis.com/language/translate/v2"
    params = {"q": word, "target": target_language, "key": settings.GOOGLE_API_KEY}
    try:
        response = requests.get(url, params=params)
        translation = Translation(
            word=word,
            target=target_language,
            translation=[
                trans["translatedText"]
                for trans in response.json()["data"]["translations"]
            ],
        )
        collection.insert_one(translation.model_dump())
        return translation.translation

    except Exception as e:
        print(f"Error occurred: {e}")
        return []
