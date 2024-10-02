#!/usr/bin/python3
"""class city for the name and state_id"""
from models.base_model import BaseModel


class City(BaseModel):
    """inherites from BaseModel"""
    name = ""
    state_id = ""
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(*args, **kwargs)
            self.name = kwargs.get("name")
            self.state_id = kwargs.get("state_id")
        else:
            super().__init__()
            self.name = ""
            self.state_id = ""
