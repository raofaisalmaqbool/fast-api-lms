from os import stat
from typing import Optional, List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from pydantic_schemas.user import UserCreate, User
from api.utils.users import get_user, get_user_by_email, get_users, create_user

router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


# @router.post("/users", response_model=User, status_code=201)
# async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = get_user_by_email(db=db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email is already registered")
#     return create_user(db=db, user=user)


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
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user