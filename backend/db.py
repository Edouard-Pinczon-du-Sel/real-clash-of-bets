# backend/db.py

from sqlalchemy import create_engine, MetaData
from databases import Database

DATABASE_URL = "sqlite:///./clash.db"

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
metadata = MetaData()
