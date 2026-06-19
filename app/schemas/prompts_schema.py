from pydantic import BaseModel,Field
from datetime import datetime

class PromptBase(BaseModel):
    title: str
    content: str
    

class PromptCreate(PromptBase):
    is_private:bool=True


class PromptUpdate(PromptBase):
    is_private:bool


class PromptResponse(PromptBase): 
    id: int
    # user_id: int
    is_private:bool
    created_at: datetime
