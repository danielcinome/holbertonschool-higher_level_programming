#!/usr/bin/python3
# Get all states
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City


Base = declarative_base()


class State(Base):
    """
    Table state
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    city = relationship("City",  backref="state", cascade="all, delete, delete-orphan")
