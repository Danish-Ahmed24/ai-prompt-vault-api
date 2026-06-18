from fastapi import Depends,HTTPException,status,Body,APIRouter
from app.database import get_conn
from typing import Annotated
from sqlalchemy.engine import Connection
from sqlalchemy import text
from app.schemas import PromptCreate,PromptUpdate
from app.sql.prompt import *
from ..auth import get_current_user

router = APIRouter()

@router.get("/prompt/me",tags=['prompt'])
def get_my_prompts(
    conn:Annotated[Connection,Depends(get_conn)],
    current_user=Depends(get_current_user) 
    ):
    result = conn.execute(GET_MY_PROMPTS,{
        "user_id":current_user['id']
    })
    result = result.mappings().fetchall()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Prompts available")
    return result


@router.get("/prompt",tags=['prompt'])
def get_prompts(
    conn:Annotated[Connection,Depends(get_conn)],
    # current_user=Depends(get_current_user) 
    ):
    result = conn.execute(GET_ALL_PROMPTS)
    result = result.mappings().fetchall()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Prompts available")
    return result


@router.get("/prompt/{prompt_id}",tags=['prompt'])
def get_prompt_by_id(
    prompt_id:int,
    conn:Annotated[Connection,Depends(get_conn)],
    # current_user=Depends(get_current_user) 
    ):
    
    
    res = conn.execute(GET_PROMPT_BY_ID,{
        "prompt_id":prompt_id
    })
    res = res.mappings().first()
    if res==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="PROMPT NOT FOUND")
    
    return res 

@router.post("/prompt/add",status_code=status.HTTP_201_CREATED,tags=['prompt'])
def add_prompt(
    prompt_data:Annotated[PromptCreate,Body()],
    conn: Annotated[Connection,Depends(get_conn)],
    current_user=Depends(get_current_user) 
               ):


    res=conn.execute(INSERT_PROMPT,{
        "user_id":current_user['id'],
        **prompt_data.model_dump()
        })
    if res.rowcount==0:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="INSERT FAILED")
    return {
        "message":f"prompt created by {current_user['username']}",
        "id":res.lastrowid,
        "is_private":prompt_data.is_private
    }


@router.delete("/prompt/delete/{prompt_id}",tags=['prompt'])
def delete_prompt_by_id(
    prompt_id:int,
    conn:Annotated[Connection,Depends(get_conn)],
    current_user=Depends(get_current_user)
    ):


    res=conn.execute(DELETE_PROMPT_BY_ID,{
        "prompt_id":prompt_id,
        "user_id":current_user['id']
    })
    if res.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Cannot delete")
    return {
        "message":"deleted",
        "id":prompt_id
    }


@router.put("/prompt/update/{prompt_id}",tags=['prompt'])
def update_prompt_by_id(
    prompt_id:int,
    prompt_data:Annotated[PromptUpdate,Body()],
    conn:Annotated[Connection,Depends(get_conn)],
    current_user=Depends(get_current_user)
    ):

    res=conn.execute(UPDATE_PROMPT_BY_ID,{
        "prompt_id":prompt_id,
        "user_id":current_user['id'],
        **prompt_data.model_dump()
        })
    if res.rowcount==0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Cannot update")
    return {
        "message":"updated",
        "id":prompt_id,
        "data":prompt_data
    }

