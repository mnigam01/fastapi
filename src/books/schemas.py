import uuid
from datetime import date, datetime
from typing import List

from pydantic import BaseModel


# class Book(BaseModel):
#     uid: uuid.UUID
#     title: str
#     author: str
#     publisher: str
#     published_date: date
#     page_count: int
#     language: str
#     created_at: datetime
#     update_at: datetime


# class BookCreateModel(BaseModel):
#     title: str
#     author: str
#     publisher: str
#     published_date: str
#     page_count: int
#     language: str


# class BookUpdateModel(BaseModel):
#     title: str
#     author: str
#     publisher: str
#     page_count: int
#     language: str

import uuid
from datetime import datetime
from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str

class BookCreate(BookBase):
    published_date: str


class BookUpdate(BookBase):
    pass

class Book(BookBase):
    uid: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
