from fastapi import FastAPI
from app.routers import prompts_router,comments_router
from app import auth
app = FastAPI()
app.include_router(prompts_router.router)
app.include_router(comments_router.router)
app.include_router(auth.router)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
