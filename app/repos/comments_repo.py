from sqlalchemy.engine import Connection
from app.sql.comments_sql import *
from ..schemas.comments_schema import Comment

def get_comments(
    conn:Connection,
    prompt_id:int,
    pagination:dict,
    user_id:int|None=None
    ):
    if user_id is None:
        result = conn.execute(GET_ALL_COMMENTS_GUEST,{
            "prompt_id":prompt_id,
            **pagination
            })
    else:
        result = conn.execute(GET_ALL_COMMENTS_LOGGED,{
            "prompt_id":prompt_id,
            "user_id":user_id,
            **pagination
            })
    return result.mappings().fetchall()


def get_no_of_comments(conn:Connection,prompt_id:int):
    result = conn.execute(COUNT_NO_OF_COMMENTS,{
            "prompt_id":prompt_id
            })
    return result.scalar_one() or 0


def add_comment(conn:Connection,prompt_id:int,user_id:int,comment_data:Comment):
    result = conn.execute(ADD_COMMENT,{
        "prompt_id":prompt_id,
        "user_id":user_id,
        **comment_data.model_dump()
    })
    return result.rowcount

def delete_comment(conn:Connection,comment_id:int,user_id:int):
    result = conn.execute(DELETE_COMMENT,{
        "comment_id":comment_id,
        "user_id":user_id
    })
    return result.rowcount