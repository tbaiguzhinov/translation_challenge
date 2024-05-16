from fastapi import APIRouter

from app.db_utils import client
from app.definition_utils import get_word_info
from app.google_api_utils import get_translation
from app.models import Word

router = APIRouter()
db = client["translation"]
collection = db["words"]


@router.get("/words/{word}", tags=["words"])
async def get_word(word: str, target: str = "es"):
    query = {"word": word.lower()}
    result = collection.find_one(query)

    if result:
        word = Word(**result)
    else:
        defintions = await get_word_info(word)
        word = Word(
            word=word.lower(),
            definitions=defintions,
            translations={},
        )
        collection.insert_one(word.model_dump())

    if target not in word.translations:
        word.translations[target] = await get_translation(
            word.word, target_language=target
        )
        collection.update_one(query, {"$set": word.model_dump()})

    word.translations = {target: word.translations[target]}
    return word


@router.delete("/words/{word}", tags=["words"])
async def delete_word(word: str):
    query = {"word": word.lower()}
    result = collection.delete_one(query)
    if not result.deleted_count:
        return {"message": "Word not found"}
    return {"message": "Word deleted successfully"}


@router.get("/words/", tags=["words"])
async def get_words(
    page: int = 1,
    limit: int = 10,
    sort: str = None,
    filter_word: str = None,
    include_details: bool = False,
):
    query = {}
    if filter_word:
        query["word"] = {"$regex": filter_word, "$options": "i"}
    if sort:
        query["$sort"] = sort

    skip = (page - 1) * limit
    words = list(collection.find(query).skip(skip).limit(limit))
    total_words = collection.count_documents(query)

    if not include_details:
        words = [word["word"] for word in words]
    else:
        words = [Word(**word) for word in words]

    return {
        "page": page,
        "limit": limit,
        "sort": sort,
        "filter_word": filter_word,
        "total_words": total_words,
        "words": words,
    }
