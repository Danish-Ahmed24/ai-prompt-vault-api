from fastapi import FastAPI
from app.routers import prompt
from app import auth
app = FastAPI()
app.include_router(prompt.router)
app.include_router(auth.router)

