import logging

from motor.motor_asyncio import AsyncIOMotorClient
from ..core.config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from .mongodb import db

logger = logging.getLogger(__name__)


async def connect_to_mongo():
    db.client = AsyncIOMotorClient(str(MONGODB_URL),
                                   maxPoolSize=MAX_CONNECTIONS_COUNT,
                                   minPoolSize=MIN_CONNECTIONS_COUNT)
    logger.info(f"Connecting to mongoDB")


async def close_mongo_connection():
    db.client.close()
    logger.info(f"Closing to mongoDB")
