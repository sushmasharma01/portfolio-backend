from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class ContactCreateRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: str = Field(min_length=5, max_length=255)
    message: str = Field(min_length=10, max_length=2000)


class ContactResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str
    message: str
    created_at: datetime


class ContactListResponse(BaseModel):
    data: list[ContactResponse]
