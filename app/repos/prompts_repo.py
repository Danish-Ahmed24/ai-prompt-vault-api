from sqlalchemy.engine import Connection
from app.sql.prompts_sql import *
from ..schemas.prompts_schema import PromptUpdate

def count_no_of_prompts(conn:Connection,user_id:int|None=None):
    if user_id is None:
        result = conn.execute(COUNT_NO_OF_PUBLIC_PROMPTS_GUEST)
    else:
        result = conn.execute(COUNT_NO_OF_PUBLIC_PROMPTS_LOGGED,{"user_id":user_id})
    return result.scalar_one()

def count_no_of_my_prompts(conn:Connection,user_id:int|None=None):
    result = conn.execute(COUNT_NO_OF_MY_PROMPTS,{"user_id":user_id})
    return result.scalar_one()


def get_prompts(conn:Connection,pagination:dict,user_id:int|None=None):
    
    if user_id is None:
        result = conn.execute(GET_ALL_PROMPTS_FOR_GUEST_USER,pagination)
    else:
        result = conn.execute(GET_ALL_PROMPTS_FOR_LOGGED_USER,{
            "user_id":user_id,
            **pagination
            })
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


def get_my_prompts(conn:Connection,pagination:dict,user_id:int):
    result = conn.execute(GET_MY_PROMPTS,{
        "user_id":user_id,
        **pagination
    })
    return result.mappings().fetchall()

def add_prompt(conn:Connection,prompt_data:dict):
    result = conn.execute(INSERT_PROMPT,prompt_data)
    return get_prompt_by_id(conn=conn,prompt_id=result.lastrowid,user_id=prompt_data['user_id'])

def get_prompt_data_by_id(conn:Connection,prompt_id:int):
    result = conn.execute(GET_PROMPT_DATA_BY_ID,{
        "prompt_id":prompt_id
    })
    return result.mappings().fetchone()

def delete_prompt_by_id(conn:Connection,prompt_id:int,user_id:int):
    result = conn.execute(DELETE_PROMPT_BY_ID,{
        "prompt_id":prompt_id,
        "user_id":user_id
    })
    return result.rowcount

def update_prompt_by_id(
    prompt_id:int,
    prompt_update_data:PromptUpdate,
    conn:Connection,
    user_id:int
):
    result = conn.execute(UPDATE_PROMPT_BY_ID,{
        "prompt_id":prompt_id,
        "user_id":user_id,
        **prompt_update_data.model_dump()
    })
    if result.rowcount == 0:
        return None
    return get_prompt_by_id(conn=conn, prompt_id=prompt_id, user_id=user_id)