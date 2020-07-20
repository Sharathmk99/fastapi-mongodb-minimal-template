from fastapi import APIRouter, Depends
from ....db.mongodb import AsyncIOMotorClient, get_database
from ....models.demo import Demo
from ....crud.demo import get_demo
from typing import List

router = APIRouter()


@router.get("/demo", response_model=List[Demo], tags=["demo"])
async def get_articles(db: AsyncIOMotorClient = Depends(get_database)) -> List[Demo]:
    demo = await get_demo(db)
    return demo
