#!/usr/bin/python3
"""
This module defines the City class, which inherits from BaseModel.

"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    City class for representing cities in the AirBnB clone project.

    """
    state_id = ""
    name = ""
