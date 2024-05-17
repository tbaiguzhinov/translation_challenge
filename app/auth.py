from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

from app.db_utils import client

db = client["translation"]
collection = db["users"]


api_key_header = APIKeyHeader(name="X-API-Key")


def verify_user(api_key_header: str = Security(api_key_header)):
    if result := collection.find_one({"token": api_key_header}):
        user = result.get("name")
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing or invalid API key"
    )
