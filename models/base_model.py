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

    def __str__(self):
        """Print the instance"""
        return "[{}] ({}) {}".format(
          self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Save the instance"""
        self.updated_at = self.id

    def to_dict(self):
        """Return a dictionary containing the instance"""
      dict = {}
      for key, value in self.__dict__.items():
        if key != "id" and key != "created_at" and key != "updated_at":
          dict[key] = value
      return dict
