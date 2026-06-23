from pydantic import BaseModel,Field
from datetime import datetime
from enum import Enum

class Comment(BaseModel):
    message: str = Field(min_length=1, max_length=2000)

class CommentResponse(Comment): 
    id:int
    username:str
    created_at:datetime

class CommentPaginatedResponse(BaseModel):
    items:list[CommentResponse]
    page:int
    page_size:int
    total:int
    total_pages:int