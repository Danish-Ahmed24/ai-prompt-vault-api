from pydantic import BaseModel,Field
from datetime import datetime
from enum import Enum

class Comment(BaseModel):
    message:str

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