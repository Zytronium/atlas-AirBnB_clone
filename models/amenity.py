#!/usr/bin/python3
"""class amenity for the name"""
from models.base_model import BaseModel

class Amenity(BaseModel):
  """inherites from BaseModel"""
  name = ""
  def __init__(self, *args, **kwargs):
    if kwargs:
      super().__init__(*args, **kwargs)
      self.name = kwargs.get('name')
    else:
      super().__init__()
      self.name = ""
