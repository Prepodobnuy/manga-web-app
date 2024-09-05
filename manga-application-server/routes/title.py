from fastapi import APIRouter, HTTPException
from sqlalchemy import func

from core.pydantic_entities import Title, TitleTag, TitleJenre
from db.tables import Title as TitleTable
from db.db import session

title_router = APIRouter()


@title_router.get('/data/{title_id}')
async def get_title(title_id: int) -> Title:
    title = session.query(TitleTable).filter_by(id=title_id).first()
    if title is not None:
        if title.approved:
            return title
        raise HTTPException(403, 'title_is_not_approved')
    raise HTTPException(403, 'title_does_not_exist')

@title_router.post('/new')
async def new_title(title: Title):
    try:
        id = session.query(func.max(TitleTable.id)).scalar() + 1
    except Exception:
        id = 0
    
    _title = TitleTable
    _title.id = id

    _title.original_name = title.original_name
    _title.ru_name = title.ru_name
    _title.en_name = title.en_name
    _title.alternative_names = title.alternative_names
    session.add(_title)
    session.commit()