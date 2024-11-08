from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str
    role: str

class UserResponse(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True
