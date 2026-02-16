from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# BOILER PLATE CODE FOR CREATING SQLALCHEMY ENGINE
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Hadiyah%4010@localhost:5432/fastapi"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)
Base = declarative_base()

# CREATING DEPENDENCY FUCNTION WHICH CREATES DB SESSION 
# # API REQUEST ----------> OPEN SESSION -------> API LOGIC CHANGES DB -----------> SESSION CLOSES

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()