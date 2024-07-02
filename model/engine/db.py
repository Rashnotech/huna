#!/usr/bin/env python3
"""a module that stores the database connection"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from model.base import Base
from model.products import Product
from model.desc import Description
from model.specs import Specification
from model.user import User
from model.order import Order, Item
from model.payment import Payment
from model.reviews import Review
from sys import modules


classes = {'Product': Product, 'Description': Description,
        'Specification': Specification, 'User': User,
        'Review': Review, 'Payment': Payment, 'Order': Order, 'Item': Item
        }


class DBStorage:
    """A class that represents the database connection"""

    __engine = None
    __session = None

    def __init__(self, db_name):
        """initialize the database connection"""
        self.__engine = create_engine(f'sqlite:///{db_name}')
        self.reload()

    def all(self, cls=None):
        """
            Query all object in the current database session.
            Args:
                cls (class): The class to query.
            Return:
                dict: A dictionary with keys in this format
                <class-name>.<object-id>
        """
        obj_dict = {}
        if cls:
            cls = getattr(modules[__name__], cls.__name__)
            result = self.__session.query(cls).all()
        else:
            result = []
            for class_name in classes:
                result.extend(self.__session.query(classes[class_name]).all())
        for obj in result:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            obj_dict[key] = obj
        return obj_dict

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

    def get(self, cls, id):
        """Retrieve objects from storage"""
        obj = self.__session.query(cls).filter_by(id=id).first()
        return obj
    
    def get_email(self, cls, email):
        """Retrieve objects from storage using email"""
        obj = self.__session.query(cls).filter_by(email=email).first()
        return obj

    def empty(self, cls):
        """empty a table"""
        self.__sesssion.query(cls).delete()
        self.save()

    def close(self):
        """close the database connection"""
        self.__session.remove()

    def reload(self):
        """reload the database connection"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
