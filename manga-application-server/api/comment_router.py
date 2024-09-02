import io
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

import db.db as DataBase


class Comment(BaseModel):
    id: int
    rating: int
    publish_date: str
    caption: str
    publisher_id: int
    parent_comment_id: int|None
    title_id: int|None
    page: int|None

comment_router = APIRouter()

@comment_router.get('/data/{comment_id}', response_model=Comment)
async def comment_data_read(comment_id: int):
    comment = DataBase.comment_read(comment_id)
    return {
        "id": comment.id, 
        "rating": comment.rating, 
        "publish_date": comment.publish_date,
        "caption": comment.caption,
        "publisher_id": comment.publisher_id,
        "parent_comment_id": comment.parent_comment_id,
        "title_id": comment.title_id,
        "page": comment.page
        }

@comment_router.post('/new')
async def comment_new(comment: Comment):
    DataBase.comment_create(comment.caption, comment.publisher_id, comment.parent_comment_id, comment.title_id, comment.page)