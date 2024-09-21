from fastapi import FastAPI
from src.server.user.user_router import router

app = FastAPI()
app.include_router(router)

@app.get("/")
async def root():
    return "/"
