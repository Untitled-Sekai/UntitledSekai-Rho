from pydantic import BaseModel
from sonolus_models import ServiceUserProfile
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    profile: Optional[ServiceUserProfile]
    created_at: datetime

    class Config:
        orm_mode = True
