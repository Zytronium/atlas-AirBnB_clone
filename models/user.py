    #!/usr/bin/python3
"""'user' class for users on the website"""
from models.base_model import BaseModel


class User(BaseModel):
    """inherites from BaseModel"""
    def __init__(self, *args, **kwargs):
        """initialize the instance"""
        super().__init__(**kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
