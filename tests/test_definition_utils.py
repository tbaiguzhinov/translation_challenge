from unittest.mock import patch

import pytest

from app.definition_utils import get_word_info


@pytest.mark.asyncio
async def test_get_word_info_error():
    word = "apple"
    with patch("app.definition_utils.requests.get") as mock_get:
        mock_get.side_effect = Exception("Error occurred")
        definitions = await get_word_info(word)
        assert definitions is None
