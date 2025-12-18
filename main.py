"""FastAPI LMS Application Entry Point."""

from fastapi import FastAPI

from api import users, courses, sections
from db.db_setup import engine
from db.models import user, course

# Create database tables
user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fast API LMS",
    description="Learning Management System for managing students and courses.",
    version="0.1.0",
    contact={
        "name": "Faisal Maqbool",
        "email": "faisal.maqbool@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

# Include API routers
app.include_router(users.router, prefix="/api", tags=["users"])
app.include_router(courses.router, prefix="/api", tags=["courses"])
app.include_router(sections.router, prefix="/api", tags=["sections"])


@app.get("/health", tags=["health"])
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}