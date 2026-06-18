from pydantic import BaseModel
from datetime import datetime

class PromptBase(BaseModel):
    title: str
    content: str


class PromptCreate(PromptBase):
    pass


class PromptUpdate(PromptBase):
    pass


class PromptResponse(PromptBase):
    id: int
    created_at: datetime