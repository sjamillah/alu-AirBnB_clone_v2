#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage_type


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete')

    else:
        name = ""

        @property
        def cities(self):
            """ Returns the list of City instances with state_id
            equals to the current State.id. """
            from models import storage
            result = [city for city in models.storage.all(City).values()
                      if city.state_id == self.id]
            return result
