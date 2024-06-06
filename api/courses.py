from api.utils.courses import get_course, get_courses, create_course
from typing import Optional, List
from fastapi import Depends, HTTPException, Query
import fastapi
from sqlalchemy.orm import Session
from db.db_setup import get_db
from pydantic_schemas.course import CourseCreate, Course


router = fastapi.APIRouter()

@router.get("/courses", response_model=List[Course])
async def read_courses(
        skip: int = Query(0, description="Number of items to skip", ge=0),
        limit: int = Query(100, description="Maximum number of items to retrieve", le=1000),
        db: Session = Depends(get_db)):
    try:
        courses = get_courses(db, skip=skip, limit=limit)
        return courses
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.post("/course", response_model=Course, status_code=201)
async def create_new_course(course: CourseCreate, db: Session = Depends(get_db)):
    try:
        return create_course(db=db, course=course)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.get("/course/{course_id}", response_model=Course)
async def read_course(course_id: int, db: Session = Depends(get_db)):
    try:
        course = get_course(db=db, course_id=course_id)
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        return course
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.patch("/courses/{id}")
async def update_course():
    return {"courses": []}


@router.delete("/courses/{id}")
async def delete_course():
    return {"courses": []}


@router.get("/courses/{id}/sections")
async def read_course_sections():
    return {"courses": []}
