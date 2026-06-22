from sqlalchemy.engine import Connection
from ..repos import prompts_repo
from fastapi import HTTPException,status
from ..schemas.prompts_schema import PromptCreate,PromptUpdate
from math import ceil

PAGE_SIZE = 2

def get_pagination_params(page:int=1):
    limit = PAGE_SIZE
    offset = (page-1)*PAGE_SIZE
    pagination = {
        "limit":limit,
        "offset":offset
    }
    return pagination

def get_prompts(conn:Connection,current_user,page:int):
    user_id=current_user['id'] if current_user else None
    pagination=get_pagination_params(page=page)
    all_prompts = prompts_repo.get_prompts(conn=conn,user_id=user_id,pagination=pagination)
    total = prompts_repo.count_no_of_prompts(conn=conn,user_id=user_id)
    return {
        "items":all_prompts,
        "page":page,
        "page_size":PAGE_SIZE,
        "total":total,
        "total_pages":ceil(total/PAGE_SIZE)
    }

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

def get_my_prompts(conn:Connection,current_user,page:int):
    user_id = current_user['id']
    pagination=get_pagination_params(page=page)
    my_prompts = prompts_repo.get_my_prompts(conn=conn,user_id=user_id,pagination=pagination)
    total = prompts_repo.count_no_of_my_prompts(conn=conn,user_id=user_id)
    return {
        "items":my_prompts,
        "page":page,
        "page_size":PAGE_SIZE,
        "total":total,
        "total_pages":ceil(total/PAGE_SIZE)
    }

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

def delete_prompt_by_id(
    prompt_id:int,
    conn:Connection,
    current_user
):
    prompt_data = prompts_repo.get_prompt_data_by_id(conn=conn,prompt_id=prompt_id)
    if prompt_data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if current_user['id']!=prompt_data['user_id']:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not your prompt")
    
    no_of_rows_deleted = prompts_repo.delete_prompt_by_id(conn=conn,prompt_id=prompt_id,user_id=current_user['id'])
    if no_of_rows_deleted ==0:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)    
    return {"message":"deleted success"}

def update_prompt_by_id(
    prompt_id:int,
    prompt_update_data:PromptUpdate,
    conn:Connection,
    current_user
):
    prompt_data = prompts_repo.get_prompt_data_by_id(conn=conn,prompt_id=prompt_id)
    if prompt_data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if current_user['id']!=prompt_data['user_id']:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not your prompt")
    
    result = prompts_repo.update_prompt_by_id(conn=conn,prompt_id=prompt_id,prompt_update_data=prompt_update_data,user_id=current_user['id'])
    if result is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)    
    return result

