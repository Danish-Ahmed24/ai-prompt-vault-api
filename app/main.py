from fastapi import FastAPI
from app.routers import prompt

app = FastAPI()
app.include_router(prompt.router)


