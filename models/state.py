#!/usr/bin/python3
"""'state' class for the name of the state"""
from models.base_model import BaseModel


class State(BaseModel):
    """inherites from BaseModel"""
    name = ""
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(*args, **kwargs)
            self.name = kwargs.get("name")
        else:
            super().__init__()
            self.name = ""
