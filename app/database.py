from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from sqlalchemy.engine import Connection
from typing import Annotated
from fastapi import Depends

load_dotenv()

# Check if DATABASE_URL exists (production) or use local MySQL
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    # Local development
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_USER = os.getenv("DB_USER", "root")
    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@localhost:3306/promptdb"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

def get_conn():
    with engine.begin() as conn:
        yield conn

dbConn = Annotated[Connection,Depends(get_conn)]