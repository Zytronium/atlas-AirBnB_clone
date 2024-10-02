#!/usr/bin/python3
"""'place' class for a place uploaded to the database"""
from models.base_model import BaseModel


class Place(BaseModel):
    """inherites from BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenities = []
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(*args, **kwargs)
            self.city_id = kwargs.get("city_id")
            self.user_id = kwargs.get("user_id")
            self.name = kwargs.get("name")
            self.description = kwargs.get("description")
            self.number_rooms = kwargs.get("number_rooms")
            self.number_bathrooms = kwargs.get("number_bathrooms")
            self.max_guest = kwargs.get("max_guest")
            self.price_by_night = kwargs.get("price_by_night")
            self.latitude =  kwargs.get("latitude")
            self.longitude =  kwargs.get("longitude")
            self.amenities = kwargs.get("amenities")
        else:
            super().__init__()
            self.city_id = ""
            self.user_id = ""
            self.name = ""
            self.description = ""
            self.number_rooms = 0
            self.number_bathrooms = 0
            self.max_guest = 0
            self.price_by_night = 0
            self.latitude = 0.0
            self.longitude = 0.0
            self.amenities = []
