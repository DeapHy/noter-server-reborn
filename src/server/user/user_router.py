from fastapi import APIRouter
from fastapi import Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


from src.server.models.Response import ServerResponse
from src.database.db_interations import create_account
from src.server.models.User import AuthUserModel

router = APIRouter()

default_headers = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*" 
}

@router.get("/create_account")
async def server_create_account(user: AuthUserModel) -> ServerResponse:
    create_account(payload={
        "login": user.login,
        "salt": user.salt,
        "hash": user.password_hash,
        "display_name": user.display_name
    })
    return JSONResponse(content=jsonable_encoder(ServerResponse(success=True)), headers=default_headers)