"""Course utility functions for database operations."""

from sqlalchemy.orm import Session

from db.models.course import Course
from pydantic_schemas.course import CourseCreate


def get_courses(db: Session, skip: int = 0, limit: int = 100):
    """Get all courses with pagination."""
    return db.query(Course).offset(skip).limit(limit).all()


def get_course(db: Session, course_id: int):
    """Get a course by ID."""
    return db.query(Course).filter(Course.id == course_id).first()


def create_course(db: Session, course: CourseCreate):
    """Create a new course."""
    db_course = Course(
        title=course.title,
        description=course.description,
        user_id=course.user_id,
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def get_user_courses(db: Session, user_id: int):
    """Get all courses created by a specific user."""
    return db.query(Course).filter(Course.user_id == user_id).all()
