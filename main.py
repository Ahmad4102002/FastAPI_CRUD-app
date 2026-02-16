from fastapi import FastAPI,Depends
from pydantic import BaseModel
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor
import time 
from sqlalchemy.orm import Session 
from . import models
from .database import engine, get_db

# THIS SINGLE LINE combines Postgres and SQLalchemy
models.Base.metadata.create_all(bind=engine)
app = FastAPI()


class Post(BaseModel):

    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

# DB CONNECTION

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Hadiyah@10',
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection established")
        break
    except Exception as error:
        print("Conection to Database failed")
        print("ERROR", error)
        time.sleep(2) 

@app.get("/posts")
def get_posts(db:Session = Depends(get_db)):
    return {"conn": "OK"}

    # REUEST FROM POSTMAN --------------> reaches the get_post function --------------> db logic -------------> SL UERIES / OMR models 
    # ---------> changes through db session--------------> respons geneerated in the get_post function
    # VALIDATE reuest bosy


    # DB LOGIC HAS TWO PARTS SETTING UP THE DB SESSION 

    # CREATING UERIES INSIDE THE API LOGIC 

    # get post from db 