#!/usr/bin/python3
"""'state' class for the name of the state"""
from models.base_model import BaseModel


class State(BaseModel):
    """inherites from BaseModel"""
    def __init__(self):
        super().__init__()
        self.name = ""
