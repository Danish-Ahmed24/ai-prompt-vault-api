from fastapi import Depends,HTTPException,status,Body,APIRouter
from app.database import get_conn,dbConn
from typing import Annotated
from sqlalchemy.engine import Connection
from sqlalchemy import text
from ..schemas.prompts_schema import PromptCreate,PromptResponse,PromptUpdate
from app.sql.prompts_sql import *
from ..auth import get_current_user,get_current_optional_user
from ..services import prompts_service

router = APIRouter()



@router.get("/prompts",response_model=list[PromptResponse])
def get_prompts(
    conn:dbConn,
    current_user=Depends(get_current_optional_user)
):
    return prompts_service.get_prompts(conn=conn,current_user=current_user)

@router.get("/users/me/prompts",response_model=list[PromptResponse])
def get_my_prompts(
    conn:dbConn,
    current_user=Depends(get_current_user)
):
    return prompts_service.get_my_prompts(conn=conn,current_user=current_user)

@router.get("/prompts/{prompt_id}",response_model=PromptResponse)
def get_prompt_by_id(
    conn:dbConn,
    prompt_id:int,
    current_user=Depends(get_current_optional_user)
):
    return prompts_service.get_prompt_by_id(conn=conn,current_user=current_user,prompt_id=prompt_id)

@router.post("/prompts",status_code=status.HTTP_201_CREATED,response_model=PromptResponse)
def add_prompt(
    prompt_data: Annotated[PromptCreate,Body()],
    conn:dbConn,
    current_user=Depends(get_current_user)
):
    return prompts_service.add_prompt(prompt_data=prompt_data,conn=conn,current_user=current_user)

@router.delete("/prompts/{prompt_id}")
def delete_prompt_by_id(
    prompt_id:int,
    conn:dbConn,
    current_user=Depends(get_current_user)
):
    return prompts_service.delete_prompt_by_id(prompt_id=prompt_id,conn=conn,current_user=current_user)

@router.put("/prompts/{prompt_id}",response_model=PromptResponse)
def update_prompt_by_id(
    prompt_id:int,
    prompt_update_data:Annotated[PromptUpdate,Body()],
    conn:dbConn,
    current_user=Depends(get_current_user)
):
    return prompts_service.update_prompt_by_id(prompt_id=prompt_id,prompt_update_data=prompt_update_data,conn=conn,current_user=current_user)

