#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, ForeignKey, Integer
from models import storage_type
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if storage_type == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship("Review", backref="place")

    else:
        city_id = user_id = name = description = ""
        number_rooms = number_bathrooms = max_guest = price_by_night = 0
        latitude = longitude = 0.0
    
    @property
    def reviews(self):
        """ getter for reviews that returns a list of Review instances"""
        from models.review import Review
        from models import storage
        return [obj for obj in storage.all(Review).values if obj.place_id == self.id]