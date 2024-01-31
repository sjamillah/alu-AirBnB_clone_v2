#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage_type


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    if storage_type == 'db':
        places = relationship("Place", backref="user", cascade="delete")
        reviews = relationship("Review", backref="user", cascade="delete")
