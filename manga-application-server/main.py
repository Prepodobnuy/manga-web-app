import uvicorn
from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from core.config import config
from routes.title import title_router
from constant_data import tags, jenres, roles, priviledges, role_priviledges
from db.db import tag_create, jenre_create, role_create, privillage_create, roleprivillage_create

from db.session import get_session_engine
from db.db import Base

session, engine = get_session_engine()
Base.metadata.create_all(bind=engine)
"""
# часть кода нужная для внесения в пустую базу данных необходимой константной информации.
for tag in tags:
    tag_create(tag["ru_name"], tag["en_name"])

for jenre in jenres:
    jenre_create(jenre["ru_name"], jenre["en_name"])

for role in roles:
    role_create(role["ru_name"], role["en_name"], role["ru_desc"], role["en_desc"])

for priviledge in priviledges:
    privillage_create(priviledge["name"])

for role_priviledge in role_priviledges:
    roleprivillage_create(role_priviledge["role_id"], role_priviledge["priviledge_id"])
"""


app = FastAPI(title=config.app.title, version=config.app.version)
app.include_router(
    title_router,
    prefix=config.api.prefix.title
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=config.run.host,
        port=config.run.port,
        reload=True
    )