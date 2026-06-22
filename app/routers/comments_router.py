from fastapi import Depends,HTTPException,status,Body,APIRouter,Query
from ..auth import dbConn,get_current_optional_user,get_current_user
from typing import Annotated
from ..services import comments_service
from ..schemas.comments_schema import CommentPaginatedResponse,CommentResponse,Comment

router = APIRouter(tags=['comments'])

@router.get("/prompts/{prompt_id}/comments",response_model=CommentPaginatedResponse)
def get_comments(
    conn:dbConn,
    prompt_id:int,
    current_user=Depends(get_current_optional_user),
    page:Annotated[int,Query(ge=1)]=1,
    ):
    return comments_service.get_comments(conn=conn,prompt_id=prompt_id,current_user=current_user,page=page)

@router.post("/prompts/{prompt_id}/comments",response_model=Comment)
def add_comment(
    conn:dbConn,
    prompt_id:int,
    comment_data:Comment,
    current_user=Depends(get_current_user)
):
    return comments_service.add_comment(conn=conn,prompt_id=prompt_id,current_user=current_user,comment_data=comment_data)
