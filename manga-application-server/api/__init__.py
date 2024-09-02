import io
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

import db.db as DataBase

from api.user_router import user_router
from api.title_router import title_router
from api.vue_router import vue_router
from api.tags_router import tags_router
from api.jenres_router import jenres_router
from api.comment_router import comment_router