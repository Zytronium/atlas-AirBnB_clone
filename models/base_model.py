#!/usr/bin/env python3
"""The base_model module."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """base attributes for each instance"""
    def __init__(self, *args, **kwargs):
        """initialize the instance"""
        format = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for nattr, vattr in kwargs.items():
                if nattr == '__class__':
                    continue
                elif nattr in ['created_at', 'updated_at']:
                    self.__dict__[nattr] = datetime.strptime(vattr, format)
                else:
                    self.__dict__[nattr] = vattr                
        else:  # if it's a new instance (not from a dictionary representation)
            models.storage.new(self)
            
    def __str__(self):
        """print the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """save the instance"""
        self.updated_at = datetime.today()
        models.storage.save()
        
    def to_dict(self):
        """return a dictionary containing the instance"""
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
