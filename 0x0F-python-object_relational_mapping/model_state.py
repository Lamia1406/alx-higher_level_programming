#!/usr/bin/python3
""" This model contains the class definition of a State class
    and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """ child of Base, links to the MySQL table states"""
    __tablename__ = 'states'
    id = Column(Integer, Sequence("id"), primary_key=True)
    name = Column(String(128), nullable=False)
