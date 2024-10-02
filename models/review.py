#!/usr/bin/python3
"""'review' class for reviews of places"""
from models.base_model import BaseModel


class Review(BaseModel):
    """inherites from BaseModel"""
    def __init__(self):
        super().__init__()
        self.place_id = ""
        self.user_id = ""
        self.text = ""
