# for migration in fast api
alembic revision --autogenerate
alembic upgrade head
alembic downgrade base



# async driver for pg
poetry add asyncpg


# install app
poetry add flake8 black pre-commit
poetry remove flake8 black pre-commit
poetry add -D flake8 black pre-commit
pre-commit install
pre-commit run --all-files