#!/usr/bin/python3
"""'review' class for reviews of places"""
from models.base_model import BaseModel


class Review(BaseModel):
    """inherites from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(*args, **kwargs)
            self.place_id =  kwargs.get("place_id")
            self.user_id =  kwargs.get("user_id")
            self.text =  kwargs.get("text")
        else:
            super().__init__()
            self.place_id = ""
            self.user_id = ""
            self.text = ""
