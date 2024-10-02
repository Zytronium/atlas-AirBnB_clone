#!/usr/bin/python3
"""'user' class for users on the website"""
from models.base_model import BaseModel


class User(BaseModel):
    """inherites from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __init__(self, *args, **kwargs):  # Chepe helped sort this out
        """initialize the instance"""
        if kwargs:
            super().__init__(*args, **kwargs)
            self.email = kwargs.get("email")
            self.password = kwargs.get("password")
            self.first_name = kwargs.get("first_name")
            self.last_name = kwargs.get("last_name")
        else:
            super().__init__()
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
