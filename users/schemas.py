from pydantic import BaseModel, Field, EmailStr
from enum import Enum

class UserRole(Enum):
    USER = 'USER'
    ADMIN = 'ADMIN'
    SUPERUSER = 'SUPERUSER'


class UserSchema(BaseModel):
    id: int
    username: str = Field(max_length=100)
    email: EmailStr
    full_name: str = Field(max_length=100)
    role_id: int


class UserCreateSchema(BaseModel):
    username: str = Field(max_length=100)
    email: EmailStr
    full_name: str
    password: str


class UpdateUserRoleSchema(BaseModel):
    role: UserRole
    user_id: int


class UserLoginSchema(BaseModel):
    username: str
    password: str