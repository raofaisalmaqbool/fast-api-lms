# FastAPI LMS - Learning Management System

A modern Learning Management System (LMS) built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**. This project provides a robust API for managing users, courses, sections, and learning content.

## Features

- **User Management**: Create and manage teachers and students
- **Course Management**: Create and organize courses with sections
- **Content Management**: Support for lessons, quizzes, and assignments
- **Student Progress Tracking**: Track completed content and grades
- **Async Support**: Built with async/await for high performance
- **Database Migrations**: Alembic integration for schema management
- **API Documentation**: Auto-generated Swagger UI and ReDoc

## Project Structure

```
fast-api-lms/
├── api/                      # API routes and endpoints
│   ├── __init__.py
│   ├── users.py             # User endpoints
│   ├── courses.py           # Course endpoints
│   ├── sections.py          # Section and content block endpoints
│   └── utils/               # Utility functions
│       ├── __init__.py
│       ├── users.py         # User database operations
│       └── courses.py       # Course database operations
├── db/                       # Database configuration
│   ├── __init__.py
│   ├── db_setup.py          # Database engine and session setup
│   └── models/              # SQLAlchemy ORM models
│       ├── __init__.py
│       ├── user.py          # User and Profile models
│       ├── course.py        # Course, Section, and ContentBlock models
│       └── mixins.py        # Reusable model mixins
├── pydantic_schemas/         # Request/response validation schemas
│   ├── __init__.py
│   ├── user.py              # User schemas
│   └── course.py            # Course schemas
├── alembic/                  # Database migrations
├── main.py                   # FastAPI application entry point
├── pyproject.toml           # Poetry dependencies
├── requirements.txt         # pip dependencies
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## Prerequisites

- Python 3.10 or higher
- PostgreSQL 12 or higher
- Poetry (for dependency management)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd fast-api-lms
```

### 2. Set Up Environment Variables

Copy the `.env.example` file to `.env` and update the database credentials:

```bash
cp .env.example .env
```

Edit `.env` with your database configuration:

```env
DATABASE_URL=postgresql+psycopg2://postgres:password@localhost/lms_db
ASYNC_DATABASE_URL=postgresql+asyncpg://postgres:password@localhost/lms_db
```

### 3. Install Dependencies

Using Poetry:

```bash
poetry install
```

Or using pip:

```bash
pip install -r requirements.txt
```

### 4. Create Database

```bash
createdb lms_db
```

### 5. Run Database Migrations

```bash
alembic upgrade head
```

Or create tables automatically:

```bash
python -c "from main import app"
```

## Running the Application

### Development Server

Using Poetry:

```bash
poetry run uvicorn main:app --reload
```

Or directly:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Users

- `GET /api/users` - Get all users (with pagination)
- `POST /api/users` - Create a new user
- `GET /api/users/{user_id}` - Get a specific user
- `GET /api/users/{user_id}/courses` - Get courses created by a user

### Courses

- `GET /api/courses` - Get all courses (with pagination)
- `POST /api/courses` - Create a new course
- `GET /api/courses/{course_id}` - Get a specific course
- `PATCH /api/courses/{course_id}` - Update a course (not yet implemented)
- `DELETE /api/courses/{course_id}` - Delete a course (not yet implemented)
- `GET /api/courses/{course_id}/sections` - Get course sections (not yet implemented)

### Sections

- `GET /api/sections/{section_id}` - Get a section (not yet implemented)
- `GET /api/sections/{section_id}/content-blocks` - Get section content blocks (not yet implemented)
- `GET /api/content-blocks/{block_id}` - Get a content block (not yet implemented)

### Health

- `GET /health` - Health check endpoint

## Database Migrations

### Create a New Migration

```bash
alembic revision --autogenerate -m "Description of changes"
```

### Apply Migrations

```bash
alembic upgrade head
```

### Rollback Migrations

```bash
alembic downgrade base
```

## Code Quality

### Format Code with Black

```bash
black .
```

### Lint with Flake8

```bash
flake8 .
```

### Pre-commit Hooks

Install pre-commit hooks:

```bash
pre-commit install
```

Run hooks on all files:

```bash
pre-commit run --all-files
```

## Development

### Adding New Dependencies

Using Poetry:

```bash
poetry add package-name
```

For development dependencies:

```bash
poetry add -D package-name
```

### Project Standards

- **Code Style**: PEP 8 with Black formatter
- **Line Length**: 79 characters (configurable in pyproject.toml)
- **Python Version**: 3.10+
- **Type Hints**: Encouraged for better code clarity
- **Docstrings**: Use concise docstrings for modules, classes, and functions

## Models

### User Model

- `id` (Integer, Primary Key)
- `email` (String, Unique)
- `role` (Enum: teacher, student)
- `is_active` (Boolean)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### Course Model

- `id` (Integer, Primary Key)
- `title` (String)
- `description` (Text, Optional)
- `user_id` (Foreign Key to User)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### Section Model

- `id` (Integer, Primary Key)
- `title` (String)
- `description` (Text, Optional)
- `course_id` (Foreign Key to Course)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### ContentBlock Model

- `id` (Integer, Primary Key)
- `title` (String)
- `description` (Text, Optional)
- `type` (Enum: lesson, quiz, assignment)
- `url` (URL, Optional)
- `content` (Text, Optional)
- `section_id` (Foreign Key to Section)
- `created_at` (DateTime)
- `updated_at` (DateTime)

## Troubleshooting

### Database Connection Issues

Ensure PostgreSQL is running and the connection string in `.env` is correct:

```bash
psql -U postgres -h localhost -d lms_db
```

### Port Already in Use

If port 8000 is already in use, run on a different port:

```bash
uvicorn main:app --port 8001 --reload
```

### Migration Errors

Reset the database and start fresh:

```bash
dropdb lms_db
createdb lms_db
alembic upgrade head
```

## Contributing

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Commit changes: `git commit -am 'Add feature'`
3. Push to branch: `git push origin feature/your-feature`
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or support, please contact:

- **Name**: Faisal Maqbool
- **Email**: faisal.maqbool@example.com

## Future Enhancements

- [ ] Authentication and authorization (JWT)
- [ ] User profile management
- [ ] Course enrollment system
- [ ] Student progress tracking
- [ ] Grading system
- [ ] Notifications
- [ ] File uploads
- [ ] Search functionality
- [ ] Advanced filtering and sorting
- [ ] Unit and integration tests