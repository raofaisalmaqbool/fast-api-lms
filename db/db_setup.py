"""Database configuration and session management."""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URLs - use environment variables in production
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost/lms_db"
)
ASYNC_DATABASE_URL = os.getenv(
    "ASYNC_DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@localhost/lms_db"
)

# Create synchronous engine
engine = create_engine(
    DATABASE_URL,
    connect_args={},
    future=True,
    echo=False,
)

# Create asynchronous engine
async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=False,
)

# Session factories
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True,
)

AsyncSessionLocal = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Base class for ORM models
Base = declarative_base()


def get_db():
    """Get synchronous database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def async_get_db():
    """Get asynchronous database session."""
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()