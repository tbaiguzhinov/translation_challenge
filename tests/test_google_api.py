from unittest.mock import patch

import pytest

from app.google_api_utils import get_translation


@patch("app.google_api_utils.requests.get")
@pytest.mark.asyncio
async def test_get_translation_existing(mock_get):
    word = "apple"
    target_language = "es"
    cached_translation = {
        "word": word,
        "target": target_language,
        "translation": ["manzana"],
    }
    mock_get.return_value.json.return_value = {
        "data": {"translations": [{"translatedText": "manzana"}]}
    }
    mock_get.return_value.status_code = 200
    with patch(
        "app.google_api_utils.collection.find_one", return_value=cached_translation
    ):
        translation = await get_translation(word, target_language)
        assert translation == cached_translation["translation"]


@patch("app.google_api_utils.requests.get")
@pytest.mark.asyncio
async def test_get_translation_non_existing(mock_get):
    word = "apple"
    target_language = "es"
    mock_get.return_value.json.return_value = {
        "data": {"translations": [{"translatedText": "manzana"}]}
    }
    mock_get.return_value.status_code = 200
    with patch("app.google_api_utils.collection.find_one", return_value=None):
        translation = await get_translation(word, target_language)
        assert translation == ["manzana"]


@patch("app.google_api_utils.requests.get")
@pytest.mark.asyncio
async def test_get_translation_error(mock_get):
    word = "apple"
    target_language = "es"
    mock_get.side_effect = Exception("Some error occurred")
    with patch("app.google_api_utils.collection.find_one", return_value=None):
        translation = await get_translation(word, target_language)
        assert translation == []
