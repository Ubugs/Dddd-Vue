from typing import Union

from admin.routers import users

from fastapi import FastAPI

from db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

