"""Pydantic schemas for User models."""

from datetime import datetime
from enum import Enum
from pydantic import BaseModel, EmailStr


class UserRole(str, Enum):
    """User role enumeration."""

    teacher = "teacher"
    student = "student"


class UserBase(BaseModel):
    """Base user schema with common fields."""

    email: EmailStr
    role: UserRole


class UserCreate(UserBase):
    """Schema for creating a new user."""

    pass


class User(UserBase):
    """Schema for user response."""

    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        """Pydantic configuration."""

        from_attributes = True
