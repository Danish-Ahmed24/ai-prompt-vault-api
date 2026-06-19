from pydantic import BaseModel,Field

class UserBase(BaseModel):
    username: str = Field(min_length=1)


class UserCreate(UserBase):
    password: str = Field(min_length=8)

class UserInDb(UserBase):
    hashed_password: str