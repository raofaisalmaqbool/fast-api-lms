"""Pydantic schemas for Course models."""

from typing import Optional
from pydantic import BaseModel


class CourseBase(BaseModel):
    """Base course schema with common fields."""

    title: str
    description: Optional[str] = None
    user_id: int


class CourseCreate(CourseBase):
    """Schema for creating a new course."""

    pass


class Course(CourseBase):
    """Schema for course response."""

    id: int

    class Config:
        """Pydantic configuration."""

        from_attributes = True