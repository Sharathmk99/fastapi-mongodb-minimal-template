from ..db.mongodb import AsyncIOMotorClient
from ..core.config import database_name, demo_collection_name
from ..models.demo import Demo
from typing import List


async def get_demo(
        conn: AsyncIOMotorClient) -> List[Demo]:
    demo_doc = conn[database_name][demo_collection_name].find({})
    demo_array = []
    async for row in demo_doc:
        demo_array.append(Demo(**row))
    return demo_array
