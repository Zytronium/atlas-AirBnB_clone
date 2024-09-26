#!/usr/bin/env python3
"""The base_model module."""
import uuid
import models
from datetime import datetime
from .engine import file_storage



class BaseModel:
    """Base atributes for each instance"""
    def __init__(self, *args, **kwargs):
        """Initialize the instance"""

        format = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for name, value in kwargs.items():
                if name == 'created_at' or name == 'updated_at':
                    self.__dict__[value] = datetime.strptime(value, format)
                else:
                    self.__dict__[name] = value
            

    def __str__(self):
        """Print the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Save the instance"""
        self.updated_at = datetime.today()
        
    def to_dict(self):
        """Return a dictionary containing the instance"""
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at
        dict["updated_at"] = self.updated_at
        return dict

