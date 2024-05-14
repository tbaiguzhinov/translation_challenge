import requests


async def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url)
        translation = response.text
        return translation
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
