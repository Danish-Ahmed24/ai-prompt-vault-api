from fastapi import FastAPI
from app.routers import prompts_router,comments_router,reactions_router
from app import auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(prompts_router.router)
app.include_router(comments_router.router)
app.include_router(reactions_router.router)
app.include_router(auth.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
