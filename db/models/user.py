"""User and Profile models."""

import enum
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from ..db_setup import Base
from .mixins import Timestamp


class Role(enum.Enum):
    """User role enumeration."""

    teacher = "teacher"
    student = "student"


class User(Timestamp, Base):
    """User model representing system users (teachers and students)."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    role = Column(Enum(Role), nullable=False)
    is_active = Column(Boolean, default=False)

    profile = relationship("Profile", back_populates="owner", uselist=False)
    student_courses = relationship("StudentCourse", back_populates="student")
    student_content_blocks = relationship(
        "CompletedContentBlock", back_populates="student"
    )


class Profile(Timestamp, Base):
    """User profile model with personal information."""

    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="profile")