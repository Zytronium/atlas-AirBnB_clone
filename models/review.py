#!/usr/bin/python3
"""'review' class for reviews of places"""
from models.base_model import BaseModel


class Review(BaseModel):
    """inherites from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
