import certifi
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from app.config import settings

client = MongoClient(
    settings.MONGODB_URL, server_api=ServerApi("1"), tlsCAFile=certifi.where()
)

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
