import io
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

import db.db as DataBase


vue_router = APIRouter()
