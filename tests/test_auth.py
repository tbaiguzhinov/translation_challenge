import pytest
from fastapi import HTTPException, status

from app.auth import verify_user
from app.db_utils import client as db_client

db = db_client["translation"]
collection = db["users"]


def setup_function():
    user = {"name": "test_user", "token": "valid_api"}
    if not collection.find_one({"name": "test_user"}):
        collection.insert_one(user)


setup_function()


def test_verify_user_valid_key():
    valid_api_key = "valid_api"
    result = verify_user(api_key_header=valid_api_key)
    assert result is not None
    assert result == "test_user"


def test_verify_user_invalid_key():
    invalid_api_key = "invalid_api_key"
    with pytest.raises(HTTPException) as exc_info:
        verify_user(api_key_header=invalid_api_key)
    assert exc_info.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert exc_info.value.detail == "Missing or invalid API key"


collection.delete_one({"name": "test_user"})
