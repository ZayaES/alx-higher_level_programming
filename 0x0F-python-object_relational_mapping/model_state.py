#!/usr/bin/python3
"""Uses SQLAlchemy to create and link class
State to the database table states"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from model_city import City


Base = declarative_base()


class State(Base):
    """ State class which creates a table state in MySQL database"""

    __tablename__ = "states"
    id = Column(Integer(), nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    #cities = relationship("City", backref="states") 
