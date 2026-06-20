from sqlalchemy.engine import Connection
from app.sql.prompts_sql import *


def get_prompts(conn:Connection,user_id:int=0):
    if user_id==0:
        result = conn.execute(GET_ALL_PROMPTS_FOR_GUEST_USER)
    else:
        result = conn.execute(GET_ALL_PROMPTS_FOR_LOGGED_USER,{"user_id":user_id})
    return result.mappings().fetchall()

def get_prompt_by_id(
    conn:Connection,
    prompt_id:int
):
    result = conn.execute(GET_PROMPT_BY_ID,{
        "prompt_id":prompt_id
    })
    return result.mappings().fetchone()