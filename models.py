
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"

    # add properties here

    # add relationships here


class Zoo(Base):
    __tablename__ = "zoos"

    # add properties here

    # add relationships here