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
    created_at: datetime




class UserBase(BaseModel):
    username: str = Field(min_length=1)


class UserCreate(UserBase):
    password: str = Field(min_length=8)

class UserInDb(UserBase):
    hashed_password: str