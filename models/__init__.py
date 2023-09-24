#!/usr/bin/python3
"""
This module contains a script that act as a 'switch'
which allows changing storage type directly by using environmental variable
"""
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE', 'my curent storage type')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
