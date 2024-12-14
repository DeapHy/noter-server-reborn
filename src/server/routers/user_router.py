from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


from src.server.models.Response import ServerDefaultResponse
from src.database.db_interations import create_user_account, get_ott, login
from src.server.models.User import AuthUserModel

user_router = APIRouter()

default_headers = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*" 
}

@user_router.post("/user")
async def server_create_account(user: AuthUserModel) -> ServerDefaultResponse:
    # Проверка на существование пользователя
    create_user_account(payload={
        "login": user.login,
        "salt": user.salt,
        "hash": user.password_hash,
        "display_name": user.display_name
    })
    return JSONResponse(content=jsonable_encoder(ServerDefaultResponse(success=True)), headers=default_headers)

@user_router.get("/ott")
async def ott():
    status = get_ott(payload={
        "login": "12315"
    })
    return status


@user_router.post("/login")
async def server_login():
    status = login(payload={
        "login": "123",
        "hash": "123"
    })
    return status

@user_router.get("/user/{id}")
async def get_user(id: int):
    ...

@user_router.delete("/user/{id}")
async def delete_user(id: int):
    ...