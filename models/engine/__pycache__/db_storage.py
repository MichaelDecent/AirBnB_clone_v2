#!/usr/bin/python3
"""

"""
from sqlalchemy import create_engine


class DBstorage():

    __engine = None
    __session = None

    __init__(self):
    self.__engine = create_engine(f"mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_db")