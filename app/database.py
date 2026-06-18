from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_USER=os.getenv("DB_USER")
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@localhost:3306/promptdb"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

def get_conn():
    with engine.begin() as conn:
        yield conn