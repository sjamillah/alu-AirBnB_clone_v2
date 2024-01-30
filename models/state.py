#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'state'

    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', backref='state', 
                                cascade='all, delete-orphan')

    else:
        @property
        def cities(self):
            """ Returns the list of City instances with state_id
            equals to the current State.id. """
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
