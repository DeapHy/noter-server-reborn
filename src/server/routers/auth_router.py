from fastapi import APIrouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.server.models.Response import ServerResponse