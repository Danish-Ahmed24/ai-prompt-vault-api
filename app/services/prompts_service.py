from sqlalchemy.engine import Connection
from ..repos import prompts_repo
from fastapi import HTTPException,status

def get_prompts(conn:Connection,current_user):
    user_id=current_user['id'] if current_user else 0
    all_prompts = prompts_repo.get_prompts(conn=conn,user_id=user_id)
    return all_prompts



def get_prompt_by_id(
    conn:Connection,
    prompt_id:int
):
    prompt_by_id = prompts_repo.get_prompt_by_id(conn=conn,prompt_id=prompt_id)
    return prompt_id