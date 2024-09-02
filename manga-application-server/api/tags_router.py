from fastapi import APIRouter

import db.db as DataBase


tags_router = APIRouter()

@tags_router.get('/all')
async def user_data_read():
    tags = DataBase.read_tags()
    return tags