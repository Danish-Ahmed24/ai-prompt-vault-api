from sqlalchemy.engine import Connection
from ..repos import prompts_repo
from fastapi import HTTPException,status

def get_prompts(conn:Connection):
    all_prompts = prompts_repo.get_prompts(conn=conn)
    return all_prompts