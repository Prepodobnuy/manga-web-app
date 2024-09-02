from fastapi import APIRouter

import db.db as DataBase


jenres_router = APIRouter()

@jenres_router.get('/all')
async def user_data_read():
    jenres = DataBase.read_jenres()
    return jenres