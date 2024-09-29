#!/usr/bin/python3
"""'user' class for users on the website"""
from models.base_model import BaseModel


class User(BaseModel):
    """inherites from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initialize the instance"""
        super().__init__(**kwargs)
