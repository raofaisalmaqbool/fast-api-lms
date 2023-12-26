from fastapi import FastAPI

# app = FastAPI()
app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Faisal",
        "email": "faisal@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
