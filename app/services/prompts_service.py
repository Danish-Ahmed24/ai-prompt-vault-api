from sqlalchemy.engine import Connection
from ..repos import prompts_repo
from fastapi import HTTPException,status

def get_prompts(conn:Connection,current_user):
    user_id=current_user['id'] if current_user else None
    all_prompts = prompts_repo.get_prompts(conn=conn,user_id=user_id)
    return all_prompts



def get_prompt_by_id(
    conn:Connection,
    current_user,
    prompt_id:int
):
    user_id=current_user['id'] if current_user else None
    prompt_by_id = prompts_repo.get_prompt_by_id(conn=conn,prompt_id=prompt_id,user_id=user_id)
    if prompt_by_id is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return prompt_by_id

def get_my_prompts(conn:Connection,current_user):
    user_id = current_user['id']
    my_prompts = prompts_repo.get_my_prompts(conn=conn,user_id=user_id)
    return my_prompts