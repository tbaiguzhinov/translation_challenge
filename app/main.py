from fastapi import FastAPI

from app.definition_utils import get_definition

app = FastAPI()


@app.get("/")
async def root():
    # result = await get_translation("Hello, World!", "es")
    result = await get_definition("hello")
    return {"message": result}
