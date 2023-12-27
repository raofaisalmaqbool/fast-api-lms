# for migration in fast api
alembic revision --autogenerate
alembic upgrade head
alembic downgrade base
