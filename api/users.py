"""User API routes."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from api.utils.courses import get_user_courses
from api.utils.users import (
    create_user,
    get_user,
    get_user_by_email,
    get_users,
)
from db.db_setup import async_get_db, get_db
from pydantic_schemas.course import Course
from pydantic_schemas.user import User, UserCreate

router = APIRouter()


@router.get("", response_model=List[User])
async def read_users(
    skip: int = Query(0, description="Number of items to skip", ge=0),
    limit: int = Query(100, description="Maximum items to retrieve", le=1000),
    db: Session = Depends(get_db),
):
    """Get all users with pagination."""
    try:
        users = get_users(db, skip=skip, limit=limit)
        return users
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}"
        )


@router.post("", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user."""
    try:
        db_user = get_user_by_email(db=db, email=user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return create_user(db=db, user=user)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}"
        )


@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(async_get_db)):
    """Get a user by ID."""
    try:
        db_user = await get_user(db=db, user_id=user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        return db_user
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}"
        )


@router.get("/{user_id}/courses", response_model=List[Course])
async def read_user_courses(user_id: int, db: Session = Depends(get_db)):
    """Get all courses created by a user."""
    try:
        courses = get_user_courses(db=db, user_id=user_id)
        return courses
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}"
        )