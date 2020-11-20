from pymongo import MongoClient
from config import mongo_url

client = MongoClient(mongo_url)
db = client['discord']


def create_guild_if_new(guild):
    collection = db['guilds']
    collection.update_one(
        {'_id': guild['_id']},
        {'$setOnInsert': guild},
        upsert=True
    )
