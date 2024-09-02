import io
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

import db.db as DataBase
import assets.image_funcs as ImageFuncs


default_pfp_path = 'assets/default/default_pfp.jpg'
with open(default_pfp_path, 'rb') as pfp:
    default_pfp = pfp.read()

user_router = APIRouter()



@user_router.get('/data/{user_id}')
async def user_data_read(user_id: int):
    user = DataBase.user_read(user_id)
    return {"id": user.id, "privilege_level": user.privilege_level, "display_name": user.display_name}

@user_router.get('/pfp/{user_id}')
async def user_pfp_read(user_id: int):
    user = DataBase.user_read(user_id)
    if user:
        pfp = ImageFuncs.get_user_pfp_bytes(user_id)
        return StreamingResponse(io.BytesIO(pfp), media_type="image/png")
    raise HTTPException(status_code=400, detail='user not found')