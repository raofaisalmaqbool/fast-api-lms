"""Course API routes."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from api.utils.courses import create_course, get_course, get_courses
from db.db_setup import get_db
from pydantic_schemas.course import Course, CourseCreate

router = APIRouter()


@router.get("", response_model=List[Course])
async def read_courses(
    skip: int = Query(0, description="Number of items to skip", ge=0),
    limit: int = Query(100, description="Maximum items to retrieve", le=1000),
    db: Session = Depends(get_db),
):
    """Get all courses with pagination."""
    try:
        courses = get_courses(db, skip=skip, limit=limit)
        return courses
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}"
        )


@router.post("", response_model=Course, status_code=201)
async def create_new_course(course: CourseCreate, db: Session = Depends(get_db)):
    """Create a new course."""
    try:
        return create_course(db=db, course=course)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}"
        )


@router.get("/{course_id}", response_model=Course)
async def read_course(course_id: int, db: Session = Depends(get_db)):
    """Get a course by ID."""
    try:
        course = get_course(db=db, course_id=course_id)
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        return course
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}"
        )


@router.patch("/{course_id}")
async def update_course(course_id: int):
    """Update a course (not yet implemented)."""
    return {"message": "Update endpoint not yet implemented"}


@router.delete("/{course_id}")
async def delete_course(course_id: int):
    """Delete a course (not yet implemented)."""
    return {"message": "Delete endpoint not yet implemented"}


@router.get("/{course_id}/sections")
async def read_course_sections(course_id: int):
    """Get sections for a course (not yet implemented)."""
    return {"message": "Sections endpoint not yet implemented"}
