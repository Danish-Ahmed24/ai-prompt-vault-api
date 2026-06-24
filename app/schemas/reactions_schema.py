from pydantic import BaseModel, Field
from enum import Enum

class ReactionTypeEnum(str, Enum):
    like = 'like'
    dislike = 'dislike'

class TargetTypeEnum(str, Enum):
    prompt = 'prompt'
    comment = 'comment'

class ReactionCreate(BaseModel):
    type: ReactionTypeEnum
    target_type: TargetTypeEnum
    target_id: int = Field(gt=0)

class ReactionDelete(BaseModel):
    target_type: TargetTypeEnum
    target_id: int = Field(gt=0)

class ReactionStats(BaseModel):
    likes: int
    dislikes: int
