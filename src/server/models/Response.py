from pydantic import BaseModel

class ServerDefaultResponse(BaseModel):
    success: bool
    details: str | None = None