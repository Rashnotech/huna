#!/usr/bin/env python3
"""a module that stores the database connection"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from models.base import Base
from models.products import Product
from models.desc import Description
from models.specs import Specification
from models.user import User
from models.order import Order, Item
from models.payment import Payment
from models.reviews import Review
from sys import modules
from models.category import Category

classes = {'Product': Product, 'Description': Description,
        'Specification': Specification, 'User': User,
        'Review': Review, 'Payment': Payment, 'Order': Order, 'Item': Item,
        'Category': Category
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

    def rollback(self):
        """Rollback all changes of the current database session"""
        self.__session.rollback()

    def save(self):
        """save an object to the database"""
        try:
            self.__session.commit()
        except:
            self.rollback()
            raise

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

    def get_product(self, cls, prd_id):
        """Retrieve objects from storage using product_id"""
        obj = self.__session.query(cls).filter_by(product_id=prd_id).first()
        return obj

    def find_category(self, cls, name):
        """Retrieve object from storage using name"""
        obj = self.__session.query(cls).filter_by(name=name).first()
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
