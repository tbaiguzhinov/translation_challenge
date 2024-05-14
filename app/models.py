from pydantic import BaseModel


class Word(BaseModel):
    word: str
    definitions: str
    synonyms: str
    translations: dict
    examples: str
