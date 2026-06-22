from fastapi import Depends,HTTPException,status,Body,APIRouter,Query
from ..auth import dbConn,get_current_optional_user
from typing import Annotated
from ..repos import comments_repo
from ..schemas.comments_schema import Comment
from sqlalchemy.engine import Connection
from math import ceil
from ..services.prompts_service import get_prompt_by_id

PAGE_SIZE = 2

def get_pagination_params(page:int=1):
    limit = PAGE_SIZE
    offset = (page-1)*PAGE_SIZE
    pagination = {
        "limit":limit,
        "offset":offset
    }
    return pagination


def get_comments(
    conn:dbConn,
    prompt_id:int,
    current_user,
    page:Annotated[int,Query(ge=1)]=1,
    ):
    user_id=current_user['id'] if current_user else None
    pagination=get_pagination_params(page=page)
    all_comments = comments_repo.get_comments(conn=conn,prompt_id=prompt_id,user_id=user_id,pagination=pagination)
    total = comments_repo.get_no_of_comments(conn=conn,prompt_id=prompt_id)
    return {
        "items":all_comments,
        "page":page,
        "page_size":PAGE_SIZE,
        "total":total,
        "total_pages":ceil(total/PAGE_SIZE)
    }

def add_comment(conn:Connection,prompt_id:int,comment_data:Comment,current_user):
    prompt = get_prompt_by_id(conn=conn,current_user=None,prompt_id=prompt_id)
    rows_inserted = comments_repo.add_comment(conn=conn,prompt_id=prompt_id,user_id=current_user['id'],comment_data=comment_data)
    if rows_inserted==0:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return {"message":comment_data.message}

def delete_comment(conn:Connection,comment_id:int,current_user):
    rows_deleted = comments_repo.delete_comment(conn=conn,comment_id=comment_id,user_id=current_user['id'])
    if rows_deleted==0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"message":"Comment deleted successfully"}
