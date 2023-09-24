#!/usr/bin/python3
"""

"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User


class DBStorage:

    __engine = None
    __session = None
    __valid_classes = [State, City, Place, Amenity, User, Review]

    def __init__(self):
        """
        setting the instance attributes
        """
        current_env = getenv('HBNB_ENV', 'my current environment')
        usr = getenv('HBNB_MYSQL_USER', 'my user')
        pwd = getenv('HBNB_MYSQL_PWD', 'my password')
        host = getenv('HBNB_MYSQL_HOST', 'my host')
        database = getenv('HBNB_MYSQL_DB', 'my database')

        """Establishing connection"""
        db_url = f"mysql+mysqldb://{usr}:{pwd}@{host}/{database}"
        self.__engine = create_engine(db_url, pool_pre_ping=True)
        if current_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        The queries the database and returns the a dictionary
        objects of the class if passed as a parameter
        if not passed it return a dictionary
        of the the objects of all the subclasses of the BaseModel
            Args:
                cls: the class to return is object
        """
        obj_list = []
        if isinstance(str, cls):
            cls = eval(cls)

        if cls in DBStorage.__valid_classes:
            obj_list = self.__session.query(cls).all()
        else:
            for obj in DBStorage.__valid_classes.values():
                obj_list.extend(self.__session.query(obj).all())

        return {f"{type(obj).__name__}.{obj.id}": obj for obj in obj_list}

    def new(self, obj):
        """
        the adds new obj to the current database
            Args:
                obj: the new object to be added
        """
        self.__session.add(obj)

    def save(self):
        """ saves all changes of the current database """
        self.__session.commit()

    def delete(self, obj=None):
        """
        deletes an object from yhre current database if passed as a argument
        else it does nothing
            Args:
                obj: the object to be deleted
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """ call remove() method on the private session attribute """
        self.__session.remove()
