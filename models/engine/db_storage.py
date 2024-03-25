#!/usr/bin/python3
"""DB storage module"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os


class DBStorage:
    """DB storage class"""

    __engine = None
    __session = None

    def __init__(self):
        """Class constructor"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(os.getenv('HBNB_MYSQL_USER'),
                    os.getenv('HBNB_MYSQL_PWD'),
                    os.getenv('HBNB_MYSQL_HOST'),
                    os.getenv('HBNB_MYSQL_DB'),
                    pool_pre_ping=True)
        )
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries on the current database session all objects
        depending on the class name"""
        result = {}
        classes = [cls] if cls else [State, City]
        # Add other classes as needed
        for c in classes:
            objects = self.__session.query(c).all()
            for obj in objects:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                result[key] = obj
        return result

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and creates the current
        database session from the engine"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)()

    def close(self):
        """Closes the current database session"""
        self.__session.remove()
