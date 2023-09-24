#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models import storage_type

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

    @property
    def cities(self):
        """
        getter for cities attribute that
        returns the list of City instance
        """
        from models import storage
        from models.city import City

        return [obj for obj in models.storage.all(
            City).values() if self.id == obj.state_id]
