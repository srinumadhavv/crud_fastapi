import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings

SQLALCHEMY_DATABASE_URL=f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine=create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal =sessionmaker(autocommit=False,autoflush=False,bind=engine) #responsible for talking with the databases

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         conn= psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='623428',cursor_factory=RealDictCursor)
#         cursor=conn.cursor()
#         print("db connection is successfull")
#         break
#     except Exception as error:
#         print("connection to db failed.")
#         print("error",error)
#         time.sleep(2)
