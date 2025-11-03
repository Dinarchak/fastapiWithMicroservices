from pydantic import BaseModel, Field, EmailStr
from enum import Enum

class UserRole(Enum):
    USER = 'user'
    ADMIN = 'ADMIN'
    SUPERUSER = 'SUPERUSER'


class UserSchema(BaseModel):
    id: int
    username: str = Field(max_length=100)
    email: EmailStr
    full_name: str = Field(max_length=100)
    user_role: UserRole


class UserCreateSchema(BaseModel):
    username: str = Field(max_length=100)
    email: EmailStr
    full_name: str


class UpdateUserRoleSchema(BaseModel):
    role: UserRole
    user_id: int