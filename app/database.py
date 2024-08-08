from app.config import settings
from pymongo import MongoClient

client = MongoClient(settings.mongo_connection_string)
db = client[settings.database_name]