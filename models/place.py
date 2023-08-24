#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, ForeignKey, Integer, Table
from models import storage_type
from sqlalchemy.orm import relationship
from models.amenity import  Amenity


place_amenity = Table("place_amenity", Base.metadata,
    Column("place_id", String(60),
            ForeignKey('places.id'),
            primary_key=True,
            nullable=False),
    Column("amenity_id", String(60),
            ForeignKey('amenities.id'),
            primary_key=True,
            nullable=False))


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
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary=place_amenity, backref="place", viewonly=False)
        amenity_ids = []

    else:
        city_id = user_id = name = description = ""
        number_rooms = number_bathrooms = max_guest = price_by_night = 0
        latitude = longitude = 0.0
        amenity_ids = []
    
    @property
    def reviews(self):
        from models.review import Review
        from models import storage
        """ getter for reviews that returns a list of Review instances"""
        return [obj for obj in storage.all(Review).values if obj.place_id == self.id]

    @property
    def amenities(self):
        """ a getter for amenities that returns a list of Amenity Instances """
        from models import storage
        return [obj for obj in storage.all(Amenity).values() if obj.id in self.amenity_ids] 
    
    @amenities.setter
    def amenities(self, obj):
        """
        Asetter that for amenities  that handles append method
        for adding an Amenity.id to the attribute amenity_ids
        """
        from models.amenity import Amenity
        if type(obj) != Amenity:
            return
        if obj.id in self.amenity_ids:
            self.amenity_ids.append(obj.id)


            

            

