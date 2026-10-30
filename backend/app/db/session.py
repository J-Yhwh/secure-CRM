from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# load variable from .env file
load_dotenv()

# 1. Get the database URL from enviroment variables
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

#2. Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#3. Create a Session Local class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#4. Create the Bass class - your models (User, Customer) will inherit from this Base)
Base = declarative_base()

#5. Dependency to get DB Session in your routes
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()


