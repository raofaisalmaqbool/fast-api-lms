from os import stat
from typing import Optional, List
from fastapi import Depends, HTTPException, Query
import fastapi
from sqlalchemy.orm import Session
from api.utils.courses import get_user_courses
from db.db_setup import get_db
from pydantic_schemas.course import Course
from pydantic_schemas.user import UserCreate, User
from api.utils.users import get_user, get_user_by_email, get_users, create_user

from sqlalchemy.ext.asyncio import AsyncSession
from db.db_setup import async_get_db, get_db

router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def read_users(
        skip: int = Query(0, description="Number of items to skip", ge=0),
        limit: int = Query(100, description="Maximum number of items to retrieve", le=1000),
        db: Session = Depends(get_db)):
    try:
        users = get_users(db, skip=skip, limit=limit)
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.post("/users", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        # Check if email is already registered
        db_user = get_user_by_email(db=db, email=user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email is already registered")
        # Create a new user
        return create_user(db=db, user=user)
    except Exception as e:
        # Log the exception or handle it appropriately based on your application's needs
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.get("/users/{user_id}", response_model=User)
# async def read_user(user_id: int, db: Session = Depends(get_db)):
async def read_user(user_id: int, db: AsyncSession = Depends(async_get_db)):
    try:
        # db_user = get_user(db=db, user_id=user_id)
        db_user = await get_user(db=db, user_id=user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        return db_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.get("/users/{user_id}/courses", response_model=List[Course])
async def read_user_courses(user_id: int, db: Session = Depends(get_db)):
    try:
        courses = get_user_courses(db=db, user_id=user_id)
        return courses
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")