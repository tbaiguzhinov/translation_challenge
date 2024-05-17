import pytest

from app.db_utils import client as db_client


def setup_function():
    db = db_client["translation"]
    collection = db["words"]
    word = {
        "word": "apple",
        "definitions": {
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
        "translations": {"es": ["manzana"]},
    }
    if not collection.find_one({"word": "apple"}):
        collection.insert_one(word)


setup_function()


def test_ping():
    assert db_client.server_info()["ok"] == 1.0


def test_exception_handling():
    with pytest.raises(Exception):
        db_client.admin.command("invalid_command")
