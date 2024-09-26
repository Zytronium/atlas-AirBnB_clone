#!/usr/bin/env python3
"""The base_model module."""
import uuid
import models
from datetime import datetime
from models.engine.file_storage import filestorage as storage

class BaseModel:
    """Base atributes for each instance"""
    def __init__(self, *args, **kwargs):
        """Initialize the instance"""

        if kwargs:
            for name, value in kwargs.items():
                if name == "__class__":
                    self.__dict__[name] = value
                elif name in ("created_at", "updated_at"):
                    self.__dict__[name] = datetime.now()
                else:
                    self.__dict__[name] = value
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)


    def __str__(self):
        """Print the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Save the instance"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing the instance"""
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict

