from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from app.db_utils import client as db_client
from app.main import app
from app.models import Word
from app.routers.items import get_word

client = TestClient(app)
db = db_client["translation"]
collection = db["words"]


def setup_function():
    word = Word(
        word="apple",
        definitions={
            "noun": {
                "definitions": [
                    {
                        "definition": "a round fruit with red or green skin and firm white flesh",
                        "synonyms": [],
                        "examples": [],
                    }
                ]
            }
        },
        translations={"es": ["manzana"]},
    )
    if not collection.find_one({"word": "apple"}):
        collection.insert_one(word.model_dump())


def teardown_function():
    collection.delete_one({"word": "orange"})


setup_function()


@pytest.mark.asyncio
async def test_get_word_existing():
    response = await get_word("apple")
    assert response == Word(
        word="apple",
        definitions={
            "noun": {
                "definitions": [
                    {
                        "definition": "a round fruit with red or green skin and firm white flesh",
                        "synonyms": [],
                        "examples": [],
                    }
                ]
            }
        },
        translations={"es": ["manzana"]},
    )


@patch("app.google_api_utils.get_translation")
@patch("app.definition_utils.get_word_info")
@pytest.mark.asyncio
async def test_get_word_non_existing(mock_get_translation, mock_get_word_info):
    mock_get_translation.return_value = ["naranja"]
    mock_get_word_info.return_value = [
        {
            "noun": {
                "definition": [
                    "a round fruit with red or green skin and firm white flesh"
                ]
            }
        }
    ]
    response = await get_word("orange")
    response == Word(
        word="orange",
        definitions={
            "noun": {
                "definition": [
                    "a round fruit with red or green skin and firm white flesh"
                ]
            }
        },
        translations={"es": ["naranja"]},
    )


def test_delete_word_existing():
    response = client.delete("/api/words/apple")
    assert response.status_code == 200
    assert response.json() == {"message": "Word deleted successfully"}


def test_delete_word_non_existing():
    response = client.delete("/api/words/pear")
    assert response.status_code == 200
    assert response.json() == {"message": "Word not found"}
