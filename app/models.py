from typing import Optional

from pydantic import BaseModel


class Word(BaseModel):
    word: str
    translations: Optional[dict[str, list]]
    definitions: Optional[dict[str, dict[str, list]]]


class Translation(BaseModel):
    word: str
    target: str
    translation: list[str]
