#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    """ creating a table schema for the Base model"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            default = ('updated_at', 'created_at')
            if '__class__' in kwargs:
                del kwargs['__class__']

            if 'id' in kwargs:
                for key, value in kwargs.items():
                    if key in default:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                self.__dict__.update(kwargs)

            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                self.__dict__.update(kwargs)

    def __repr__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        #if '_sa_instance_state' in self.__dict__:
            #del self.__dict__['_sa_instance_state']
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if hasattr(self, "_sa_instance_state"):
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """ deletes the current instance from the storage """
        from models import storage
        storage.delete(self)
        storage.save()
