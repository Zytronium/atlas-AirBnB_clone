#!/usr/bin/env python3
import uuid

class BaseModel:
    """Base atributes for each instance"""
    def __init__(self, *args, **kwargs):
        """Initialize the instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    self.__dict__[key] = value
                else:
                    setattr(self, key, value)
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = self.id