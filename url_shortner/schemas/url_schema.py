from pydantic import BaseModel, HttpUrl
from datetime import datetime

class URLCreate(BaseModel):
    original_url: HttpUrl

class URLResponse(BaseModel):
    id: int
    original_url: str
    short_code: str
    created_at: datetime

    class Config:
        from_attributes = True

class URLListResponse(BaseModel):
    data: list[URLResponse]

class APIResponse(BaseModel):
    status: str
    message: str | None = None
    data: dict | list | None = None