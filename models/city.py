#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, ForeignKey, Column
from models import storage_type
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, defines a table with state ID and name attributes """
    __tablename__ = 'cities'
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        place = relationship("Place", backref="cities") 
    else:
        name = ""
        state_id = ""
