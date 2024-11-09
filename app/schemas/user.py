# app/schemas/user.py

from pydantic import BaseModel, EmailStr

# Registro
class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    phone: str

class UserCreate(UserBase):
    password: str
    role: str
class UserResponse(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True

# Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    
#Zona Datos de Usuario
class UserResponse(BaseModel):
    id: int
    full_name: str
    email: str
    phone: str
    role: str
    
    class Config:
        orm_mode = True