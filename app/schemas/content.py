from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ContentBase(BaseModel):
    title: str
    body: str
    publish: Optional[bool]= True


class ContentCreate(ContentBase):
    owner_id: Optional[int]=None


class ContentUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None


class ContentOut(ContentBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
