import uvicorn
from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from core.config import config

from api import *

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

from constant_data import tags, jenres, roles, priviledges, role_priviledges
from db.db import tag_create, jenre_create, role_create, privillage_create, roleprivillage_create

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
users = FastAPIUsers[User, int](
    get_user_manager=get_user_manager,
    auth_backends=[auth_backend]
)

app.include_router( # /user
    user_router,
    prefix=config.api.prefix.user,
    tags=['user']
)
app.include_router( # /title
    title_router,
    prefix=config.api.prefix.title,
    tags=['title']
)
app.include_router( # /tag
    tags_router,
    prefix=config.api.prefix.tags,
    tags=['tag']
)
app.include_router( # /jenre
    jenres_router,
    prefix=config.api.prefix.jenres,
    tags=['jenre']
)
app.include_router(
    comment_router,
    prefix=config.api.prefix.comment,
    tags=['comment']
)
app.include_router( # /auth/jwt
    users.get_auth_router(auth_backend),
    prefix=config.api.prefix.auth,
    tags=['auth']
)
app.include_router( # /auth
    users.get_register_router(UserRead, UserCreate),
    prefix=config.api.prefix.register,
    tags=['auth']
)
app.include_router( # /
    vue_router,
    prefix=config.api.prefix.default
)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=config.run.host,
        port=config.run.port,
        reload=True
    )
"""