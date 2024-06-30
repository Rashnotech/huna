#!/usr/bin/env python3
"""a module that stores the database connection"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from model.base import Base


class DBStorage:
    """A class that represents the database connection"""

    __engine = None
    __session = None

    def __init__(self, db_name):
        """initialize the database connection"""
        self.__engine = create_engine(f'sqlite:///{db_name}')

    def new(self, obj):
        """add a new object to the database"""
        self.__session.add(obj)

    def save(self):
        """save an object to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an object from the database"""
        if obj:
            self.__session.delete(obj)

    def empty(self, cls):
        """empty a table"""
        cls.drop(self.__engine)

    def close(self):
        """close the database connection"""
        self.__session.remove()

    def reload(self):
        """reload the database connection"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
