#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                         '%Y-%m-%dT%H:%M:%S.%f'
                                                         )
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                         '%Y-%m-%dT%H:%M:%S.%f'
                                                         )
            if '__class__' in kwargs:
                del kwargs['__class__']
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        my_dict = dict(self.__dict__)
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        if '_sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        if "_sa_instance_state" in self.__dict__:
            del self.__dict__["_sa_instance_state"]
        dictionary = dict(self.__dict__)
        dictionary['__class__'] = self.__class__.__name__
        if 'created_at' in dictionary:
            dictionary['created_at'] = dictionary['created_at'].isoformat()
        if 'updated_at' in dictionary:
            dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        return dictionary

    def delete(self):
        '''delete the current instance from the storage'''
        storage.delete(self)
