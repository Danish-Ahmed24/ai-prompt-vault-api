from pydantic import BaseModel,Field
from datetime import datetime
from enum import Enum

class ReactionType(str,Enum):
    like = 'like'
    dislike = 'dislike'
    none = 'none'

class PromptBase(BaseModel):
    title: str  
    content: str
    

class PromptCreate(PromptBase):
    is_private:bool=True


class PromptUpdate(PromptBase):
    is_private:bool


class PromptResponse(PromptBase): 
    id: int
    author: str
    created_at: datetime
    likes_count: int
    dislikes_count:int
    comments_count:int
    bookmarked:bool | None = None
    my_reaction:ReactionType | None = None

# [
#   {
#     "id": 1,
#     "title": "FastAPI Guide",
#     "content": "....",
#     "author": "ali",
#     "created_at": "2026-06-20T10:00:00Z",
#     "reaction_count": 10,
#     "comment_count": 5
#   }
# ]