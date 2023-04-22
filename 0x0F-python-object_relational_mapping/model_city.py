#!/usr/bin/python3
"""Uses SQLAlchemy to create and link class
State to the database table states"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
Base = declarative_base()


class City(Base):
    """ City class which links a table cities in MySQL database"""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    #state = relationship("State", backref="cities")
