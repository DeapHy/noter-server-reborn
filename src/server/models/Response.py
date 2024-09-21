from pydantic import BaseModel

class ServerResponse(BaseModel):
    success: bool
    details: str | None = None