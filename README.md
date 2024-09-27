# AirBnB Clone Console

---
###### Project Readme Template
This project is all about something.

###### Description and example of concepts in this project 


Example code:
```python
class ToyotaCamry07:
    # (public) class attributes
    manufacturer = "Toyota"
    model_name = "Camry"
    make_year = 2007
    def __init__(self, vin, color, owner, fuel = 100.0, engine_mods = None, destination = None):
        # instance attributes
        self.__vin = vin
        self.color = color
        self._owner = owner
        self._fuel = fuel  # percent of full tank, NOT gallons
        self._engine_mods = engine_mods
        self.__destination = destination

    # it would be a good idea to specify the types and/or raise exceptions to enforce types
    # property getters and setters would also be a good idea
```
