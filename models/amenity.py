#!/usr/bin/python3
"""class amenity for the name"""
from models.base_model import BaseModel

class Amenity(BaseModel):
  """inherites from BaseModel"""
  def __init__(self):
    super().__init__()
    self.name = ""
