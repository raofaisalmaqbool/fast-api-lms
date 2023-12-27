from fastapi import FastAPI
# from fastapi_admin.app import app as admin_app
from api import users, courses, sections
from db.db_setup import engine, SessionLocal
from db.models import user, course
from db.models.user import User

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Gwen",
        "email": "gwen@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

# app.mount("/admin", admin_app)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)