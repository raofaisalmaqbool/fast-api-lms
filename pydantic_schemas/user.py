from datetime import datetime
from enum import Enum
from pydantic import BaseModel, EmailStr


class UserRole(str, Enum):
    teacher = "teacher"
    student = "student"


class UserBase(BaseModel):
    email: EmailStr
    role: UserRole


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        # orm_mode = True
        from_attributes = True
