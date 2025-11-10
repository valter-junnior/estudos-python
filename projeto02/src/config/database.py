from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models import *

URL = "mysql+pymysql://user:password@localhost:3306/database"

engine = create_engine(URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()