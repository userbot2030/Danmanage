import asyncio
import sys
from motor import motor_asyncio
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from RitoRobot import MONGO_DB_URI


MONGO_DB_URI = "doadmin"


client = MongoClient()
client = MongoClient(MONGO_DB_URI, 27017)[MONGO_DB_URI]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI, 27017)
db = motor[MONGO_DB_URI]
db = client["doadmin"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(log.critical("Can't connect to mongodb! Exiting..."))
