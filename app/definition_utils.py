import requests


async def get_word_info(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url)
        payload = response.json()
        definitions = {}
        for item in payload[0]["meanings"]:
            definitions[item["partOfSpeech"]] = {
                "definitions": [sub_item for sub_item in item["definitions"]],
                "synonyms": item["synonyms"],
            }
        return definitions
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
