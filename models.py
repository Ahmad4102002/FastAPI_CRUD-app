# Defingin models here
from sqlalchemy import Column, Integer , String , Boolean, text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base



# DEFINE the structure of the table to be creted in the Posgres 
# database. 
# if tablename is found then no change are made if not found then a
# new tabel is created

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key = True, nullable= False)
    title = Column(String, nullable = False)
    content = Column(String, nullable = False)
    published = Column(Boolean, server_default= text("true"), nullable=False)
    cretaed_at = Column(TIMESTAMP(timezone= True), nullable= False, server_default=text('now()'))

