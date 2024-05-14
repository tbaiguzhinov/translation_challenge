from fastapi import APIRouter

from app.db_utils import client
from app.models import Word

router = APIRouter()
db = client["translation"]


@router.get("/words/{word}", tags=["words"])
async def get_word(word: str, target: str = "es"):
    query = Word(word=word)
    result = await db.fetch_one(query)

    # Check if the word exists
    if result:
        # Word exists in the database
        # Add your logic here
        pass
    else:
        # Word does not exist in the database
        # Add your logic here
        pass

    return [{"word": word, "target": target}]


@router.get("/words/", tags=["words"])
async def get_words(
    username: str,
    page: int = 1,
    limit: int = 10,
    sort: str = None,
    filter_word: str = None,
):
    query = {}
    if filter_word:
        query["word"] = {"$regex": filter_word, "$options": "i"}
    if sort:
        query["$sort"] = sort

    skip = (page - 1) * limit
    words = await db.find(query).skip(skip).limit(limit).to_list(None)
    total_words = await db.count_documents(query)

    return {
        "username": username,
        "page": page,
        "limit": limit,
        "sort": sort,
        "filter_word": filter_word,
        "total_words": total_words,
        "words": words,
    }


@router.delete("/words/{word}", tags=["words"])
async def delete_word():
    return {"username": "fakecurrentuser"}
