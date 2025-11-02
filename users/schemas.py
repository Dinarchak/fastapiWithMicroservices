from pydantic import BaseModel, Field, EmailStr
from enum import Enum

class UserRole(Enum):
    USER = 'user'
    ADMIN = 'ADMIN'
    SUPERUSER = 'SUPERUSER'


class User(BaseModel):
    id: int
    username: str = Field(max_length=100)
    email: EmailStr = None
    full_name: str = Field(max_length=100)
    user_role: UserRole
