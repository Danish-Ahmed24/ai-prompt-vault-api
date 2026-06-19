from sqlalchemy.engine import Connection
from app.sql.prompts_sql import *


def get_prompts(conn:Connection):
    result = conn.execute(GET_ALL_PROMPTS)
    return result.mappings().fetchall()