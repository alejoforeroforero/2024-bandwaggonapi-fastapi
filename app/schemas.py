from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdateName(BaseModel):
    name: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True