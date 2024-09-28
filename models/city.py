#!/usr/bin/python3
"""class city for the name and state_id"""
from models.base_model import BaseModel


class City(BaseModel):
    """inherites from BaseModel"""
    name = ""
    state_id = ""
