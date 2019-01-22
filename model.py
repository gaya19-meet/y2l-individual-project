from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Link(Base):
    __tablename__ = "link"
    id = Column(Integer, primary_key=True)
    subject = Column(String) #math? history? ...
    type = Column(String) #liste,gme,visual
    link = Column(String)
    

