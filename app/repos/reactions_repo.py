from sqlalchemy.engine import Connection
from app.sql.reactions_sql import *
from ..schemas.reactions_schema import ReactionCreate, ReactionDelete

def add_or_update_reaction(
    conn: Connection, 
    user_id: int, 
    reaction_data: ReactionCreate
):
    result = conn.execute(UPSERT_REACTION, {
        "user_id": user_id,
        "target_type": reaction_data.target_type,
        "target_id": reaction_data.target_id,
        "type": reaction_data.type
    })
    return result.rowcount

def remove_reaction(
    conn: Connection,
    user_id: int,
    reaction_data: ReactionDelete
):
    result = conn.execute(DELETE_REACTION, {
        "user_id": user_id,
        "target_type": reaction_data.target_type,
        "target_id": reaction_data.target_id
    })
    return result.rowcount

def get_reaction_stats(
    conn: Connection,
    target_type: str,
    target_id: int
):
    result = conn.execute(GET_REACTION_STATS, {
        "target_type": target_type,
        "target_id": target_id
    })
    row = result.fetchone()
    if row is None:
        return {"likes": 0, "dislikes": 0}
    return {"likes": row[0] or 0, "dislikes": row[1] or 0}

def check_target_exists(
    conn: Connection,
    target_type: str,
    target_id: int
) -> bool:
    if target_type == 'prompt':
        result = conn.execute(CHECK_PROMPT_EXISTS, {"target_id": target_id})
    else:  # comment
        result = conn.execute(CHECK_COMMENT_EXISTS, {"target_id": target_id})
    
    return result.fetchone() is not None
