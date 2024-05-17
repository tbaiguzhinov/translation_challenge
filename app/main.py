from fastapi import Depends, FastAPI

from app.auth import verify_user
from app.config import settings
from app.routers.items import router

app = FastAPI()

if settings.AUTHENTICATION:
    app.include_router(router, prefix="/api", dependencies=[Depends(verify_user)])
else:
    app.include_router(router, prefix="/api")
