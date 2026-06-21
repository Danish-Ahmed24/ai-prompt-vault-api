from sqlalchemy.engine import Connection
from app.sql.prompts_sql import *


def get_prompts(conn:Connection,user_id:int|None=None):
    if user_id is None:
        result = conn.execute(GET_ALL_PROMPTS_FOR_GUEST_USER)
    else:
        result = conn.execute(GET_ALL_PROMPTS_FOR_LOGGED_USER,{"user_id":user_id})
    return result.mappings().fetchall()

def get_prompt_by_id(
    conn:Connection,
    prompt_id:int,
    user_id:int|None=None
):
    if user_id is None:
        result = conn.execute(GET_PROMPT_BY_ID_GUEST,{
            "prompt_id":prompt_id
        })
    else:
        result = conn.execute(GET_PROMPT_BY_ID_LOGGED,{
            "prompt_id":prompt_id,
            "user_id":user_id
        })
    return result.mappings().fetchone()


def get_my_prompts(conn:Connection,user_id:int):
    result = conn.execute(GET_MY_PROMPTS,{
        "user_id":user_id
    })
    return result.mappings().fetchall()

def add_prompt(conn:Connection,prompt_data:dict):
    result = conn.execute(INSERT_PROMPT,prompt_data)
    return get_prompt_by_id(conn=conn,prompt_id=result.lastrowid,user_id=prompt_data['user_id'])