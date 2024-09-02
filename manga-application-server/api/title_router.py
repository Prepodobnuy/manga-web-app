import io
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

import db.db as DataBase
import db.entities as Entities
import assets.image_funcs as ImageFuncs


class NewTitleData(BaseModel):
    age_rating: str = Field(example="0+")
    ru_name: str = Field(example="string")
    en_name: str = Field(example="string")
    alternative_names: str = Field(example="string")
    release_year: str = Field(example="string")
    description: str = Field(example="string")
    status: str = Field(example="string")
    translate_status: str = Field(example="string")
    franchise: str = Field(example="string")
    author: str = Field(example="string")
    artist: str = Field(example="string")
    publisher: str = Field(example="string")

class ReadTitles(BaseModel):
    read_from: int       = Field(example=0)
    read_to: int         = Field(example=50)
    filter_by: int       = Field(examples=["rating", "views"])
    reverse: bool        = Field(example=True)
    tags_include: list   = Field(example=[0, 1, 2])
    tags_exclude: list   = Field(example=[3, 4, 5])
    jenres_include: list = Field(example=[0, 1, 2])
    jenres_exclude: list = Field(example=[3, 4, 5])
    text_prompt: str     = Field(example="Человек бензопила")

title_router = APIRouter()

@title_router.get('/data/{title_id}')
async def title_read(title_id: int):
    title = DataBase.title_read(title_id)
    return {
        "id": title.id,
        "age_rating": title.age_rating,
        "ru_name": title.ru_name,
        "en_name": title.en_name,
        "alternative_names": title.alternative_names,
        "release_year": title.release_year,
        "description": title.description,
        "status": title.status,
        "approve_status": title.approve_status,
        "translate_status": title.translate_status,
        "franchise": title.franchise,
        "author": title.author,
        "artist": title.artist,
        "publisher": title.publisher
        }

@title_router.get('/previewpic/{title_id}')
async def title_preview_read(title_id: int):
    title = DataBase.title_read(title_id)
    if title:
        preview = ImageFuncs.get_title_preview_bytes(title_id)
        return StreamingResponse(io.BytesIO(preview), media_type="image/png")
    raise HTTPException(status_code=400, detail='title not found')

@title_router.post('/new-title')
async def title_new(title_data: NewTitleData):
    DataBase.title_create(
        age_rating = title_data.age_rating,
        ru_name = title_data.ru_name,
        en_name = title_data.en_name,
        alternative_names = title_data.alternative_names,
        release_year = title_data.release_year,
        description = title_data.description,
        status = title_data.status,
        approve_status = 0, 
        translate_status = title_data.translate_status,
        franchise = title_data.franchise,
        author = title_data.author,
        artist = title_data.artist,
        publisher = title_data.publisher
        )

#@title_router.get('/search')
#async def title_search(search_data: ReadTitles):
#    titles = DataBase.session.query(Entities.Title)