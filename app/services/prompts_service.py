from sqlalchemy.engine import Connection
from ..repos import prompts_repo
from fastapi import HTTPException,status
from ..schemas.prompts_schema import PromptCreate
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

def add_prompt(
    prompt_data:PromptCreate,
    conn:Connection,
    current_user
):
    user_id=current_user['id']
    added_prompt=prompts_repo.add_prompt(conn=conn,prompt_data={
        **prompt_data.model_dump(),
        "user_id":user_id
    })
    if added_prompt is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Cannot add prompt")
    return added_prompt